from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.http import Http404
from rtiapp import models
import json

def make_profile_context(user):
	context = {
		'user_id' : user.id,
		'first_name' : user.first_name,
		'last_name' : user.last_name,
		'email' : user.email,
	}

	profile = models.User_profile.objects.filter(user = user).first()
	if profile:
		context['reputation'] = profile.reputation
		context['gender'] =  profile.gender
		context['date_of_birth'] = profile.date_of_birth
		context['bio_description'] = profile.bio_description
		context['profile_picture'] = str(profile.profile_picture)
	
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
	return HttpResponse(json.dumps(context))

def do_it():
	u1 = models.User.objects.all().first()
	print make_profile_context(u1)


