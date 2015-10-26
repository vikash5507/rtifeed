from rtiapp import models
from datetime import timedelta,datetime

def count_matching_tags(user,rti_query):
	user_tags = models.User_interst.objects.filter(user=user);
	common_tags = models.RTI_tag.objects.filter(tag = user_tags, rti_query = rti_query)
	return len(common_tags)

def calc_relevance(user, rti_query):
	w_like=1
	w_comment=2
	w_follow=3
	w_tags=1
	num_likes=len(models.Like.objects.filter(rti_query=rti_query))
	num_comments=len(models.Comment.objects.filter(rti_query=rti_query))
	num_follows=len(models.Follow_query.objects.filter(rti_query = rti_query))
	relevance=w_like*num_likes+w_comment*num_comments+num_follows*w_follow+ 10;
	# print "Dsdfvs", datetime.now()
	# print "dfsdfsd", rti_query.entry_date
	relevance/=(1.0*(datetime.now().replace(tzinfo=None)-rti_query.entry_date.replace(tzinfo=None)).total_seconds()/60.0+10)

	return relevance

def make_relevance_for_rti(rti_query):
	models.Relevance.objects.filter(rti_query = rti_query).delete()
	all_users = models.User.objects.all()
	
	for user in all_users:
		relevance = calc_relevance(user, rti_query)
		# print relevance
		rel_record = models.Relevance()
		rel_record.user = user
		rel_record.relevance = relevance
		rel_record.rti_query = rti_query
		rel_record.update_date = datetime.now()
		rel_record.save()

def make_relevance_for_user(user):
	models.Relevance.objects.filter(user = user).delete()
	all_rti_queries = models.RTI_query.objects.all()
	
	for rti_query in all_rti_queries:
		relevance = calc_relevance(user, rti_query)
		rel_record = models.Relevance()
		rel_record.user = user
		rel_record.relevance = relevance
		rel_record.rti_query = rti_query
		rel_record.update_date = datetime.now()
		rel_record.save()

def update_relevance_for_rti(rti_query):
	rel_records = models.Relevance.objects.filter(rti_query = rti_query)
	for rel_record in rel_records:
		relevance = calc_relevance(rel_record.user, rel_record.rti_query)
		rel_record.relevance = relevance
		rel_record.update_date = datetime.now()
		rel_record.save()

def update_relevance_for_user(user):
	rel_records = models.Relevance.objects.filter(user = user)
	for rel_record in rel_records:
		relevance = calc_relevance(rel_record.user, rel_record.rti_query)
		rel_record.relevance = relevance
		rel_record.update_date = datetime.now()
		rel_record.save()


def update_all_relevance():
	rel_records = models.Relevance.objects.all()
	for rel_record in rel_records:
		relevance = calc_relevance(rel_record.user, rel_record.rti_query)
		rel_record.relevance = relevance
		rel_record.update_date = datetime.now()
		rel_record.save()	
