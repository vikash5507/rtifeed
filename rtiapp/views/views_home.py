from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
from rtiapp.rtiengine import relevance
import json

@login_required
def home_page(request):
	user = request.user
	

	context = {}
	context['my_profile'] = get_profile_context(user)
	context['full_feed'] = True
	return render_to_response('Home/home.html', context)

def rti_page(request):
	user = request.user
	context = {}
	context['my_profile'] = get_profile_context(user)
	context['rti_query_id'] = request.GET['rti_query_id']
	context['full_feed'] = False
	return render_to_response('Home/home.html', context)

def get_profile_context(user):
	user_profile = models.User_profile.objects.filter(user = user).first()
	context = {
		'uid' : user.id,
		'name_user': user.first_name + " " + user.last_name,
		'profile_picture' : user_profile.profile_picture,
		'profile_url' : '/profile/'+user.username+'/',
		'username' : user.username,
		'user_profile_link' : '/profile/' + user.username
	}
	return context

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

	return get_feed_for_rtis(rti_list, user)

def get_feed_for_rtis(rti_list, user):
	html_string = ""
	for rti in rti_list:
		rti_html = get_feed_for_rti(rti, user)
		html_string += rti_html.content
	return HttpResponse(html_string)


def view_rti(request):
	user = request.user
	if not user:
		return
	rti = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()
	if rti:
		return get_feed_for_rti(rti, user)
	else:
		return HttpResponse("404")


def get_feed_for_rti(rti, user, comment_strategy = 'time', max_comments = 2):
	profile = models.User_profile.objects.filter(user = rti.user).first()
	user_profile = models.User_profile.objects.filter(user = user).first()
	# rti_photo = models.RTI_query_file.objects.filter(rti_query = rti).first()
	rti_context = {
		'my_rti' : user == rti.user,
		'name_user' : user.first_name + " " + user.last_name,
		'user_pic' : user_profile.profile_picture,
		'rti_id' : rti.id,
		'rti_url' : '/rti_page?rti_query_id=' + str(rti.id),
		'rti_user' : rti.user.first_name + " " + rti.user.last_name,
		'rti_user_url' : '/profile/'+ rti.user.username+'/',
		'rti_query_text' : rti.query_text,
		'rti_rti_number' : rti.rti_number,
		'rti_description' : rti.description,
		'rti_file_date' : rti.rti_file_date,
		'rti_entry_date' : rti.entry_date,
		'rti_query_type' : rti.query_type,
		'rti_response_status' : rti.response_status,
		
	}
	
	if models.RTI_query_file.objects.filter(rti_query = rti).first():
		rti_context['rti_photo'] = models.RTI_query_file.objects.filter(rti_query = rti).first().query_picture
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
	
	if comment_strategy == 'time':
		rti_context['top_comments'] = comments[0: max_comments]
		rti_context['top_comments'].reverse()
	
	if len(comments) > max_comments:
		rti_context['more_comments'] = len(comments) - max_comments
	comment_html = ""
	for comment in rti_context['top_comments']:
		comment_html += get_comment_html(comment, user).content

	like_status = len(models.Like.objects.filter(user = user, rti_query = rti)) > 0
	follow_status = len(models.Follow_query.objects.filter(user = user, rti_query = rti)) > 0

	rti_context['like_status'] = like_status
	rti_context['follow_status'] = follow_status
	rti_context['comment_html'] = comment_html
	rti_context['my_profile'] = get_profile_context(user)
	rti_html = render_to_response('Home/feedbox.html', rti_context)

	relevance = models.Relevance.objects.filter(user = user, rti_query = rti).first()
	if relevance:
		relevance.views += 1
		relevance.save()
	return rti_html

def get_comment_html(comment, user):
	profile = models.User_profile.objects.filter(user = comment.user).first()
	context = {
		'rti_id' : comment.rti_query.id,
		'comment_id' : comment.id,
		'comment_text' : comment.comment_text,
		'comment_user_id' : comment.user.id,
		'comment_user_url' : '/profile/'+ comment.user.username+'/',
		'comment_user_pic' : profile.profile_picture,
		'comment_name_user' : comment.user.first_name + " " + comment.user.last_name,
		'comment_date' : comment.entry_date,
		'my_comment' : comment.user == user,
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

	top_comments = [comment]
	# top_comments.reverse()

	print top_comments
	comment_html = ""
	for comment in top_comments[::-1]:
		print comment.comment_text
		comment_html += get_comment_html(comment, user).content

	comments = models.Comment.objects.filter(rti_query = rti_query )
	likes = models.Like.objects.filter(rti_query = rti_query )
	shares = models.Share.objects.filter(rti_query = rti_query )


	context = {
		'comment_html' : comment_html,
		'no_comments' : len(comments),
		'no_likes' : len(likes),
		'no_shares' : len(shares)
	}
	relevance.update_relevance_for_rti(rti_query)
	return HttpResponse(json.dumps(context))

@login_required
def post_edit_comment(request):
	user = request.user
	comment = models.Comment.objects.filter(id = request.GET['comment_id']).first()
	if comment and comment.rti_query.user == user:
		comment.comment_text = request.GET['comment_text']
		comment.save()
	return HttpResponse('done')

@login_required
def post_delete_comment(request):
	user = request.user
	comment = models.Comment.objects.filter(id = request.GET['comment_id']).first()
	if comment.user == user:
		comment.delete()
		

	rti_query = comment.rti_query
	comments = models.Comment.objects.filter(rti_query = rti_query )
	likes = models.Like.objects.filter(rti_query = rti_query )
	shares = models.Share.objects.filter(rti_query = rti_query )

	context = {
		'no_comments' : len(comments),
		'no_likes' : len(likes),
		'no_shares' : len(shares)
	}
	relevance.update_relevance_for_rti(rti_query)
	return HttpResponse(json.dumps(context))

@login_required
def post_like(request):
	user = request.user
	rti_query = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()
	models.Like.objects.filter(user = user, rti_query = rti_query).delete()
	like = models.Like()
	like.user = user
	like.rti_query = rti_query
	like.save()

	comments = models.Comment.objects.filter(rti_query = rti_query )
	likes = models.Like.objects.filter(rti_query = rti_query )
	shares = models.Share.objects.filter(rti_query = rti_query )

	context = {
		'no_comments' : len(comments),
		'no_likes' : len(likes),
		'no_shares' : len(shares)
	}
	relevance.update_relevance_for_rti(rti_query)
	return HttpResponse(json.dumps(context))


@login_required
def post_unlike(request):
	user = request.user
	rti_query = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()
	
	models.Like.objects.filter(user = user, rti_query = rti_query).delete()

	comments = models.Comment.objects.filter(rti_query = rti_query )
	likes = models.Like.objects.filter(rti_query = rti_query )
	shares = models.Share.objects.filter(rti_query = rti_query )

	context = {
		'no_comments' : len(comments),
		'no_likes' : len(likes),
		'no_shares' : len(shares)
	}
	relevance.update_relevance_for_rti(rti_query)
	return HttpResponse(json.dumps(context))

@login_required
def post_follow_query(request):
	user = request.user
	rti_query = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()
	models.Follow_query.objects.filter(user = user, rti_query = rti_query).delete()
	
	follow = models.Follow_query()
	follow.user = user
	follow.rti_query = rti_query
	follow.save()

	comments = models.Comment.objects.filter(rti_query = rti_query )
	likes = models.Like.objects.filter(rti_query = rti_query )
	shares = models.Share.objects.filter(rti_query = rti_query )

	context = {
		'no_comments' : len(comments),
		'no_likes' : len(likes),
		'no_shares' : len(shares)
	}
	relevance.update_relevance_for_rti(rti_query)
	return HttpResponse(json.dumps(context))

@login_required
def post_unfollow_query(request):
	user = request.user
	rti_query = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()
	
	models.Follow_query.objects.filter(user = user, rti_query = rti_query).delete()

	comments = models.Comment.objects.filter(rti_query = rti_query )
	likes = models.Like.objects.filter(rti_query = rti_query )
	shares = models.Share.objects.filter(rti_query = rti_query )

	context = {
		'no_comments' : len(comments),
		'no_likes' : len(likes),
		'no_shares' : len(shares)
	}

	relevance.update_relevance_for_rti(rti_query)
	return HttpResponse(json.dumps(context))

def load_prev_comments(request):
	user = request.user
	rti_query = models.RTI_query.objects.filter(id = request.GET['rti_query_id']).first()
	comments = models.Comment.objects.filter(rti_query = rti_query).order_by('entry_date')
	comment_html = ""
	for comment in comments:
		comment_html += get_comment_html(comment, user).content
	context = {
		comment_html : comment_html
	}

	return HttpResponse(context)


