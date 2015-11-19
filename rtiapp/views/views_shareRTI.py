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
from rtiapp.rtiengine import relevance
from django.views.decorators.csrf import csrf_exempt

def share_rti_query(request):
	context = {}
	context['my_profile'] = views_home.get_profile_context(request.user)
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
	print "dep", departments
	context['departments']  = departments
	context['gov_list'] = gov_list
	return render_to_response('ShareRTI/post_rti_query.html', context)

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


@csrf_exempt
def post_rti_query(request):

	if request.method == "POST":
		
		user = request.user
		rti_number = request.POST['rti_no']
		query= request.POST['query_text']
		description= request.POST['description']
		authority=request.POST['authority_name']
		dept_id=request.POST['dept_id']
		rti_file_date=request.POST['rti_date']
		
		rti_query=models.RTI_query()
		rti_query.user = user
		rti_query.rti_number = rti_number	
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
		
		rti_query.department_id = dept_id
		rti_query.save()

		if ('photo' in request.FILES) and request.FILES['photo']:
			support_document = models.RTI_query_file()
			support_document.query_picture = request.FILES['photo']
			support_document.rti_query = rti_query
			support_document.save()
			print "doc saved"
		
		activity = models.Activity()
		activity.rti_query = rti_query
		activity.user = user
		activity.activity_type = 'rti_query'
		activity.save()

		return HttpResponse('done')