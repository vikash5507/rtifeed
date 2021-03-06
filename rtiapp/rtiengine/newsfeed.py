from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
from rtiapp.rtiengine import relevance, notification
import json


def get_profile_context(user):
	if user.is_anonymous():
		return {
			'no_user' : True
		}
	user_profile = models.User_profile.objects.filter(user = user).first()
	
	if not user_profile:
		return {
			'no_user' : True
		}

	context = {
		'uid' : user.id,
		'name_user': user.first_name + " " + user.last_name,
		'profile_picture' : user_profile.profile_picture,
		'profile_url' : '/profile/'+user.username+'/',
		'username' : user.username,
		'user_profile_link' : '/profile/' + user.username,
		'bio_description' : user_profile.bio_description,
		'num_followers' : len(models.Follow_user.objects.filter(followee = user)),
		'num_rtis' : len(models.RTI_query.objects.filter(user = user)),
		'num_blogs' : len(models.Blog.objects.filter(user = user)),
		# 'num_new_messages' : len(models.Message.objects.filter(receiver = user, read_status = False))
	}
	return context


def make_head_line(activity, user):
	head_line = ""
	# if activity.user == user:
	# 	return head_line
	name_user = activity.user.first_name + " " + activity.user.last_name + " "
	name_link = '<a href = "/profile/' + activity.user.username + '">' + name_user + '</a> '
	head_line += name_link
	if activity.activity_type == 'rti_query' and (not activity.rti_query.proposed):
		head_line += 'posted an RTI query'
	elif activity.activity_type == 'rti_query' and activity.rti_query.proposed:
		head_line += 'proposed an RTI'
	
	elif activity.activity_type == 'rti_response':
		head_line += 'posted an RTI response'
	
	elif activity.activity_type == 'like':
		head_line += 'liked this'
	
	elif activity.activity_type == 'follow' and (not activity.rti_query.proposed):
		head_line += 'followed this'

	elif activity.activity_type == 'follow' and activity.rti_query.proposed:
		head_line += 'wants an answer for this'
		
	elif activity.activity_type == 'comment':
		head_line += 'commented on this'

	return head_line
	
def get_feed_for_rtis(rti_list, user):
	html_string = ""
	rti_id_list = []
	for rti in rti_list:
		rti_html = get_feed_for_rti(rti['rti_query'], user, rti['rti_head_line'])
		html_string += rti_html.content
		rti_id_list.append(rti['rti_query'].id)
	
	context = {
		'feed_html' : html_string,
		'rti_id_list' : rti_id_list
	}
	
	return HttpResponse(json.dumps(context))

def make_rti_context(rti_query):
	
	context = {
		'rti_id' : rti_query.id,
		'rti_query_text' : rti_query.query_text,
		'rti_description' : rti_query.description,
		'rti_file_date' : rti_query.rti_file_date,
		'rti_query_type' : rti_query.query_type,
		'rti_response_status' : rti_query.response_status,
		'rti_department_id' : rti_query.department,
		'rti_authority' : rti_query.authority,
		'rti_query_type' : rti_query.query_type,

	}
	# rti_dept = models.Department.objects.filter(department_name = rti_query.department).first()
	# context['rti_department'] = rti_dept.department_name
	# context['government'] = rti_dept.department_type
	rti_tag = models.RTI_tag.objects.filter(rti_query = rti_query).first()
	# tag_text_list = models.Tag.objects.filter(id = 6)
	# tag_list = [{}]
	# for text in tag_text_list:
	# 	tag_list.append({
	# 		'tag_val' : rti_tag.tag
	# 		})
	context['tag_list'] = rti_tag.tag
	image_list = models.RTI_query_file.objects.filter(rti_query = rti_query).first()
	rti_image = image_list.query_picture
	context['rti_image'] = rti_image
	return context


def get_feed_for_rti(rti, user, head_line = '', comment_strategy = 'time', max_comments = 2):
	
	profile = models.User_profile.objects.filter(user = rti.user).first()
	
	if user.is_anonymous():
		user = models.User()
		user_profile = models.User_profile()
		user_profile.user = user
	else:
		user_profile = models.User_profile.objects.filter(user = user).first()

	# print user_profile
	# rti_photo = models.RTI_query_file.objects.filter(rti_query = rti).first()
	rti_context = {
		'my_rti' : user == rti.user,
		'name_user' : user.first_name + " " + user.last_name,
		'user_pic' : user_profile.profile_picture,
		'rti_id' : rti.id,
		'rti_url' : '/rti_page/' + rti.slug,
		'rti_user' : rti.user.first_name + " " + rti.user.last_name,
		'rti_user_url' : '/profile/'+ rti.user.username+'/',
		'rti_query_text' : rti.query_text,
		'rti_description' : rti.description,
		'rti_file_date' : rti.rti_file_date,
		'rti_entry_date' : rti.entry_date,
		'rti_query_type' : rti.query_type,
		'rti_response_status' : rti.response_status,
		'rti_department' : rti.department.department_name,
		'rti_department_url' : '/department/' + rti.department.slug,
		'rti_proposed' : rti.proposed,
		'rti_head_line' : head_line,
		'rti_query_images' : [],
		'rti_response_images' : [],
		'rti_query_files' : [],
		'rti_response_files' : [],
		'rti_slug' : rti.slug
	}
	
	if rti.department.department_type == 'state':
		# sd = models.State_department.objects.filter(department = rti.department).first()
		st = rti.department.state
		rti_context['rti_state'] = st.state_name
		rti_context['rti_state_url'] = '/state/' + st.slug
	
	rti_query_images =  models.RTI_query_file.objects.filter(rti_query = rti)

	for r_image in rti_query_images:
		if r_image.query_picture and r_image.extension() != '.pdf':
			rti_context['rti_query_images'].append({
				'image_url' : r_image.query_picture.url
				})
		else:
			rti_context['rti_query_files'].append({
				'pdf_url' : r_image.query_picture.url
				})
	
	total_query_photos = len(rti_context['rti_query_images'])
	
	if total_query_photos == 1:
		rti_context['qp_container_class'] = 'col-md-offset-4 col-md-8'
		
	elif total_query_photos == 2:
		rti_context['qp_container_class'] = 'col-md-offset-2 col-md-10'
	else:
		rti_context['qp_container_class'] = 'col-md-12'

	if profile:
		rti_context['rti_user_pic'] = profile.profile_picture
	
	
	if rti.response_status:
		response = models.RTI_response.objects.filter(rti_query = rti).first()
		if response:
			rti_context['response_text'] = response.response_text
			
			rti_context['response_file_date'] = response.rti_response_date
			rti_context['response_entry_date'] = response.entry_date

		rti_response_images =  models.RTI_response_file.objects.filter(rti_response = response)

		for r_image in rti_response_images:
			if r_image.response_picture and r_image.extension() != '.pdf':
				rti_context['rti_response_images'].append({
					'image_url' : r_image.response_picture.url
					})
			else:
				rti_context['rti_response_files'].append({
					'pdf_url' : r_image.response_picture.url
					})


		total_response = len(rti_context['rti_response_images'])
	
		if total_response == 1:
			rti_context['rp_container_class'] = 'col-md-offset-4 col-md-8'
			
		elif total_response == 2:
			rti_context['rp_container_class'] = 'col-md-offset-2 col-md-10'
		else:
			rti_context['rp_container_class'] = 'col-md-12'

	comments = models.Activity.objects.filter(rti_query = rti, activity_type = 'comment').order_by('-entry_date')
	likes = models.Activity.objects.filter(rti_query = rti, activity_type = 'like').order_by('-entry_date')
	follows = models.Activity.objects.filter(rti_query = rti, activity_type = 'follow').order_by('-entry_date')

	rti_context['no_comments'] = len(comments)
	rti_context['no_likes'] = len(likes)
	rti_context['no_follows'] = len(follows)
	
	if comment_strategy == 'time':
		rti_context['top_comments'] = comments[0: max_comments]
		rti_context['top_comments'].reverse()
	
	if len(comments) > max_comments:
		rti_context['more_comments'] = len(comments) - max_comments
	comment_html = ""
	for comment in rti_context['top_comments']:
		comment_html += get_comment_html(comment, user).content

	like_status = len(models.Activity.objects.filter(user = user, rti_query = rti, activity_type = 'like')) > 0
	follow_status = len(models.Activity.objects.filter(user = user, rti_query = rti, activity_type = 'follow')) > 0
	spam_status = len(models.Activity.objects.filter(user = user, rti_query = rti, activity_type = 'spam')) > 0
	rti_context['like_status'] = like_status
	rti_context['follow_status'] = follow_status
	rti_context['spam_status'] = spam_status
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
		'comment_text' : json.loads(comment.meta_data)['comment_text'],
		'comment_user_id' : comment.user.id,
		'comment_user_url' : '/profile/'+ comment.user.username+'/',
		'comment_user_pic' : profile.profile_picture,
		'comment_name_user' : comment.user.first_name + " " + comment.user.last_name,
		'comment_date' : comment.entry_date,
		'comment_no_likes' : len(models.Activity.objects.filter(activity_link = comment, activity_type = 'comment_like')),
		'my_comment' : comment.user == user,
		'comment_like_status' : (len(models.Activity.objects.filter(activity_link = comment, activity_type = 'comment_like', user = user)) > 0),
	}
	return render_to_response('Home/comment.html', context)


def get_rti_meta_data(rti):
	rti_context = {}
	comments = models.Activity.objects.filter(rti_query = rti, activity_type = 'comment').order_by('-entry_date')
	likes = models.Activity.objects.filter(rti_query = rti, activity_type = 'like').order_by('-entry_date')
	follows = models.Activity.objects.filter(rti_query = rti, activity_type = 'follow').order_by('-entry_date')

	rti_context['no_comments'] = len(comments)
	rti_context['no_likes'] = len(likes)
	rti_context['no_follows'] = len(follows)

	return rti_context

# def get_trending_data(user):
# 	users = models.User.objects.all()
# 	follower_list = []
# 	for user in users:
# 		no_followers = len(models.Follow_user.objects.filter(followee = user))
# 		follower_list.append((-no_followers, no_followers, get_profile_context(user)))
# 	follower_list.sort()
# 	follower_list[-]
# 	topics = models.Tag.objects.all()


