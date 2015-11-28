from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
from rtiapp.rtiengine import relevance, notification, newsfeed
import json
from django.views.decorators.csrf import csrf_exempt

@login_required
def home_page(request):

	user = request.user
	user_profile = models.User_profile.objects.filter(user = user).first()
	if user_profile.profile_status == 'incomplete':
		user_profile.profile_status = 'complete'
		user_profile.save()
		return HttpResponseRedirect('/profile/' + user.username)	
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	context['full_feed'] = True
	return render_to_response('Home/home.html', context)

def rti_page(request):
	user = request.user
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	context['rti_query_id'] = request.GET['rti_query_id']
	context['full_feed'] = False
	return render_to_response('Home/home.html', context)

@login_required
def get_feed(request):
	user = request.user
	if not user:
		return
	
	fetched_rti_list = json.loads(request.GET['fetched_rti_list'])
	print fetched_rti_list
	
	relevant_activities = models.Activity_relevance.objects.filter(user = user).order_by('-relevance')
	rti_list = []
	rti_mark_list = []
	for activity in relevant_activities:
		if activity.activity.activity_type == 'spam':
			continue
		rti = activity.activity.rti_query
		activity.views += 1
		activity.save()

		
		if (not (rti in rti_mark_list)) and (not rti.id in fetched_rti_list):
			rti_mark_list.append(rti)
			rti_list.append({
				'rti_query' : rti,
				'rti_head_line' : newsfeed.make_head_line(activity.activity, user)
			})

	return newsfeed.get_feed_for_rtis(rti_list, user)

def view_rti(request):
	user = request.user
	if not user:
		return
	rti = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()
	if rti:
		return newsfeed.get_feed_for_rti(rti, user)
	else:
		return HttpResponse("404")

def load_prev_comments(request):
	user = request.user
	rti_query = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()
	comments = models.Activity.objects.filter(rti_query = rti_query, activity_type = 'comment').order_by('entry_date')
	comment_html = ""
	for comment in comments:
		comment_html += newsfeed.get_comment_html(comment, user).content
	context = {
		comment_html : comment_html
	}
	return HttpResponse(context)

@login_required
@csrf_exempt
def post_rti_activity(request):
	user = request.user
	rti_query = models.RTI_query.objects.filter(id = request.POST['rti_query_id']).first()
	undo = request.POST['undo']
	edit = request.POST['edit']
	activity_type = request.POST['activity_type']

	meta_data = None
	context = {}
	if undo == '1':
		
		if activity_type == 'comment':
			models.Activity.objects.filter(user = user, rti_query = rti_query, id = request.POST['comment_id']).delete()
		else:
			models.Activity.objects.filter(user = user, rti_query = rti_query, activity_type = activity_type).delete()
	else:
		if activity_type == 'comment':
			comment_text = request.POST['comment_text']
			meta_data = json.dumps({'comment_text' : comment_text})
		else:
			models.Activity.objects.filter(user = user, rti_query = rti_query, activity_type = activity_type).delete()
		
		if request.POST['edit'] == '1':
			activity = models.Activity.objects.filter(id = request.POST['comment_id']).first()
		else:
			activity = models.Activity()

		activity.user = user
		activity.rti_query = rti_query
		activity.activity_type = activity_type
		activity.meta_data = meta_data

		activity.save()
		notification.make_notification(activity)
	

	comments = models.Activity.objects.filter(rti_query = rti_query, activity_type = 'comment').order_by('-entry_date')
	likes = models.Activity.objects.filter(rti_query = rti_query, activity_type = 'like').order_by('-entry_date')
	shares = models.Activity.objects.filter(rti_query = rti_query, activity_type = 'share').order_by('-entry_date')
	
	if activity_type == 'comment' and undo == '0':
		context['comment_html'] = newsfeed.get_comment_html(activity, user).content
	context['no_comments'] = len(comments)
	context['no_likes'] = len(likes)
	context['no_shares'] = len(shares)

	relevance.update_relevance_for_rti(rti_query)
	
	return HttpResponse(json.dumps(context))

def get_notifications(request):
	notifications = notification.get_notifications(request.user)
	return HttpResponse(json.dumps(notifications))