from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models

import json
from django.views.decorators.csrf import csrf_exempt

def make_notification(activity):
	notification = models.Notification()
	notification.user = activity.rti_query.user
	notification.notification_type = 'rti_query'
	notification.activity = activity
	notification.read_status = False
	notification.save()

def get_notifications(user):
	max_notifications = 10
	unread_notifications = models.Notification.objects.filter(user = user, read_status = 0).order_by('-entry_date')
	read_notifications = models.Notification.objects.filter(user = user, read_status = 1).order_by('-entry_date')[10 - len(unread_notifications)]
