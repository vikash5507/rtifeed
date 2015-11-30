from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
from rtiapp.rtiengine import activity_relevance, notification, newsfeed
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def delete_rti(request):
	if not request.user.is_superuser:
		raise Http404("Page Not Found")
	rti_id = request.POST['rti_id']
	models.RTI_query.objects.filter(id = rti_id).delete()

def delete_user(request):
	if not request.user.is_superuser:
		raise Http404("Page Not Found")
	user_id = request.POST['user_id']
	models.User.objects.filter(id = user_id).delete()