import json
import pprint
from rtiapp import models
from datetime import datetime
import warnings
from rtiapp.rtiengine import activity_relevance as ar
import os

warnings.filterwarnings("ignore")

def save_rtis():
	file_path = os.path.join(os.path.dirname(__file__), 'delhi_data_new.json')
	json_file = open(file_path, 'r')
	dep_rtis = json.loads(json_file.read())
	
	c = 0

	user = models.User.objects.filter(first_name = 'rtist').first()
	state = models.State.objects.filter(state_name = "Delhi").first()
	if not state:
		state = models.State()
		state.state_name = "Delhi"
		state.save()

	print state
	map_rtis = {}
	dup = 0
	for dep in dep_rtis:
		if len(dep_rtis[dep]) == 0:
			continue
		rtis = dep_rtis[dep]
		state_department = models.State_department.objects.filter(state__state_name = 'Delhi', department__department_name = dep).first()
		if state_department:
			department = state_department.department
		else:
			department = models.Department()
			department.department_name = dep
			department.department_type = 'state'
			department.save()

			state_department = models.State_department()
			state_department.department = department
			
			state_department.state = state
			state_department.save()
		# print state_department
		# return
		d = 0
		for rti in rtis:
			# print rti
			if rti['url'] in map_rtis:
				dup += 1
				continue
			if (not rti['query']) or (not rti['response']) or (not rti['url']):
				continue
			map_rtis[ rti['url'] ] = True
			rti_query = models.RTI_query()
			rti_query.user = user
			rti_query.query_text = rti['query']
			rti_url = '<br><a href = "'+ rti['url'] +'">'+ rti['url'] +'</a>'
			rti_query.query_text = rti_query.query_text + rti_url
			# if not rti['query']:
				# print rti
			if not rti['query']:
				continue
			if not rti['response']:
				continue
			if len(rti['query']) <= 20 or len(rti['response']) <= 20:
				continue
			# print rti
			# break
			rti_query.description = ""
			
			rti_query.department = department
			rti_query.entry_date = datetime.now()
			try:
				rti_query.save()
				pass
			except:
				print "err qu"
				continue
			tag = models.Tag.objects.filter(tag_text = rti['category']).first()
			if not tag:
				tag = models.Tag()
				tag.tag_text = rti['category']
				tag.save()

			rti_tag = models.RTI_tag()
			rti_tag.rti_query = rti_query
			rti_tag.tag = tag
			try:
				rti_tag.save()
				pass
			except:
				print "err tg"
				continue

			rti_response = models.RTI_response()
			rti_response.rti_query = rti_query
			rti_response.response_text = rti['response']
			# print rti['response']
			rti_response.entry_date = datetime.now()
			try:
				rti_response.save()
				pass
			except:
				print "err rs"
				continue
			rti_query.response_status = True
			rti_query.save()

			activity = models.Activity()
			activity.activity_type = 'rti_query'
			activity.rti_query = rti_query
			activity.user = user
			activity.save()
			ar.update_activity_relevance(activity)
			# print c
			c += 1
			d += 1
		print d
	print c, dup
	# pprint.pprint(dep_rtis)
