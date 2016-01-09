from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
from rtiapp.rtiengine import activity_relevance, notification, newsfeed
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import Http404
from rtiapp.views import views_profile
from rtiapp.rtiengine import welcome

def about(request):
	return render_to_response('About/index.html', {})

def faq(request):
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	faqs = models.Faq.objects.all().order_by('priority')
	context['faqs'] = []
	for faq in faqs:
		context['faqs'].append({
			'question' : faq.question,
			'answer' : faq.answer
			})
	return render_to_response('About/faq.html', context)