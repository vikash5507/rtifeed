from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth.decorators import login_required
from rtiapp import models
import json
import views_home
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
	departments = models.Central_department.objects.all()
	context['departments']  = departments
	context['gov_list'] = gov_list
	return render_to_response('ShareRTI/post_rti_query.html', context)

def get_departments_of(request):
	gov_id = request.GET['gov_id']
	if int(gov_id) == 0:
		departments = models.Central_department.objects.all()
	else:
		state = models.State.objects.filter(id = request.GET['gov_id']).first()
		departments = models.State_department.objects.filter(state = state)
	context= {
		'departments' : departments
	}

	
	return render_to_response('ShareRTI/departments.html', context);


@csrf_exempt
def post_rti_query(request):
	if request.method == "POST":
		
		user = request.user
		
		print request.FILES
		# return HttpResponse("dhslfhkj")
		
		rti_number = request.POST['rti_no']
		query= request.POST['query_text']
		description= request.POST['description']
		authority=request.POST['authority_name']
		dept_id=request.POST['dept_id']
		rti_file_date=request.POST['rti_date']
		
		print rti_number
		print "OK"
		

		response_status = 0
		# print user.id, query, authority, rti_file_date


		rti_query=models.RTI_query()

		rti_query.user = user
		# rti_query.department_id = dept_id
		rti_query.rti_number = rti_number	
		# rti_query.authority=authority
		rti_query.query_text = str(query)
		print query
		rti_query.description = description
		if not rti_file_date or rti_file_date == "":
			rti_query.rti_file_date = datetime.now()
		else:	
			rti_query.rti_file_date=rti_file_date

		rti_query.entry_date = datetime.now()

		rti_query.response_status=response_status

		rti_query.save()
		print "query saved"

		if int(request.POST['govt_id']) == 0:
			rti_query.query_type = 'centre'
			rti_query.save()
			central_query = models.Central_RTI_query()
			central_query.rti_query = rti_query
			central_query.department_id = dept_id
			central_query.save()
			print "centre query saved"
		else:
			rti_query.query_type = 'state'
			rti_query.save()
			state_query = models.State_RTI_query()
			state_query.rti_query = rti_query
			state_query.department_id = dept_id
			state_query.save()


		# # print form
		if ('photo' in request.FILES) and request.FILES['photo']:
			support_document = models.RTI_query_file()
			support_document.query_picture = request.FILES['photo']
			support_document.rti_query = rti_query
			support_document.save()
			print "doc saved"
		
		relevance.make_relevance_for_rti(rti_query)
		# if request.POST['govt_id'] == 1:
		# 	cenral

		# # im = Image.open(rti_query.supporting_document)
		# print "CHECKKKKKK"
		# # print rti_query.supporting_document.url
		# # size = im.size
		# # im.thumbnail(size, Image.ANTIALIAS)
		# # im.save('compressed'+str(rti_query.id), 'JPG', progressive = 1, optimize = 1, quality = 80)
		# rti_query.save()
		# relevance.make_relevance_for_rti(rti_query)
		# return HttpResponse(rti_query.id)
		return HttpResponse('done')