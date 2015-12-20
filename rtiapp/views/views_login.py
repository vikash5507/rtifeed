from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from rtiapp import models
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import string
import random
import json
from django.core.mail import EmailMultiAlternatives

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

@csrf_exempt
def email_signup(request):
	print "hello from the server side"
	email = request.POST['email']
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	password = request.POST['password']
	if not(len(first_name) >0) or not(len(last_name) >0) or not(len(email) >0) or not(len(password) >0):
		context = {
			'message_type' : 'error',
			'message_long' : 'Please fill out all the fields',
			'message' : 'Fields not filled'
		}
		return HttpResponse(json.dumps(context))
	email_user = models.Email_user.objects.filter(email = email).first()
	if email_user:
		context = {
			'message_type' : 'error',
			'message_long' : 'Please Login to continue',
			'message' : 'User already registered'
		}
		return HttpResponse(json.dumps(context))
	
	email_user = models.Email_user()
	email_user.email = email
	email_user.first_name = first_name
	email_user.last_name = last_name
	email_user.password = password
	email_user.verification_code = generate_random_code(30)
	email_user.save()
	verify_url = '/verify_email?email=' + str(email)
	verify_url += '&verification_code=' + str(email_user.verification_code)
	verify_url = request.build_absolute_uri(verify_url)
	print verify_url

	emailText = verify_url
	kwargs = {
		"subject": "Verify Your Account",
		"body": emailText,
		"from_email": "rtifeedteam@rtifeed.com",
		"to": ["paarth.n@gmail.com", email_user.email],
	}
	emailHTML = render_to_response('Login/email.html', {'verfication_url' : verify_url}).content
	email = EmailMultiAlternatives(**kwargs)
	email.attach_alternative(emailHTML, "text/html")
	email.send()
	context = {
		'message_type' : 'success',
		'message' : 'Email verification link sent',
		'message_long' : 'Please click on the activation link sent to you, to activate your account',
	}

	return HttpResponse(json.dumps(context))

def verify_email(request):
	print "aha//"
	email = request.GET['email']
	verification_code = request.GET['verification_code']
	print email, verification_code
	email_user = models.Email_user.objects.filter(email = email, verification_code = verification_code).first()
	# print "email_user", email_user.email
	
	if not email_user:
		return render_to_response('Login/login.html', {'error' : "Incorrect verification code"})
	user = models.User.objects.filter(email = email).first()
	
	if not user:
		user = models.User()
		username = email_user.first_name + email_user.last_name
		c = 0
		while len(models.User.objects.filter(username = username)) > 0:
			username = username + str(c)
			c += 1

		user.username = username

	user.email = email_user.email
	user.first_name = email_user.first_name
	user.last_name = email_user.last_name
	user.set_password(email_user.password)
	user.save()
	
	userprofile = models.User_profile.objects.filter(user = user).first()
	if not userprofile:
		userprofile = models.User_profile()
	
	userprofile.user = user
	userprofile.entry_date = datetime.now()
	userprofile.save()
	
	email_user.verified = True
	email_user.save()
	user = authenticate(username = user.username, password = email_user.password)
	login(request, user)
	return HttpResponseRedirect('/profile/' + str(user.username))

def forgot_password(request):
	email = request.GET['email']
	user = models.User.objects.filter(email = email).first()
	if not user:
		email_user = models.Email_user.objects.filter(email = email).first()
		if not email_user:
			context = {
				'message_long' : 'You do not seem to have registered on RTIFeed',
				'message' : 'Email address not registered',
				'message_type' : 'error'
			}
			return HttpResponse(json.dumps(context))

		username = email_user.first_name + email_user.last_name
		c = 0
		while len(models.User.objects.filter(username = username)) > 0:
			username = username + str(c)
			c += 1
		
		user = models.User()
		user.username = username
		user.email = email_user.email
		user.first_name = email_user.first_name
		user.last_name = email_user.last_name
		new_password = generate_random_code(8)
		user.set_password( new_password )
		user.save()

		userprofile = models.User_profile()
		userprofile.user = user
		userprofile.entry_date = datetime.now()
		userprofile.save()
	
	else:
		new_password = generate_random_code(8)
		user.set_password( new_password )
		user.save()

	emailText = 'Hi ' + str(user.first_name) + ','
	emailText += '\nYour new password is ' + str(new_password)
	emailText += '\nPlease login to http://www.rtifeed.com and reset your password.'
	emailText += '\nThanks,'
	emailText += '\nRTIFeed Team'

	kwargs = {
		"subject": "Verify Your Account",
		"body": emailText,
		"from_email": "rtifeedteam@rtifeed.com",
		"to": ["paarth.n@gmail.com", user.email],
	}
	email = EmailMultiAlternatives(**kwargs)
	email.send()

	context = {
		'message_type' : 'success',
		'message' : 'An email with the new password has been sent to you',
		'message_long' : 'PLease login to your account and reset the password',
	}

	return HttpResponse(json.dumps(context))

def generate_random_code(code_length):
	code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(code_length))
	return code


