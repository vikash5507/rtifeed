from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from rtiapp import models
import json

def login_page(request):
	return render_to_response('Login/login.html', {})

def login(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username = username, password = password)
	if user:
		if user.is_active:
			login(request, user)
			return HttpResponse('loggedin')
		else:
			return HttpResponse('disabled')
	else:
		return HttpResponse('invalid')

def u_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def register(request):
	return HttpResponse('registered')
