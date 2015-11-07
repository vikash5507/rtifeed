from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.http import Http404
from rtiapp import models
import json
import views_home
from rtiapp.rtiengine import relevance
from rtiapp.views import views_profile

def display_department_profile(request, department_id):
	department = models.Department.objects.filter(id = department_id).first()
	context = make_department_context(department, request.user)
	context['my_profile'] = views_home.get_profile_context(request.user)
	return render_to_response('TDS/tds_profile.html', context)
	

def display_department_details(request, department_id, details_required):
	department = models.Department.objects.filter(id = department_id).first()
	if not department:
		raise Http404("Department Does Not Exist")
	context = make_department_context(department, request.user)
	context['my_profile'] = views_home.get_profile_context(request.user)
	context['details_required'] = 'following'
	if details_required == 'followers':
		return render_to_response('TDS/tds_follow.html', context)
	else:
		raise Http404("Department Does Not Exist")

def display_state_details(request, state_id, details_required):
	state = models.State.objects.filter(id = state_id).first()
	if not state:
		raise Http404("Department Does Not Exist")
	context = make_state_context(state, request.user)
	context['my_profile'] = views_home.get_profile_context(request.user)
	context['details_required'] = 'following'
	if details_required == 'followers':
		return render_to_response('TDS/tds_follow.html', context)
	else:
		raise Http404("Department Does Not Exist")

def display_topic_profile(request, topic_id):
	return HttpResponse('temp')

def display_topic_details(request, topic_id, details_required):
	return HttpResponse('temp')

def display_state_profile(request, state_id):
	state = models.State.objects.filter(id = state_id).first()
	context = make_state_context(state, request.user)
	context['my_profile'] = views_home.get_profile_context(request.user)
	return render_to_response('TDS/tds_profile.html', context)
	



def make_department_context(department, user):
	context = {
		'tds_id' : department.id,
		'tds_type' : 'department',
		'tds_name' : department.department_name,
		'tds_subline' : department.website,
		'tds_website' : department.website,
		'department_type' : department.department_type
	}
	if department.department_type == 'state':
		context['tds_state'] = department.state.state_name
	context['follow_status'] = len(models.Follow_department.objects.filter(followee = department, follower = user)) > 0
	context['tds_no_followers'] = len(models.Follow_department.objects.filter(followee = department))
	rti_queries = models.RTI_query.objects.filter(department = department)
	rti_responses = models.RTI_response.objects.filter(rti_query = rti_queries)
	context['tds_no_rti_queries'] = len(rti_queries)
	context['tds_no_rti_responses'] = len(rti_responses)
	print "FOLLOW STATUS", context['follow_status']
	return context

def make_state_context(state, user):
	context = {
		'tds_id' : state.id,
		'tds_type' : 'state',
		'tds_name' : state.state_name,
		'tds_state_capital' : state.capital_name,
	}
	state_departments = models.State_department.objects.values('department').filter(state = state)
	rti_queries = models.RTI_query.objects.filter(department = state_departments)
	rti_responses = models.RTI_response.objects.filter(rti_query = rti_queries)
	context['tds_no_rti_queries'] = len(rti_queries)
	context['tds_no_rti_responses'] = len(rti_responses)
	context['follow_status'] = len(models.Follow_state.objects.filter(followee = state, follower = user)) > 0
	context['tds_no_followers'] = len(models.Follow_state.objects.filter(followee = state))
	return context

def make_topic_context(topic):
	return {}


def post_follow_tds(request):
	follow = None
	context = {}
	if request.GET['tds_type'] == 'department':
		fe = models.Department.objects.filter(id = request.GET['tds_id']).first()
		models.Follow_department.objects.filter(follower = request.user, followee = fe).delete()
		follow = models.Follow_department()
		follow.follower = request.user
		follow.followee = fe
		follow.save()
		context = make_department_context(fe, request.user)

	elif request.GET['tds_type'] == 'state':
		fe = models.State.objects.filter(id = request.GET['tds_id']).first()
		models.Follow_state.objects.filter(follower = request.user, followee = fe).delete()
		follow = models.Follow_state()
		follow.follower = request.user
		follow.followee = fe
		follow.save()
		context = make_state_context(fe, request.user)

	elif request.GET['tds_type'] == 'topic':
		fe = models.Tag.objects.filter(id = request.GET['tds_id']).first()
		models.Follow_topic.objects.filter(follower = request.user, followee = fe).delete()
		follow = models.Follow_topic()
		follow.follower = request.user
		follow.followee = fe
		follow.save()
		# context['no_followers'] = len(models.Follow_department.objects.filter(followee = fe))
	return HttpResponse(json.dumps(context))

def post_unfollow_tds(request):
	context = {}
	if request.GET['tds_type'] == 'department':
		fe = models.Department.objects.filter(id = request.GET['tds_id']).first()
		models.Follow_department.objects.filter(follower = request.user, followee = fe).delete()
		context = make_department_context(fe, request.user)

	elif request.GET['tds_type'] == 'state':
		fe = models.State.objects.filter(id = request.GET['tds_id']).first()
		models.Follow_state.objects.filter(follower = request.user, followee = fe).delete()
		context = make_state_context(fe, request.user)

	elif request.GET['tds_type'] == 'topic':
		fe = models.Tag.objects.filter(id = request.GET['tds_id']).first()
		models.Follow_topic.objects.filter(follower = request.user, followee = fe).delete()
		context = make_topic_context(fe, request.user)

	return HttpResponse(json.dumps(context))


def get_tds_feed(request):
	startfeed = request.GET['startfeed']
	maxfeed = request.GET['maxfeed']
	tds_id = request.GET['tds_id']
	rti_queries = []

	if request.GET['tds_type'] == 'department':
		department = models.Department.objects.filter(id = tds_id).first()
		rti_queries = models.RTI_query.objects.filter(department = department).order_by('-entry_date')[startfeed : maxfeed]
	elif request.GET['tds_type'] == 'state':
		state = models.State.objects.filter(id = tds_id).first()
		state_departments = models.State_department.objects.values('department').filter(state = state)
		rti_queries = models.RTI_query.objects.filter(department = state_departments).order_by('-entry_date')[startfeed : maxfeed]
	elif request.GET['tds_type'] == 'topic':
		topic = models.Tag.objects.filter(id = tds_id)
		rti_queries = models.RTI_tag.objects.values('rti_query').filter(tag = topic).order_by('-entry_date')[startfeed : maxfeed]

	return views_home.get_feed_for_rtis(rti_queries, request.user)

def get_tds_follow(request):
	context = {}
	tds_id = request.GET['tds_id']
	if request.GET['tds_type'] == 'department':
		department = models.Department.objects.filter(id = tds_id).first()
		followers = models.Follow_department.objects.filter(followee = department)
	elif request.GET['tds_type'] == 'state':
		state = models.State.objects.filter(id = tds_id).first()
		followers = models.Follow_state.objects.filter(followee = state)
	elif request.GET['tds_type'] == 'topic':
		topic = models.Tag.objects.filter(id = tds_id).first()
		followers = models.Follow_topic.objects.filter(followee = tag)

	follower_list = []
	for follower in followers:
		follower_list.append(follower.follower)
	
	user_context_list = []
	for follower in follower_list:
		user_context = views_profile.make_profile_context(follower)
		user_context = render_to_response('Profile/user_widget.html', user_context).content
		user_context_list.append(user_context)
		# user_context['profile_picture'] = str(user_context['profile_picture'])
		# context.append(user_context)
	context['user_context_list'] = user_context_list

	return render_to_response('Profile/user_list.html', context)




