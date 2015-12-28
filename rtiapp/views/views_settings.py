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
from django.contrib.auth.decorators import login_required
# def all_settings(request, settings_type):
# 	if settings_type == 'profile':
# 		return profile_settings(request)
# 	else if settings_type == 'password':
# 		return password_settings(request)
# 	else:
# 		raise Http404("Page not found")

@login_required
def profile_settings(request):
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	return render(request,'Settings/profile.html',context)

@login_required
def password_settings(request):
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	return render(request,'Settings/password.html',context)

@login_required
@csrf_exempt
def update_settings(request):
	print "checl"
	setting_type = request.POST['setting_type']

	print setting_type
	if setting_type == 'profile':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		bio_description = request.POST['bio_description']
		
		user = request.user
		if len(first_name) > 0:
			user.username = username
			user.first_name = first_name
			user.last_name = last_name
			user.save()

			user_profile = models.User_profile.objects.filter(user = user).first()
			user_profile.bio_description = bio_description
			user_profile.save()

			return HttpResponse('done')
		else:
			raise Http404('Bad Input')
	elif setting_type == 'password':
		user = request.user
		old_password = request.POST['old_password']
		new_password = request.POST['new_password']
		check_user = authenticate(username = user.username, password = old_password)
		
		if check_user == None:
			print "ab theek hai na"
			raise Http404('OK')
		else:
			user.set_password(new_password)
        	user.save()
        	user = authenticate(username = user.username, password = new_password)
        	login(request, user)
        	return HttpResponse('done')