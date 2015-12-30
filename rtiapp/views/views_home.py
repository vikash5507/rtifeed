from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
from rtiapp.rtiengine import activity_relevance, notification, newsfeed
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import Http404

@login_required
def home_page(request):

	user = request.user
	user_profile = models.User_profile.objects.filter(user = user).first()
	if user_profile.profile_status == 'incomplete':
		user_profile.profile_status = 'complete'
		user_profile.save()
		activity_relevance.make_initial_relevance(user)
		return HttpResponseRedirect('/profile/' + user.username)	
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	context['full_feed'] = True
	return render_to_response('Home/home.html', context)

@login_required
def proposed_rtis(request):

	user = request.user
	user_profile = models.User_profile.objects.filter(user = user).first()
	if user_profile.profile_status == 'incomplete':
		user_profile.profile_status = 'complete'
		user_profile.save()
		activity_relevance.update_user_relevance(user)
		return HttpResponseRedirect('/profile/' + user.username)	
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	context['full_feed'] = True
	return render_to_response('Home/proposed_rtis.html', context)

def feedback(request):
	feedback_text = request.GET['feedback_text']
	feedback_model = models.Feedback()
	feedback_model.user = request.user
	feedback_model.feedback_text = feedback_text
	feedback_model.save()
	return HttpResponse(json.dumps('done'))

def rti_page(request, rti_slug):
	user = request.user
	rti_query = models.RTI_query.objects.filter(slug = rti_slug).first()
	if not rti_query:
		raise Http404('Page Not found')

	rti_id = rti_query.id
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	context['rti_query_id'] = rti_id
	context['full_feed'] = False
	context['rti_url'] = '/rti_page/' + rti_query.slug
	context['rti_page'] = True
	
	
	context['feed_box'] = newsfeed.get_feed_for_rti(rti_query, request.user).content

	if len(rti_query.description) > 5:
		context['rti_description'] = rti_query.description
	else:
		context['rti_description'] = rti_query.query_text[0:50] + "..."

	rti_image = models.RTI_query_file.objects.filter(rti_query = rti_query).first()
	if rti_image and rti_image.query_picture:
		context['rti_image_url'] = 'http://www.rtifeed.com/media/' + str(rti_image.query_picture)

	return render_to_response('Home/rtipage.html', context)

@login_required
def get_feed(request):
	user = request.user
	if not user:
		# print "ck"
		return
	
	fetched_rti_list = json.loads(request.GET['fetched_rti_list'])
	# print fetched_rti_list
	
	if 'proposed' in request.GET:
		relevant_activities = models.Activity_relevance.objects.filter(user = user, activity__rti_query__proposed = True).order_by('-relevance')[0:100]
	else:
		relevant_activities = models.Activity_relevance.objects.filter(user = user).order_by('-relevance')[0:100]
	rti_list = []
	rti_mark_list = []
	max_feed = 10

	for activity in relevant_activities:
		if activity.activity.activity_type == 'spam':
			continue
		rti = activity.activity.rti_query
		

		
		if (not (rti in rti_mark_list)) and (not rti.id in fetched_rti_list) and len(rti_list) < max_feed:
			rti_mark_list.append(rti)
			rti_list.append({
				'rti_query' : rti,
				'rti_head_line' : newsfeed.make_head_line(activity.activity, user)
			})
			activity.views += 1
			activity.save()

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

@login_required
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
			meta_data = request.POST['meta_data']
			if not meta_data:
				meta_data = None
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
		activity_relevance.update_activity_relevance(activity)
		notification.make_notification(activity)
	

	comments = models.Activity.objects.filter(rti_query = rti_query, activity_type = 'comment').order_by('-entry_date')
	likes = models.Activity.objects.filter(rti_query = rti_query, activity_type = 'like').order_by('-entry_date')
	follows = models.Activity.objects.filter(rti_query = rti_query, activity_type = 'follow').order_by('-entry_date')
	
	if activity_type == 'comment' and undo == '0':
		context['comment_html'] = newsfeed.get_comment_html(activity, user).content
	
	context['no_comments'] = len(comments)
	context['no_likes'] = len(likes)
	context['no_follows'] = len(follows)

	
	
	return HttpResponse(json.dumps(context))

@csrf_exempt
def post_comment_activity(request):
	comment_id = request.POST['comment_id']
	rti_id = request.POST['rti_id']
	comment_activity = request.POST['comment_activity']

	comment = models.Activity.objects.filter(id = comment_id).first()
	models.Activity.objects.filter(activity_type = 'comment_like', activity_link = comment, user = request.user).delete()

	if comment_activity == 'like':
		activity = models.Activity()
		activity.user = request.user
		activity.rti_query_id = rti_id
		activity.activity_link = comment
		activity.activity_type = 'comment_like'
		activity.save()
		notification.make_notification(activity, comment.user)
	
	context = {
		'no_likes' : len(models.Activity.objects.filter(activity_link = comment, activity_type = 'comment_like'))
	}
	

	return HttpResponse(json.dumps(context))


@login_required
def get_notifications(request):
	context = notification.get_notifications(request.user)
	return HttpResponse(json.dumps(context))

@login_required
def notification_page(request):
	page = 1
	if 'page' in request.GET:
		page = int(request.GET['page'])
	context = notification.get_notifications(request.user, page)
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	return render_to_response('Notification/notification_page.html', context)

@login_required
def mark_all_notifications(request):
	notification.mark_all_notifications(request.user)
	return HttpResponse('OK')
