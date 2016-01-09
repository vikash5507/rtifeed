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
from django.db.models import Q

@login_required
def messenger_page(request):
	contacts = find_contacts(request.user)
	context = {
		'my_profile' : newsfeed.get_profile_context(request.user),
		'contacts' : contacts,
	}
	return render_to_response('Messenger/messenger_page.html', context)

def private_chat(request, username):
	user = request.user
	other_user = models.User.objects.filter(username = username).first()
	print user, other_user
	

	contacts = find_contacts(request.user)
	context = {
		'my_profile' : newsfeed.get_profile_context(request.user),
		'contacts' : contacts,
		'other_username' : username,
		'other_user_name' : other_user.first_name + " " + other_user.last_name
	}

	return render_to_response('Messenger/messenger_page.html', context)

@login_required
def send_message(request, username):
	user = request.user
	other_user = models.User.objects.filter(username = username).first()
	message_text = request.GET['message_text']

	msg = models.Message()
	msg.sender = user
	msg.receiver = other_user
	msg.message_text = message_text
	msg.save()

	new_messages = render_to_response('Messenger/message_right.html', make_message_context(msg)).content
	context = {
		'new_messages' : new_messages
	}
	return HttpResponse(json.dumps(context))

@login_required
def fetch_messages(request, username):
	user = request.user
	other_user = models.User.objects.filter(username = username).first()
	new_last_fetched_index = None
	if 'unread' in request.GET:
		messages = models.Message.objects.filter(receiver = request.user, sender = other_user, read_status = False).order_by('message_date')
	else:
		last_fetched_index = None
		if 'last_fetched_index' in request.GET:
			last_fetched_index = request.GET['last_fetched_index']
		messages = models.Message.objects.filter(Q(Q(sender = user) & Q(receiver = other_user)) | 
		Q(Q(sender = other_user) & Q(receiver = user))).order_by('-message_date')
		
		if last_fetched_index:
			messages = messages.filter(id__lt = int(last_fetched_index))
		
		messages = messages[0:10]

		
		if len(messages) > 0 and messages[len(messages) - 1]:
			new_last_fetched_index = messages[len(messages) - 1].id
		
		messages = list(messages)
		messages.reverse()
	
	message_list_html = ""
	for message in messages:
		if message.sender == user:
			message_list_html += render_to_response('Messenger/message_right.html', make_message_context(message)).content
		else:
			message_list_html += render_to_response('Messenger/message_left.html', make_message_context(message)).content
		message.read_status = True
		message.save()

	context = {
		'message_list_html' : message_list_html,
		'last_fetched_index' : new_last_fetched_index
	}

	return HttpResponse(json.dumps(context))


def make_message_context(message):
	sender_profile = models.User_profile.objects.filter(user = message.sender).first()
	context = {
		'message_sender' : message.sender.first_name + " " + message.sender.last_name,
		'message_time' 	 : message.message_date,
		'message_photo'	 : '/media/' + str(sender_profile.profile_picture),
		'message_text'	 : message.message_text,
	}
	return context


def find_contacts(user):
	contacts = []
	messages = models.Message.objects.filter(Q(sender = user) | Q(receiver= user)).order_by('-message_date')
	contact_users = []
	contact_messages = []
	for message in messages:
		other_user = message.sender
		if other_user == user:
			other_user = message.receiver
		if other_user in contact_users:
			continue
		contact_users.append(other_user)
		contact_messages.append(message)
	
	contacts_context = []
	for contact_message in contact_messages:
		contacts_context.append(make_contact_context(contact_message, user))
	
	return contacts_context

def make_contact_context(message, user):
	other_user = message.sender
	if other_user == user:
		other_user = message.receiver

	other_user_profile = models.User_profile.objects.filter(user = other_user).first()
	context = {
		'contact_name' : other_user.first_name + " " + other_user.last_name,
		'contact_url' : '/messages/' + other_user.username,
		'contact_message_text' : message.message_text[0:20] + '....',
		'contact_message_date' : message.message_date,
		'contact_photo' : '/media/' + str(other_user_profile.profile_picture)
	}
	return context
