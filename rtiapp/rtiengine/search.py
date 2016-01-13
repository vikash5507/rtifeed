from rtiapp import models
from rtiapp.rtiengine import newsfeed
from rtiapp.views import views_profile
from haystack.query import SearchQuerySet
from rtiapp.common import XOR_KEY

def search_model(sTerm, model_type, search_type):
	search_model = None
	if model_type == 'state':
		search_model = models.State
	elif model_type == 'department':
		search_model = models.Department
	elif model_type == 'topic':
		search_model = models.Tag
	elif model_type == 'blog':
		search_model = models.Blog
	elif model_type == 'user':
		search_model = models.User
	elif model_type == 'rti':
		search_model = models.RTI_query

	print sTerm, model_type, search_type
	if search_type == 'autocomplete':
		search_results = SearchQuerySet().models(search_model).autocomplete(content = sTerm)
	elif search_type == 'search':
		search_results = SearchQuerySet().models(search_model).filter(content = sTerm)

	search_list = []
	mark_list = {}
	search_results = search_results[0:10]
	for r in search_results:
		# print "IDDDD", r.pk
		try:
			s_model = search_model.objects.filter(pk=r.pk).first()
		except:
			continue
		if not s_model.id in mark_list:
			mark_list[s_model.id] = True
			search_context = make_search_context(s_model, model_type)
			search_list.append(search_context)
	return search_list

def make_search_context(s_model, model_type):
	search_context = {}
	
	if model_type == 'state':
		search_context = {
			'tds_name' : s_model.state_name,
			'search_link' : '/state/' + s_model.slug
		}
		state_departments = models.State_department.objects.values('department').filter(state = s_model)
		rti_queries = models.RTI_query.objects.filter(department = state_departments)
		rti_responses = models.RTI_response.objects.filter(rti_query = rti_queries)
		search_context['tds_no_rti_queries'] = len(rti_queries)
		search_context['tds_no_rti_responses'] = len(rti_responses)
		search_context['tds_no_followers'] = len(models.Follow_state.objects.filter(followee = s_model))
	elif model_type == 'department':
		search_context = {
			'tds_name' : s_model.department_name,
			'search_link' : '/department/' + s_model.slug
		}
		rti_queries = models.RTI_query.objects.filter(department = s_model)
		rti_responses = models.RTI_response.objects.filter(rti_query = rti_queries)
		search_context['tds_no_followers'] = len(models.Follow_department.objects.filter(followee = s_model))
		search_context['tds_no_rti_queries'] = len(rti_queries)
		search_context['tds_no_rti_responses'] = len(rti_responses)

	elif model_type == 'topic':
		search_context = {
			'tds_name' : s_model.tag_text,
			'search_link' : '/topic/' + s_model.slug
		}
		rti_queries = models.RTI_tag.objects.values('rti_query').filter(tag = s_model)
		rti_responses = models.RTI_response.objects.filter(rti_query = rti_queries)
		search_context['tds_no_rti_queries'] = len(rti_queries)
		search_context['tds_no_rti_responses'] = len(rti_responses)
		search_context['tds_no_followers'] = len(models.Follow_topic.objects.filter(followee = s_model))

	elif model_type == 'user':
		search_context = {
			'name_user' : s_model.first_name + ' ' + s_model.last_name,
			'search_link' : '/profile/' + s_model.username,
			'search_username' : s_model.username
		}
		user_profile = models.User_profile.objects.filter(user = s_model).first()
		search_context['profile_picture'] = user_profile.profile_picture.url
		search_context['num_followers'] = len(models.Follow_user.objects.filter(followee = s_model))
		search_context['num_following'] = len(models.Follow_user.objects.filter(follower = s_model))

	elif model_type == 'rti':
		
		search_context = {
			'rti_id' : s_model.id,
			'search_link' : '/rti_page/' + s_model.slug + '/',
			}
		if len(s_model.description) < 3:
			search_context['rti_description'] = s_model.query_text[0:50] + "..."
		else:
			search_context['rti_description'] = s_model.description
		meta_data = newsfeed.get_rti_meta_data(s_model)
		search_context['no_likes'] = meta_data['no_likes']
		search_context['no_comments'] = meta_data['no_comments']

	elif model_type == 'blog':
		
		search_context = {
			'blog_id' : s_model.id,
			'search_link' : '/blog/' + s_model.slug,
			}
		search_context['blog_heading'] = s_model.heading
		search_context['blog_picture'] = s_model.blog_picture.url
		meta_data = newsfeed.get_rti_meta_data(s_model)
		
	search_context['model_type'] = model_type
	return search_context