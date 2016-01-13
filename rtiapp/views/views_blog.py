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

def blog(request, blog_user = None):

	user = request.user
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	if not blog_user:
		blogs = models.Blog.objects.all().order_by('-entry_date')
		top_blog = blogs[0]
		blogs = blogs[1:]
		context['top_blog'] = make_blog_context(top_blog)
		context['top_blog']['blog_text'] = context['top_blog']['blog_text'][0:200] + " .."
	else:
		blogs = models.Blog.objects.filter(user = blog_user).order_by('-entry_date')
		context['blog_user'] = newsfeed.get_profile_context(blog_user)

	page = 1
	
	paginator = Paginator(blogs, 10)
	if 'page' in request.GET:
		page = int(request.GET['page'])
		blogs = paginator.page(page)

	else:
 		blogs = paginator.page(1)
	if page == 1:
		context['main_page'] = 1
	
	page_url_list = []
	for i in range(0, paginator.num_pages):
		page_url_list.append({
			'page_no' : i + 1,
			'url' : '?page=' + str(i+1),
			'active' : (i+1) == page
			})
	if len(page_url_list) > 1:
		context['multiple_pages'] = True

	context['page_url_list'] = page_url_list
	blog_list = []
	for blog in blogs:
		blog_context = make_blog_context(blog)
		blog_list.append(blog_context)

	context['blog_list'] = blog_list
	context['top_writers'] = get_top_writers()
	return render_to_response('Blog/blog_page.html', context)

def blog_page(request, blog_slug):
	blog = models.Blog.objects.filter(slug = blog_slug).first()
	if not blog:
		raise Http404('no found')
	blog.num_views += 1
	blog.save()

	context = {}
	context['blog'] = make_blog_context(blog)
	context['single_blog'] = True
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	context['fb_blog_url'] = "http://www.rtifeed.com/blog/" + blog.slug
	context['trending_list'] = []
	blogs = models.Blog.objects.all().order_by('-entry_date')[0:5]
	for blog in blogs:
		
		bls = {
			'blog_url' : '/blog/' + blog.slug,
			'blog_heading' : blog.heading,
			}
		
		if blog.blog_picture:
			bls['blog_picture'] = blog.blog_picture.url

		context['trending_list'].append(bls)
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
		context['blog_image'] = blog.blog_picture.url
	context['blog_url'] = '/blog/' + blog.slug
	return context

def share_blog(request):
	user = request.user
	# if not user.is_superuser:
	# 	raise Http404('Page Not Found')
	user_profile = models.User_profile.objects.filter(user = request.user).first()
	if not user_profile.is_blogger:
		raise Http404('Cannot find page')

	context = {}
	context['my_profile'] = newsfeed.get_profile_context(user)
	return render_to_response('Blog/post_blog.html', context)

def get_top_writers():
	users = models.User.objects.all()
	top_list = []
	for user in users:
		if user.is_anonymous():
			continue

		no_blogs = len(models.Blog.objects.filter(user = user))
		top_list.append((-no_blogs, user))
	top_list.sort()
	top_list = top_list[0:5]
	top_writers = []
	for user in top_list:
		top_writers.append(newsfeed.get_profile_context(user[1]))
	return top_writers

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