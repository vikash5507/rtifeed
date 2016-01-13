from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
from rtiapp.rtiengine import relevance, notification
from rtiapp.views import views_profile
from rtiapp.rtiengine import activity_relevance
import json

def get_states_list():
	states = models.State.objects.all().order_by('state_name')
	context = []
	for state in states:
		context.append({
			'state_id' : state.id,
			'state_name' : state.state_name,
			})
	return context

def get_trending_users():
	users = models.User.objects.all()
	user_profiles = models.User_profile.objects.order_by('-reputation')[0:10]
	context = []
	for u in user_profiles:
		context.append(views_profile.make_profile_context( u.user ))
	return context

def save_user_preference(request):
	state_ids =  json.loads(request.GET['states'])
	user_ids =  json.loads(request.GET['users'])

	total_activities = 0
	
	for st_id in state_ids:
		state = models.State.objects.filter(id = int(st_id)).first()
		models.Follow_state.objects.filter(follower = request.user, followee_id = state).delete()

		fs = models.Follow_state()
		fs.follower = request.user
		fs.followee = state
		fs.save()

		
		activities = models.Activity.objects.filter(activity_type = 'rti_query', rti_query__department__state = state ).order_by('-entry_date')
		if len(activities) > 0:
			activities = activities[0:50]
			for activity in activities:
				activity_relevance.calc_relevance(request.user, activity)
				total_activities += 1
		
	activities = models.Activity.objects.filter(activity_type = 'rti_query', rti_query__department__state = None ).order_by('-entry_date')
	activities = activities[0:50]
	for activity in activities:
		activity_relevance.calc_relevance(request.user, activity)
		total_activities += 1

	for ur_id in user_ids:
		f_user = models.User.objects.filter(id = int(ur_id)).first()
		models.Follow_user.objects.filter(follower = request.user, followee_id = f_user).delete()
		
		fu = models.Follow_user()
		fu.follower = request.user
		fu.followee = f_user
		fu.save()
		notification.make_follow_notification(fu)
		
		activities = models.Activity.objects.filter(user = f_user).order_by('-entry_date')
		if len(activities) > 0:
			activities = activities[0:50]
			for activity in activities:
				activity_relevance.calc_relevance(request.user, activity)
				total_activities += 1
		
	
	activities = models.Activity.objects.filter(activity_type = 'rti_query').order_by('-entry_date')
	for activity in activities:
		if total_activities >= 100:
			break
		activity_relevance.calc_relevance(request.user, activity)
		total_activities += 1


	user_profile = models.User_profile.objects.filter(user = request.user).first()
	user_profile.profile_status = 'complete'
	user_profile.save()
	
	return HttpResponse('done')