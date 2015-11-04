from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from rtiapp import models
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def login_page(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/home')
	return render_to_response('Login/login.html', {'error' : False})

def login_error_page(request):
	return render_to_response('Login/login.html', {'error' : "Authentication Failed"})

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

@csrf_exempt
def register(request):
	user = models.User()
	user_data = (request.POST)
	
	
	if validate_register_data(user_data) == 'OK':
		username = user_data['username']
		password = user_data['password']
		repassword = user_data['password']
		email = user_data['email']
		user = User.objects.create_user(username=username,
	                         email=email,
	                         password=password)
		user.first_name = user_data['first_name']
		user.last_name = user_data['last_name']
		user.save()
		
	else:
		return HttpResponse(err)
		

	userprofile = models.User_profile()
	userprofile.user = user
	userprofile.entry_date = datetime.now()
	userprofile.save()

	login(request, user)
	return HttpResponseRedirect('/profile/' + user.username)
	

def validate_register_data(user_data):
	return "OK"




