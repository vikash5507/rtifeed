from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
import json
from rtiapp.views import views_home
from datetime import datetime, timedelta
from rtiapp.rtiengine import activity_relevance, newsfeed
from django.views.decorators.csrf import csrf_exempt
from django.db.models.signals import post_delete


def share_rti_query(request):
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	states = models.State.objects.all()
	gov_list = [{
		'gov_id' : 0,
		'gov_name' : 'Union Government'
	}]
	for state in states:
		gov_list.append({
			'gov_id' : state.id,
			'gov_name' : state.state_name + ' Government'
			})
	departments = models.Department.objects.filter(department_type = 'centre')
	rti_hash = str(request.user.id) + '####' + str(datetime.now())
	context['rti_hash'] = rti_hash
	context['departments']  = departments
	context['gov_list'] = gov_list
	return render_to_response('ShareRTI/post_rti_query.html', context)

def share_rti_response(request):
	context = {}
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	if 'rti_id' in request.GET:
		rti_query = models.RTI_query.objects.filter(id = request.GET['rti_id']).first()
		
		if len(models.RTI_response.objects.filter(rti_query = rti_query)) > 0:
			return HttpResponseRedirect('/rti_page/' + str(rti_query.id))

		if not rti_query or rti_query.user != request.user:
			raise Http404("Page Not Found")
		context['single_query'] = True
		context['rti_description'] = rti_query.description
		context['rti_id'] = rti_query.id
		rti_hash = str(request.user.id) + '####' + str(datetime.now())
		context['rti_hash'] = rti_hash
		return render_to_response('ShareRTI/post_rti_response.html', context)

	else:
		context['single_query'] = False
		query_list = models.RTI_query.objects.filter(user = request.user, response_status = False).order_by('-entry_date')
		description_list = []
		counter = 1
		for query in query_list:
			description_list.append({
				's_no' : counter,
				'rti_id' : query.id,
				'rti_description' : query.description,
				'filed_date' : query.rti_file_date,
				'department' : query.department.department_name,
				'response_url' : '/share_rti_response?rti_id=' + str(query.id),
				'query_url' : '/rti_page/' + str(query.id)
				})
			counter += 1
		context['rti_description_list'] = description_list

		return render_to_response('ShareRTI/rti_response_list.html', context)
	
	
	


def get_departments_of(request):
	gov_id = request.GET['gov_id']
	if int(gov_id) == 0:
		departments = models.Department.objects.filter(department_type = 'centre')
	else:
		state = models.State.objects.filter(id = request.GET['gov_id']).first()
		departments = models.State_department.objects.filter(state = state)
		dep_list = []
		for dep in departments:
			dep_list.append(dep.department)
		departments = dep_list
	context= {
		'departments' : departments
	}

	
	return render_to_response('ShareRTI/departments.html', context);

def get_rti_tag(request):
	tags=models.Tag.objects.all()
	tag_content=[]
	for t in tags:
		tag_content.append({
			'tag_name':t.tag_text
			})
	return HttpResponse(json.dumps(tag_content))

@csrf_exempt
def post_rti_query(request):

	if request.method == "POST":
		
		user = request.user
		rti_hash = request.POST['rti_hash']
		
		query = request.POST['query_text']
		print query
		# return HttpResponse('done')

		description= request.POST['description']
		authority_name=request.POST['authority_name']
		dept_id=request.POST['dept_id']
		rti_file_date=request.POST['rti_date']
		

		authority = models.Authority.objects.filter(authority_name = authority_name).first()
		if not authority:
			authority = models.Authority()
			authority.authority_name = authority_name
			authority.department_id = dept_id
			authority.save()

		rti_query=models.RTI_query()
		
		rti_query.user = user
		rti_query.query_text = str(query)
		rti_query.description = description
		
		if not rti_file_date or rti_file_date == "":
			rti_query.rti_file_date = datetime.now()
		else:	
			rti_query.rti_file_date=rti_file_date

		rti_query.entry_date = datetime.now()
		rti_query.response_status = 0
		
		if int(request.POST['govt_id']) == 0:
			rti_query.query_type = 'centre'
		else:
			rti_query.query_type = 'state'
		
		rti_query.authority = authority
		rti_query.department_id = dept_id
		rti_query.save()

		tags = json.loads(request.POST['tags'])
		for tag in tags:
			print tag
			tag_model = models.Tag.objects.filter(tag_text = tag).first()
			if not tag_model:
				tag_model = models.Tag()
				tag_model.tag_text = tag
				tag_model.save()
			# print "check1"
			rti_tag = models.RTI_tag()
			rti_tag.rti_query = rti_query
			rti_tag.tag = tag_model
			rti_tag.save()

		rti_images = models.RTI_unlinked_files.objects.filter(user = user, rti_hash = rti_hash)
		for rti_image in rti_images:
			rti_file = models.RTI_query_file()
			rti_file.rti_query = rti_query
			rti_file.query_picture = rti_image.query_picture
			rti_file.save()
			rti_image.linked = True
			rti_image.save()

		
		activity = models.Activity()
		activity.rti_query = rti_query
		activity.user = user
		activity.activity_type = 'rti_query'
		activity.save()

		activity_relevance.update_activity_relevance(activity)

		context = {
			'rti_id' : json.dumps(rti_query.id)
		}

		return HttpResponse(json.dumps(context))

@csrf_exempt
def post_rti_response(request):
	if request.method == 'POST':
		user = request.user
		rti_query_id = request.POST['rti_query_id']
		rti_hash = request.POST['rti_hash']
		rti_query = models.RTI_query.objects.filter(id = rti_query_id).first()
		if not rti_query or (rti_query.user != request.user):
			return HttpResponse('Invalid Query')
		rti_response = models.RTI_response()
		rti_response.rti_query = rti_query
		rti_response.response_text = request.POST['response_text']
		rti_response.rti_response_date = request.POST['rti_response_date']
		rti_response.entry_date = datetime.now()
		rti_response.save()
		rti_query.response_status = True
		rti_query.save()
		print "HASh", rti_hash
		rti_images = models.RTI_unlinked_files.objects.filter(user = user, rti_hash = rti_hash)
		for rti_image in rti_images:
			rti_file = models.RTI_response_file()
			rti_file.rti_response = rti_response
			rti_file.response_picture = rti_image.query_picture
			rti_file.save()
			rti_image.linked = True
			rti_image.save()

		
		
		activity = models.Activity()
		activity.rti_query = rti_query
		activity.user = user
		activity.activity_type = 'rti_response'
		activity.save()

		activity_relevance.update_activity_relevance(activity)

		context = {
			'rti_id' : json.dumps(rti_query.id)
		}

		return HttpResponse(json.dumps(context))


def edit_rti_query(request, rti_id):
	rti_query = models.RTI_query.objects.filter(id = rti_id).first()
	if not rti_query:
		raise Http404("Page Not Found")
	if not (rti_query.user == request.user):
		raise Http404("Page Not Found")

	context = newsfeed.make_rti_context(rti_query)
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	states = models.State.objects.all()
	gov_list = [{
		'gov_id' : 0,
		'gov_name' : 'Union Government'
	}]
	for state in states:
		gov_list.append({
			'gov_id' : state.id,
			'gov_name' : state.state_name + ' Government'
			})
	departments = models.Department.objects.filter(department_type = 'centre')
	rti_hash = str(request.user.id) + '####' + str(datetime.now())
	context['rti_hash'] = rti_hash
	context['departments']  = departments
	context['gov_list'] = gov_list
	return render_to_response('ShareRTI/edit_rti_query.html', context)
	

@csrf_exempt
def submit_rti_photos(request):
	rti_hash = request.POST['rti_hash']
	

	models.RTI_unlinked_files.objects.filter(user = request.user).exclude(rti_hash = rti_hash).delete()
	for f in request.FILES:
		
		unliked_photo = models.RTI_unlinked_files()
		unliked_photo.user = request.user
		unliked_photo.rti_hash = rti_hash
		unliked_photo.query_picture = request.FILES[f]
		unliked_photo.save()

	
	return HttpResponseRedirect('/share_rti_query')

@csrf_exempt
def delete_rti(request):
	rti_id = request.POST['rti_id']
	models.RTI_query.objects.filter(id = rti_id, user = request.user).delete()
	return HttpResponse('done')


