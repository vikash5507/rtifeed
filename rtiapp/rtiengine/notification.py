from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

def make_notification(activity, user = None):
	notification = models.Notification()
	if not user:
		if activity.user == activity.rti_query.user:
			return
		notification.user = activity.rti_query.user
	else:
		if activity.user == user:
			return
		notification.user = user
	notification.notification_type = 'rti_query'
	notification.activity = activity
	notification.read_status = False
	notification.save()

def make_follow_notification(follow_user):
	models.Notification.objects.filter(follow = follow_user).delete()
	notification = models.Notification()
	notification.user = follow_user.followee
	notification.notification_type = 'user_follow'
	notification.follow = follow_user
	notification.read_status = False
	notification.save()


def get_notifications(user, page = 1, notification_type = 'all'):
	max_notifications = 8
	unread_notifications = models.Notification.objects.filter(user = user, read_status = 0).order_by('-entry_date')
	read_notifications = models.Notification.objects.filter(user = user, read_status = 1).order_by('-entry_date')
	all_notifications = models.Notification.objects.filter(user = user).order_by('-entry_date')

	last_fetched_id = all_notifications[len(all_notifications) - 1].id
	if notification_type == 'all':
		paginator = Paginator(all_notifications, max_notifications)
	else:
		paginator = Paginator(unread_notifications, max_notifications)
	
	page_notifications = paginator.page(page)

	notification_list_html = ""
	notification_context_list = []
	for notification in page_notifications:
		notification_list_html += make_notification_html(notification).content
		notification_context_list.append( make_notification_context(notification) )

	no_unread_notifications = len(unread_notifications)
	
	page_url_list = []
	for i in range(0, paginator.num_pages):
		page_url_list.append({
			'url' : '/notifications?page='+str(i+1),
			'page_no' : (i + 1),
			'active'  : ((i + 1) == page)
			})
		
	context = {
		'no_unread_notifications' : no_unread_notifications,
		'notification_list_html' : notification_list_html,
		'notification_context_list' : notification_context_list,
		'num_pages'					: paginator.num_pages,
		'page_url_list'				: page_url_list
	}
	
	return context

def mark_all_notifications(user):
	notifications = models.Notification.objects.filter(user = user)
	for notification in notifications:
		notification.read_status = 1
		notification.save()
	
def make_notification_context(notification):
	context = {}
	not_user = None
	if notification.notification_type == 'rti_query':
		activity = notification.activity
		not_user = activity.user
		context['notification_user'] = activity.user.first_name +  " " + activity.user.last_name
		context['notificatin_user_url'] = '/profile/' + activity.user.username
		context['notification_url'] = '/rti_page/' + str(activity.rti_query.slug)
		notification_text = ""

		if activity.activity_type == 'comment':
			notification_text = ' commented on your RTI'
		elif activity.activity_type == 'like':
			notification_text = ' liked your RTI'
		elif activity.activity_type == 'follow':
			notification_text = ' followed your RTI'
		elif activity.activity_type == 'spam':
			notification_text = ' marked your RTI as spam'
		elif activity.activity_type == 'comment_like':
			notification_text = ' liked your comment'
		context['notification_text'] = notification_text
	
	elif notification.notification_type == 'user_follow':
		not_user = notification.follow.follower
		context['notification_user'] = notification.follow.follower.first_name + " " + notification.follow.follower.last_name
		context['notificatin_user_url'] = '/profile/' + notification.follow.follower.username
		context['notification_url'] = '/profile/' + notification.user.username + '/followers'
		context['notification_text'] = ' followed you'
	user_profile = models.User_profile.objects.filter(user = not_user).first()
	if user_profile:
		context['notification_image'] = user_profile.profile_picture.url
	return context

def make_notification_html(notification):
	context = make_notification_context(notification)
	return render_to_response('Notification/notification.html', context)
