from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
import json

@login_required
def home_page(request):
	user = request.user
	user_profile = models.User_profile.objects.filter(user = user).first()

	context = {
		'uid' : user.id,
		'name_user': user.first_name + " " + user.last_name,
		'profile_picture' : user_profile.profile_picture
		}
	return render_to_response('Home/home.html', context)

@login_required
def get_feed(request):
	user = request.user
	if not user:
		return
	startfeed = int(request.GET['startfeed'])
	maxfeed = int(request.GET['maxfeed']) + startfeed
	rel_objects = models.Relevance.objects.filter(user = user).order_by('-relevance')[startfeed:maxfeed]

	rti_list = []
	for rel in rel_objects:
		rti_list.append(rel.rti_query)

	return get_feed_for_rtis(rti_list)

def get_feed_for_rtis(rti_list):
	html_string = ""
	for rti in rti_list:
		rti_html = get_feed_for_rti(rti)
		html_string += rti_html.content
	return HttpResponse(html_string)


def get_feed_for_rti(rti):
	profile = models.User_profile.objects.filter(user = rti.user).first()

	rti_context = {
		'rti_id' : rti.id,
		'rti_user' : rti.user.first_name + " " + rti.user.last_name,
		'rti_query_text' : rti.query_text,
		'rti_rti_number' : rti.rti_number,
		'rti_description' : rti.description,
		'rti_file_date' : rti.rti_file_date,
		'rti_entry_date' : rti.entry_date,
		'rti_query_type' : rti.query_type,
		'rti_response_status' : rti.response_status
	}
	if profile:
		rti_context['rti_user_pic'] = profile.profile_picture
	if rti_context['rti_query_type'] == 'centre':
		centre_rti = models.Central_RTI_query.objects.filter(rti_query = rti).first()
		if centre_rti:
			rti_context['rti_department'] = centre_rti.department.department_name

	else:
		state_rti = models.State_RTI_query.objects.filter(rti_query = rti).first()
		if state_rti:
			rti_context['rti_state'] = state_rti.department.state.state_name
			rti_context['rti_department'] = state_rti.department.department_name

	if rti.response_status:
		response = models.RTI_Response.objects.filter(rti_query = rti).first()
		if response:
			rti_context['response_text'] = response.response_text
			rti_context['response_description'] = response.description
			rti_context['response_file_date'] = response.rti_response_date
			rti_context['response_entry_date'] = response.entry_date

	

	comments = models.Comment.objects.filter(rti_query = rti).order_by('-entry_date')
	likes = models.Like.objects.filter(rti_query = rti).order_by('entry_date')
	shares = models.Share.objects.filter(rti_query = rti).order_by('entry_date')

	rti_context['no_comments'] = len(comments)
	rti_context['no_likes'] = len(likes)
	rti_context['no_shares'] = len(shares)

	rti_context['top_comments'] = comments[0:2]
	comment_html = ""
	for comment in rti_context['top_comments']:
		comment_html += get_comment_html(comment).content

	rti_context['comment_html'] = comment_html
	rti_html = render_to_response('Home/feedbox.html', rti_context)
	return rti_html

def get_comment_html(comment):
	profile = models.User_profile.objects.filter(user = comment.user).first()
	context = {
		'comment_text' : comment.comment_text,
		'comment_user_id' : comment.user.id,
		'comment_user_pic' : profile.profile_picture,
		'comment_name_user' : comment.user.first_name + " " + comment.user.last_name,
		'comment_date' : comment.entry_date
	}
	return render_to_response('Home/comment.html', context)

@login_required
def post_comment(request):
	user = request.user
	comment_text = request.GET['comment_text']
	rti_query = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()

	comment = models.Comment()
	comment.user = user
	comment.comment_text = comment_text
	comment.rti_query = rti_query
	comment.save()

	all_comments = models.Comment.objects.filter(rti_query = rti_query).order_by('-entry_date')[0:3]
	comment_html = ""
	for comment in all_comments:
		comment_html += get_comment_html(comment).content

	return HttpResponse(comment_html)



