from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.http import Http404
from rtiapp import models
import json
import views_home
from rtiapp.rtiengine import relevance

def make_profile_context(user):
	context = {
		'user_id' : user.id,
		'username' : user.username,
		'first_name' : user.first_name,
		'last_name' : user.last_name,
		'email' : user.email,
		'name_user' : user.first_name + " " + user.last_name
	}

	profile = models.User_profile.objects.filter(user = user).first()
	if profile:
		context['reputation'] = profile.reputation
		context['gender'] =  profile.gender
		context['date_of_birth'] = profile.date_of_birth
		context['bio_description'] = profile.bio_description
		context['profile_picture'] = profile.profile_picture
		if profile.address and profile.address.state:
			context['state'] = profile.state.state_name
	context['num_followers'] = len(models.Follow_user.objects.filter(followee = user))
	context['num_following'] = len(models.Follow_user.objects.filter(follower = user))

	return context

def get_profile_follow(request):
	context = {}
	followers = []
	user = models.User.objects.filter(id = request.GET['user_id']).first()
	start_from = (request.GET['start_from'])
	max_size = (request.GET['max_size'])
	if request.GET['details_required'] == "followers":
		followers = models.Follow_user.objects.filter(followee = user)[start_from : start_from + max_size]
		temp = []
		for follower in followers:
			temp.append(follower.follower)
	else:
		followers = models.Follow_user.objects.filter(follower = user)[start_from : start_from + max_size]
		temp = []
		for follower in followers:
			temp.append(follower.followee)

	followers = temp
	user_context_list = []
	for follower in followers:
		user_context = make_profile_context(follower)
		user_context = render_to_response('Profile/user_widget.html', user_context).content
		user_context_list.append(user_context)
		# user_context['profile_picture'] = str(user_context['profile_picture'])
		# context.append(user_context)
	context['user_context_list'] = user_context_list

	return render_to_response('Profile/user_list.html', context)

def profile_base_context(request, username):
	user = models.User.objects.filter(username = username).first()
	if not user:
		raise Http404("User Does Not Exist")
	context = {}
	if user:
		context = make_profile_context(user)
	if request.user == user:
		context['is_me'] = True
	else:
		context['is_me'] = False
	context['my_profile'] = views_home.get_profile_context(request.user)
	context['user_follow_status'] = len(models.Follow_user.objects.filter(follower = request.user, followee = user)) > 0
	return context

def display_user_profile(request, username):
	context = profile_base_context(request, username)
	# return HttpResponse(json.dumps(context))
	return render_to_response('Profile/profile.html', context)

def display_user_details(request, username, details_required):
	context = profile_base_context(request, username)
	context['details_required'] = details_required

	if details_required == 'followers' or details_required == 'following':
		return render_to_response('Profile/profile_follow.html', context)
	else:
		raise Http404("User Does Not Exist")


# @login_required
def get_profile_feed(request):
	user = models.User.objects.filter(id = request.GET['user_id']).first()
	if not user:
		return
	startfeed = int(request.GET['startfeed'])
	maxfeed = int(request.GET['maxfeed']) + startfeed
	
	rti_list = models.RTI_query.objects.filter(user = user).order_by('-entry_date')[startfeed: maxfeed]
	return views_home.get_feed_for_rtis(rti_list, user)

def post_follow_user(request):
	me_user = request.user
	other_user = models.User.objects.filter(id = request.GET['other_user_id']).first()
	models.Follow_user.objects.filter(follower = me_user, followee = other_user).delete()
	follow_user = models.Follow_user()
	follow_user.follower = me_user
	follow_user.followee = other_user
	follow_user.save()
	relevance.update_relevance_for_user(me_user)
	context = {}
	context['num_followers'] = len(models.Follow_user.objects.filter(followee = other_user))
	context['num_following'] = len(models.Follow_user.objects.filter(follower = other_user))
	return HttpResponse(json.dumps(context))

def post_unfollow_user(request):
	me_user = request.user
	other_user = models.User.objects.filter(id = request.GET['other_user_id']).first()
	models.Follow_user.objects.filter(follower = me_user, followee = other_user).delete()
	relevance.update_relevance_for_user(me_user)
	context = {}
	context['num_followers'] = len(models.Follow_user.objects.filter(followee = other_user))
	context['num_following'] = len(models.Follow_user.objects.filter(follower = other_user))
	return HttpResponse(json.dumps(context))

def settings(request):
	# if request.method != 'POST':
	# 	context = make_profile_context(request.user)
		

	return HttpResponse('None')

def do_it():
	u1 = models.User.objects.all().first()
	print make_profile_context(u1)


