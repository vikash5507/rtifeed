from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.http import Http404
from rtiapp import models
import json
from rtiapp.rtiengine import newsfeed
from rtiapp.rtiengine import relevance

# def all_settings(request, settings_type):
# 	if settings_type == 'profile':
# 		return profile_settings(request)
# 	else if settings_type == 'password':
# 		return password_settings(request)
# 	else:
# 		raise Http404("Page not found")

def profile_settings(request):
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	return render(request,'Settings/profile.html',context)

def password_settings(request):
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	return render(request,'Settings/password.html',context)
