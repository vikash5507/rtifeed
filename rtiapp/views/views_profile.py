from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.http import Http404
from rtiapp import models
import json
import views_home

def make_profile_context(user):
	context = {
		'user_id' : user.id,
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

def make_follow_context(user, start_from = 0, limit = True, max_size = 30, ftype = "followers"):
	context = []
	followers = []
	if ftype == "followers":
		if not limit:
			followers = models.Follow_user.objects.filter(followee = user)
		else:
			followers = models.Follow_user.objects.filter(followee = user)[start_from : start_from + max_size]
	else:
		if not limit:
			followers = models.Follow_user.objects.filter(follower = user)
		else:
			followers = models.Follow_user.objects.filter(follower = user)[start_from : start_from + max_size]


	for follower in followers:
		context.append({
			'user_id' : follower.id,
			'first_name' : follower.first_name,
			'last_name' : follower.last_name,
			'email' : follower.email,
			})
	
	return context

def get_user_profile(request, username):
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
	# return HttpResponse(json.dumps(context))
	return render_to_response('Profile/profile.html', context)


# @login_required
def get_profile_feed(request):
	user = models.User.objects.filter(id = request.GET['user_id']).first()
	if not user:
		return
	startfeed = int(request.GET['startfeed'])
	maxfeed = int(request.GET['maxfeed']) + startfeed
	
	rti_list = models.RTI_query.objects.filter(user = user).order_by('-entry_date')[startfeed: maxfeed]
	return views_home.get_feed_for_rtis(rti_list, user)

def do_it():
	u1 = models.User.objects.all().first()
	print make_profile_context(u1)


