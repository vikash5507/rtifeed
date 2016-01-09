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

def sitemap(request):
	return render_to_response('Sitemap/sitemap.html')

def sitemap_rtis(request):
	rtis = models.RTI_query.objects.all()
	paginator = Paginator(rtis, 50)
	
	if 'page' in request.GET:
		rtis = paginator.page(int(request.GET['page']))
	else:
		rtis = paginator.page(1)

	rti_list = []
	for rti in rtis:
		rti_list.append({
			'rti_url' : '/rti_page/' + str(rti.slug),
		})
	
	page_list = []
	for i in range(0, paginator.num_pages):
		page_list.append({ 'url' : '/sitemap/rtis?page=' + str(i+1), 'page_no' : (i+1)})

	context = {
		'rti_list' : rti_list,
		'num_pages' : paginator.num_pages,
		'page_list' : page_list
	}

	return render_to_response('Sitemap/rtis.html', context)

def sitemap_users(request):
	users = models.User.objects.all()
	paginator = Paginator(users, 50)
	
	if 'page' in request.GET:
		users = paginator.page(int(request.GET['page']))
	else:
		users = paginator.page(1)

	user_list = []
	for user in users:
		user_list.append({
			'user_url' : '/profile/' + str(user.username)
		})

	page_list = []
	for i in range(0, paginator.num_pages):
		page_list.append({ 'url' : '/sitemap/users?page=' + str(i+1), 'page_no' : (i+1)})

	context = {
		'user_list' : user_list,
		'num_pages' : paginator.num_pages,
		'page_list' : page_list
	}
	return render_to_response('Sitemap/users.html', context)


def sitemap_tdss(request):
	tds_type = request.GET['tds_type']
	if tds_type == 'state':
		tdss = models.State.objects.all()
	elif tds_type == 'department':
		tdss = models.Department.objects.all()
	elif tds_type == 'topic':
		tdss = models.Tag.objects.all()

	paginator = Paginator(tdss, 50)
	
	if 'page' in request.GET:
		tdss = paginator.page(int(request.GET['page']))
	else:
		tdss = paginator.page(1)

	tds_list = []
	for tds in tdss:
		if tds_type == 'state':
			tds_list.append({
				'tds_url' : '/state/' +  tds.slug
			})
		elif tds_type == 'department':
			tds_list.append({
				'tds_url' : '/department/' +  tds.slug
			})
		elif tds_type == 'topic':
			tds_list.append({
				'tds_url' : '/topic/' +  tds.slug
			})
	print tds_list	
	page_list = []
	for i in range(0, paginator.num_pages):
		page_list.append({ 'url' : '/sitemap/tds?tds_type='+str(tds_type)+'&page=' + str(i+1), 'page_no' : (i+1)})

	context = {
		'tds_list' : tds_list,
		'num_pages' : paginator.num_pages,
		'page_list' : page_list
	}

	return render_to_response('Sitemap/tdss.html', context)
