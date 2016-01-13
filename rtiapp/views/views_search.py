from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect, HttpRequest
from django.template import RequestContext
import datetime
from datetime import timedelta,datetime
from django.db import connection
import json
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery
import haystack
from rtiapp.models  import RTI_query,User_profile,RTI_response,Department,State
from django.contrib.auth.models import User
from rtiapp.rtiengine import newsfeed, search
from rtiapp.views import views_profile
from django.contrib.auth.decorators import login_required
# def search_user(request):
# 	sTerm = request.GET['query']
# 	# sTerm = haystack.inputs.Clean(sTerm)
# 	print "sterm", sTerm
# 	result_user = SearchQuerySet().models(User).autocomplete(content = sTerm)
# 	search_list = []
# 	for r in result_user:
# 		user = User.objects.filter(pk=r.pk).first()
# 		user_context = views_profile.make_profile_context(user)
		
# 		user_context['profile_picture'] = '/media/' +  str(user_context['profile_picture'])
# 		user_context['profile_url'] = '/profile/' + user.username
# 		user_context['user_id'] = user.id
# 		user_context['search_type'] = 'user'
# 		print user_context['num_followers'], "dsjhfjkdshfjkdshfjkdshgfkjhsd"
# 		search_list.append(user_context)

# 	print search_list
# 	return HttpResponse(json.dumps(search_list))


# def search_rti(request):
# 	sTerm = request.GET['query']
# 	sTerm = Clean(sTerm)
# 	result_rti = SearchQuerySet().models(RTI_query).filter(content = sTerm).order_by()
	
# 	search_list = []
# 	for r in result_rti:
# 		rti_query = RTI_query.objects.filter(pk=r.pk).first()
# 		rti_context = {
# 			'rti_id' : rti_query.id,
# 			'rti_description' : rti_query.description,
# 			'rti_url' : '/rti_page/' + str(rti_query.id) + '/',
# 			}
# 		meta_data = newsfeed.get_rti_meta_data(rti_query)
# 		rti_context['no_likes'] = meta_data['no_likes']
# 		rti_context['no_comments'] = meta_data['no_comments']
# 		rti_context['search_type'] = 'rti'
# 		search_list.append(rti_context)

# 	return HttpResponse(json.dumps(search_list))

@login_required
def search_model(request):
	sTerm = request.GET['query']
	model_type = request.GET['model_type']
	search_type = request.GET['search_type']
	data_type = request.GET['data_type']
	context = None
	if model_type == 'all':
		
		user_list = search.search_model(sTerm, 'user', search_type)
		rti_list = search.search_model(sTerm, 'rti', search_type)
		state_list = search.search_model(sTerm, 'state', search_type)
		department_list = search.search_model(sTerm, 'department', search_type)
		topic_list = search.search_model(sTerm, 'topic', search_type)
		blog_list = search.search_model(sTerm, 'blog', search_type)
		context = {
			'user_list' : user_list,
			'state_list' : state_list,
			'department_list' : department_list,
			'topic_list' : topic_list,
			'rti_list' : rti_list,
			'blog_list' : blog_list
		}
		print context
	else:
		context = search.search_model(sTerm, model_type, search_type)[0:3]

	if data_type == 'json':
		return HttpResponse(json.dumps(context))
	else:
		return context

@login_required
def search_page(request):
	context = search_model(request)
	print "#########"
	print context
	context['my_profile'] = newsfeed.get_profile_context(request.user)
	
	return render_to_response('search/search_page.html', context)





# def search(request):
	
# 	sTerm = request.GET['query']
	
# 	print sTerm
# 	result_user = SearchQuerySet().models(User).filter(content = sTerm).order_by()
# 	# for r in results:
# 	# 	rti_list.append(models.Relevance.objects.filter(rti_query_id = r.id)[0])

# 	# print rti_list
# 	print result_user
# 	user_list = []
# 	for r in result_user :
# 		user_list.append({
# 			'name_user' : User.objects.filter(pk=r.pk).first().first_name,
# 			}
# 		)

# 	rti_list=[]
# 	result_rti = SearchQuerySet().models(RTI_query).filter(content = sTerm).order_by()
# 	print result_rti
# 	for r in result_rti :
# 		rti_list.append(RTI_query.objects.filter(pk=r.pk).first().id)

# 	result_rti_response = SearchQuerySet().models(RTI_response).filter(content = sTerm).order_by()
# 	rti_response_list = []
# 	for r in result_rti_response :
# 		rti_response_list.append(RTI_response.objects.filter(pk=r.pk).first().id)

# 	result_state = SearchQuerySet().models(State).filter(content = sTerm).order_by()

# 	state_list = []
# 	for r in result_state :
# 		state_list.append(State.objects.filter(pk=r.pk).first().id)
# 	print result_state

# 	Department_result = SearchQuerySet().models(Department).filter(content = sTerm).order_by()
# 	Department_list = []
# 	for r in Department_result :
# 		Department_list.append(Department.objects.filter(pk=r.pk).first().id)
	

# 	results = {'user_list':user_list,
# 				'rti_query_list':rti_list,
# 				'rti_response_list': rti_response_list,
# 				'state_list': state_list,
# 				'Department':Department_list}

# 	print user_list
# 	return HttpResponse(json.dumps(user_list))