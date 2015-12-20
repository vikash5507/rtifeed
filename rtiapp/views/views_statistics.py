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

@login_required
def statistics(request):
	total_rti_queries = len(models.RTI_query.objects.all())
	total_rti_responses = len(models.RTI_response.objects.all())

	departments = models.Department.objects.filter(department_type = 'centre')

	department_list = []
	for department in departments:
		no_rti_queries = len(models.RTI_query.objects.filter(department = department))
		department_list.append((-no_rti_queries, department))

	department_list.sort()

	top_department_list = department_list[0:5]

	top_dep_context = []
	counter = 1
	for td in top_department_list:
		department = td[1]
		rti_queries = models.RTI_query.objects.filter(department = department)
		rti_responses = models.RTI_response.objects.filter(rti_query = rti_queries)
		response_rate = 0.0
		if len(rti_queries) > 0:
			response_rate = int((100.0 * len(rti_responses)) / len(rti_queries) )
			print "rrrrr", response_rate
		top_dep_context.append({
			's_no' : counter,
			'department_name' : department.department_name,
			'no_rti_queries' : len(rti_queries),
			'no_rti_responses' : len(rti_responses),
			'response_rate' : response_rate,
			'department_url' : '/department/' + str(department.id)
			})
		counter += 1

	states = models.State.objects.all()
	states_context = []
	for state in states:
		state_departments = models.State_department.objects.values('department').filter(state = state)
		rti_queries = models.RTI_query.objects.filter(department = state_departments)
		rti_responses = models.RTI_response.objects.filter(rti_query = rti_queries)

		states_context.append({
			'state_name' : state.state_name,
			'no_rti_queries' : len(rti_queries),
			'no_rti_responses' : len(rti_responses),
			
			})

	context = {
		'total_rti_queries' : total_rti_queries,
		'total_rti_responses' : total_rti_responses,
		'top_dep_context' : top_dep_context,
		'states_context' : states_context
	}

	context['my_profile'] = newsfeed.get_profile_context(request.user)
	return render_to_response('Statistics/statistics.html', context)


