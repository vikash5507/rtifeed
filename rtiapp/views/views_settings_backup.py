from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.http import Http404
from rtiapp import models
import json
import views_home
from rtiapp.rtiengine import relevance

def all_settings(request, settings_type):
	if settings_type == 'profile':
		return profile_settings(request)
	else:
		raise Http404("Page not found")

def profile_settings(request):
	return HttpResponse('done')
