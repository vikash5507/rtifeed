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

@csrf_exempt
def email_login(request):
	email = request.POST['email']
	password = request.POST['password']
	username = None
	
	user = models.User.objects.filter(email = email).first()
	if user:
		username = user.username
	
	user = authenticate(username = username, password = password)
	
	if user:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect('/home')
		else:
			return HttpResponseRedirect('/login_error_page')
	else:
		return HttpResponseRedirect('/login_error')

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
	
def email_verify_sent(request):
	return render_to_response('Login/email_verification_sent.html')
	
def validate_register_data(user_data):
	return "OK"




