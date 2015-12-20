from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models

import json
from django.views.decorators.csrf import csrf_exempt

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


def get_notifications(user):
	max_notifications = 10
	unread_notifications = models.Notification.objects.filter(user = user, read_status = 0).order_by('-entry_date')
	read_notifications = models.Notification.objects.filter(user = user, read_status = 1).order_by('-entry_date')[0:10 - len(unread_notifications)]
	all_notifications = list(unread_notifications) + list(read_notifications)

	notification_list_html = ""
	for notification in all_notifications:
		notification_list_html += make_notification_html(notification).content

	no_unread_notifications = len(unread_notifications)
	context = {
		'no_unread_notifications' : no_unread_notifications,
		'notification_list_html' : notification_list_html
	}
	
	return context

def mark_all_notifications(user):
	notifications = models.Notification.objects.filter(user = user)
	for notification in notifications:
		notification.read_status = 1
		notification.save()
	

def make_notification_html(notification):
	context = {}
	if notification.notification_type == 'rti_query':
		activity = notification.activity
		context['notification_user'] = activity.user.first_name +  " " + activity.user.last_name
		context['notificatin_user_url'] = '/profile/' + activity.user.username
		context['notification_url'] = '/rti_page/' + str(activity.rti_query.id)
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
		
		context['notification_user'] = notification.follow.follower.first_name + " " + notification.follow.follower.last_name
		context['notificatin_user_url'] = '/profile/' + notification.follow.follower.username
		context['notification_url'] = '/profile/' + notification.user.username + '/followers'
		context['notification_text'] = ' followed you'
		
	
	return render_to_response('Notification/notification.html', context)
