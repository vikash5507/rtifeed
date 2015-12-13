from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.http import Http404
from rtiapp import models
import json
from rtiapp.rtiengine import newsfeed
from rtiapp.rtiengine import relevance
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login, logout

def bad_request(request):
	return HttpResponse('Bad request')

def permission_denied(request):
	return HttpResponse('Bad request')

def page_not_found(request):
	return HttpResponse('Bad request')

def server_error(request):
	return HttpResponse('Bad request')
