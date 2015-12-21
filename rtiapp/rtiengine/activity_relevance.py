from rtiapp import models
from datetime import timedelta,datetime
import math

def calc_relevance(user, activity):
	rti_query = activity.rti_query
	activity_user = activity.user
	rti_tags  = models.RTI_tag.objects.filter(rti_query = rti_query)
	rti_department = rti_query.department


	user_tags = models.Follow_topic.objects.filter(follower = user)
	user_tag_list = []
	for tag in user_tags:
		user_tag_list.append(tag.followee)
	
	user_departments = models.Follow_department.objects.filter(follower = user)
	user_department_list = []
	for dept in user_departments:
		user_department_list.append(dept.followee)

	fact_user_follow = len(models.Follow_user.objects.filter(follower = user, followee = activity_user))
	fact_rti_follow = len(models.Activity.objects.filter(user = user, rti_query = rti_query, activity_type = 'follow'))
	
	fact_tag = 0
	for tag in rti_tags:
		if tag in user_tags:
			fact_tag += 1

	fact_department = 0
	if rti_department in user_departments:
		fact_department = 1

	comments = len(models.Activity.objects.filter(rti_query = rti_query, activity_type = 'comment').order_by('-entry_date'))
	likes = len(models.Activity.objects.filter(rti_query = rti_query, activity_type = 'like').order_by('-entry_date'))
	shares = len(models.Activity.objects.filter(rti_query = rti_query, activity_type = 'share').order_by('-entry_date'))

	fact_popularity = comments + likes + shares

	wt_user_follow = 1
	wt_rti_follow = 1
	wt_tag = 1
	wt_department = 1
	wt_popularity = 1

	fact_all = wt_user_follow * fact_user_follow
	fact_all += wt_rti_follow * fact_rti_follow
	fact_all += wt_tag * fact_tag
	fact_all += wt_department * fact_department
	fact_all += wt_popularity * fact_popularity

	activity_entry_date = activity.entry_date
	time_decay = (datetime.now().replace(tzinfo=None) - activity_entry_date.replace(tzinfo=None)  ).total_seconds() 
	time_decay = math.log(time_decay / 60.0 / 60.0)

	relevance = (fact_all + 10) / time_decay
	activity_relevance = models.Activity_relevance.objects.filter(user = user, activity = activity).first()
	if not activity_relevance:
		activity_relevance = models.Activity_relevance()
		activity_relevance.user = user
		activity_relevance.activity = activity
	
	activity_relevance.relevance = relevance
	activity_relevance.save()

def update_all_user_activity_relevance():
	users = models.User.objects.all()
	activities = models.Activity.objects.all()

	for user in users:
		for activity in activities:
			print user.id, activity.id
			calc_relevance(user, activity)


def update_user_relevance(user):
	activities = models.Activity.objects.all()
	for activity in activities:
		calc_relevance(user, activity)

def update_activity_relevance(activity):
	users = models.User.objects.all()
	for user in users:
		calc_relevance(user, activity)


