from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.http import Http404
from rtiapp import models
import json
from rtiapp import common
from django.views.decorators.csrf import csrf_exempt
from rtiapp.rtiengine import newsfeed, notification
from PIL import Image, ImageOps
from django.core.files import File
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

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
	context['num_rtis'] = len(models.RTI_query.objects.filter(user = user))

	return context

# @login_required
# def get_profile_follow(request):
# 	context = {}
# 	followers = []
# 	max_size = 2
# 	user = models.User.objects.filter(id = request.GET['user_id']).first()
	
# 	if request.GET['details_required'] == "followers":
# 		followers = models.Follow_user.objects.filter(followee = user)
# 		temp = []
# 		for follower in followers:
# 			temp.append(follower.follower)
# 	else:
# 		followers = models.Follow_user.objects.filter(follower = user)
# 		temp = []
# 		for follower in followers:
# 			temp.append(follower.followee)

# 	followers = temp
# 	paginator = Paginator(followers, max_size)
# 	page = 1
# 	if 'page' in request.GET:
# 		page = request.GET['page']
	
# 	followers = paginator.page(page)
# 	user_context_list = []
# 	for follower in followers:
# 		user_context = make_profile_context(follower)
# 		user_context = render_to_response('Profile/user_widget.html', user_context).content
# 		user_context_list.append(user_context)
# 		# user_context['profile_picture'] = str(user_context['profile_picture'])
# 		# context.append(user_context)
# 	context['user_context_list'] = user_context_list

# 	return render_to_response('Profile/user_list.html', context)

@login_required
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
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	context['user_follow_status'] = len(models.Follow_user.objects.filter(follower = request.user, followee = user)) > 0
	context['previous_messages'] = False
	
	if len(models.Message.objects.filter(sender = user, receiver = request.user)) > 0:
		context['previous_messages'] = True
	if len(models.Message.objects.filter(sender = request.user, receiver = user)) > 0:
		context['previous_messages'] = True

	return context

@login_required
def display_user_profile(request, username):
	context = profile_base_context(request, username)
	# return HttpResponse(json.dumps(context))
	return render_to_response('Profile/profile.html', context)

@login_required
def display_user_details(request, username, details_required):
	max_size = 10
	context = profile_base_context(request, username)
	context['details_required'] = details_required
	profile_user = models.User.objects.filter(username = username).first()
	if details_required == 'followers' or details_required == 'following':
		user_list = []
		if details_required == 'followers':
			followers = models.Follow_user.objects.filter(followee = profile_user)
			for f in followers:
				user_list.append(make_profile_context(f.follower))
		else:
			followers = models.Follow_user.objects.filter(follower = profile_user)
			for f in followers:
				user_list.append(make_profile_context(f.followee))
		page = 1
		if 'page' in request.GET:
			page = int(request.GET['page'])
		paginator = Paginator(user_list, max_size)
		user_list = paginator.page(page)
		context['user_list'] = user_list

		page_url_list = []
		
		for i in range(0, paginator.num_pages):
			page_url_list.append({
				'url' : '/profile/' + username + '/' + details_required + '?page=' + str(i+1),
				'page_no' : (i+1),
				'active' : (i+1) == page
				})

		context['page_url_list'] = page_url_list
		context['multiple_pages'] = len(page_url_list) > 1
		return render_to_response('Profile/profile_follow.html', context)
	elif details_required == 'rtis':
		return render_to_response('Profile/profile_rtis.html', context)
	else:
		raise Http404("User Does Not Exist")


# @login_required
@login_required
def get_profile_feed(request):
	# user = models.User.objects.filter(id = request.GET['user_id']).first()
	# if not user:
	# 	return
	# startfeed = int(request.GET['startfeed'])
	# maxfeed = int(request.GET['maxfeed']) + startfeed
	
	# rti_list = models.RTI_query.objects.filter(user = user).order_by('-entry_date')[startfeed: maxfeed]
	# return views_home.get_feed_for_rtis(rti_list, request.user)

	user = models.User.objects.filter(id = request.GET['user_id']).first()
	if not user:
		return
	
	fetched_rti_list = json.loads(request.GET['fetched_rti_list'])
	# print fetched_rti_list
	
	user_activities = models.Activity.objects.filter(user = user).order_by('-entry_date')[0:1000]
	rti_list = []
	rti_mark_list = []
	for activity in user_activities:
		if activity.activity_type == 'spam':
			continue
		rti = activity.rti_query
		
		if (not (rti in rti_mark_list)) and (not rti.id in fetched_rti_list) and len(rti_list) < common.MAX_FEED:
			rti_mark_list.append(rti)
			rti_list.append({
				'rti_query' : rti,
				'rti_head_line' : newsfeed.make_head_line(activity, user)
			})

	return newsfeed.get_feed_for_rtis(rti_list, user)

@login_required
def get_profile_rtis(request):
	user = models.User.objects.filter(id = request.GET['user_id']).first()
	if not user:
		return
	
	fetched_rti_list = json.loads(request.GET['fetched_rti_list'])
	# print fetched_rti_list
	
	user_rtis = models.RTI_query.objects.filter(user = user).order_by('-entry_date')
	rti_list = []
	rti_mark_list = []
	for rti in user_rtis:
		
		
		if (not (rti in rti_mark_list)) and (not rti.id in fetched_rti_list) and len(rti_list) < common.MAX_FEED:
			rti_mark_list.append(rti)
			rti_list.append({
				'rti_query' : rti,
				'rti_head_line' : ""
			})

	return newsfeed.get_feed_for_rtis(rti_list, request.user)

@login_required
def post_follow_user(request):
	me_user = request.user
	other_user = models.User.objects.filter(id = request.GET['other_user_id']).first()
	models.Follow_user.objects.filter(follower = me_user, followee = other_user).delete()
	follow_user = models.Follow_user()
	follow_user.follower = me_user
	follow_user.followee = other_user
	follow_user.save()
	notification.make_follow_notification(follow_user)
	context = {}
	context['num_followers'] = len(models.Follow_user.objects.filter(followee = other_user))
	context['num_following'] = len(models.Follow_user.objects.filter(follower = other_user))
	return HttpResponse(json.dumps(context))

@login_required
def post_unfollow_user(request):
	me_user = request.user
	other_user = models.User.objects.filter(id = request.GET['other_user_id']).first()
	models.Follow_user.objects.filter(follower = me_user, followee = other_user).delete()
	context = {}
	context['num_followers'] = len(models.Follow_user.objects.filter(followee = other_user))
	context['num_following'] = len(models.Follow_user.objects.filter(follower = other_user))
	return HttpResponse(json.dumps(context))

@login_required
@csrf_exempt
def submit_profile_photo(request):
	username = request.user.username
	user_profile = models.User_profile.objects.filter(user = request.user).first()
	for f in request.FILES:
		image_file = request.FILES[f]
		image_file = Image.open(image_file)
		w, h = image_file.size
		d = min(w, h)
		size = (d, d)
		thumb = ImageOps.fit(image_file, size, Image.ANTIALIAS)
		size = (128, 128)
		thumb.thumbnail(size)
		thumb_io = StringIO.StringIO()
		thumb.save(thumb_io, format='JPEG')
		thumb_file = InMemoryUploadedFile(thumb_io, None, str(username) + '.jpg', 'image/jpeg',
                                  thumb_io.len, None)
		
		user_profile.profile_picture = thumb_file
		user_profile.save()

	return HttpResponseRedirect('/profile/' + str(request.user.id))

@login_required
def settings(request):
	return HttpResponse('None')

def do_it():
	u1 = models.User.objects.all().first()
	print make_profile_context(u1)


