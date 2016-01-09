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

def blog(request):
	user = request.user
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	blogs = models.Blog.objects.all().order_by('-entry_date')
	paginator = Paginator(blogs, 5)
	if 'page' in request.GET:
		blogs = paginator.page(int(request.GET['page']))
	else:
		blogs = paginator.page(1)
	
	blog_list = []
	for blog in blogs:
		blog_context = make_blog_context(blog)
		blog_list.append(blog_context)

	context['blog_list'] = blog_list

	return render_to_response('Blog/blog_page.html', context)

def blog_page(request, blog_slug):
	blog = models.Blog.objects.filter(slug = blog_slug).first()
	
	context = {}
	context['blog'] = make_blog_context(blog)
	context['single_blog'] = True
	context['my_profile'] = newsfeed.get_profile_context(request.user)

	context['trending_list'] = []
	blogs = models.Blog.objects.all().order_by('-entry_date')[0:5]
	for blog in blogs:
		context['trending_list'].append({
			'blog_url' : '/blog/' + blog.slug,
			'blog_heading' : blog.heading,
			'blog_picture' : '/media/' + str(blog.blog_picture)
			})
	print context['trending_list']
	return render_to_response('Blog/blog_page_single.html', context)


def make_blog_context(blog):
	context = {}
	context['blog_user_nameuser'] = blog.user.first_name +  " " + blog.user.last_name
	context['blog_user_username'] = blog.user.username
	context['blog_text'] = blog.blog_text
	context['blog_heading'] = blog.heading
	context['blog_date'] = blog.entry_date
	if blog.blog_picture:
		context['blog_image'] = '/media/' + str(blog.blog_picture)
	context['blog_url'] = '/blog/' + blog.slug
	return context

def share_blog(request):
	user = request.user
	# if not user.is_superuser:
	# 	raise Http404('Page Not Found')

	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	return render_to_response('Blog/post_blog.html', context)

@csrf_exempt
def post_blog(request):
	# print "CHECK CHECK"
	blog_head = request.POST['blog_head']
	blog_text = request.POST['blog_text'].encode('ascii', 'ignore')

	blog = models.Blog()
	blog.user = request.user
	blog.heading = blog_head
	blog.blog_text = blog_text
	
	tags = request.POST['tags']
	for f in request.FILES:
		blog.blog_picture = request.FILES[f]
	
	blog.save()
	
	return HttpResponse('OK')