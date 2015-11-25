from rtiapp import models
from datetime import timedelta,datetime

def calc_relevance(user, activity):
	rti_query = activity.rti_query
	activity_user = activity.user
	rti_tags  = models.RTI_tag.objects.filter(rti_query = rti_query)
	rti_department = activity.department


	user_tags = models.Follow_topic.objects.filter(follower = user)
	user_tag_list = []
	for tag in user_tags:
		user_tag_list.append(tag.followee)
	
	user_departments = models.Follow_department.objects.filter(follower = user)
	user_department_list = []
	for dept in user_departments:
		user_department_list.append(dept.followee)

	fact_user_follow = len(models.Follow_user.objects.filter(follower = user, followee = activity_user))
	fact_rti_follow = len(models.Activity.objects.filter(user = user, rti_query = rti_query. activity_type = 'follow'))
	
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
	time_decay = (activity_entry_date.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)).total_seconds()

