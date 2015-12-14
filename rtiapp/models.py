from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
import os
#TO DO
# max_length attributes

# https://docs.djangoproject.com/en/1.8/ref/contrib/auth/
class State(models.Model):
	def __unicode__(self):
		return self.state_name

	state_name = models.CharField(max_length = 200)
	capital_name = models.CharField(null = True, max_length = 200)
	latitude = models.FloatField(null = True)
	longitude = models.FloatField(null = True)

class Address(models.Model):
	def __unicode__(self):
		return self.address_line

	address_line = models.CharField(max_length = 200, null = True)
	state = models.ForeignKey(State, on_delete = models.SET_NULL, null = True)
	city = models.CharField(max_length = 200, null = True)
	pincode = models.CharField(max_length = 200, null = True)
	latitude = models.FloatField(null = True)
	longitude = models.FloatField(null = True)
	entry_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now_add=True)

class User_profile(models.Model):
	def __unicode__(self):
		return self.user.username

	user = models.OneToOneField(User, primary_key = True)
	profile_picture = models.ImageField(upload_to  = 'profile_pictures', default = 'profile_pictures/default.jpg')
	reputation = models.FloatField(default = 10)
	gender = models.CharField(max_length = 200, null = True)
	date_of_birth = models.DateTimeField(null = True)
	address = models.ForeignKey(Address, null = True)
	bio_description = models.CharField(max_length = 200, default = "")
	entry_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now_add=True)
	email_signed_up = models.BooleanField(default = False)
	verification_url = models.CharField(max_length = 500, null = True)
	profile_status = models.CharField(max_length = 200, default = 'incomplete')
	# email_password = models.CharField(max_length = 200, null = True)

class Department(models.Model):
	def __unicode__(self):
		return self.department_name
	department_name = models.CharField(max_length = 200)
	website = models.CharField(null = True, max_length = 200)
	department_type = models.CharField(max_length = 50)
	# centre, state

class Authority(models.Model):
	def __unicode__(self):
		return self.authority_name

	department = models.ForeignKey(Department, on_delete = models.CASCADE)
	authority_name = models.CharField(max_length = 200)
	# centre, state

class State_department(models.Model):
	def __unicode__(self):
		return self.department

	department = models.OneToOneField(Department, on_delete = models.CASCADE)
	state = models.ForeignKey(State, on_delete = models.CASCADE)
	
class Central_department(models.Model):
	def __unicode__(self):
		return self.department
	department = models.OneToOneField(Department, on_delete = models.CASCADE)

# @python_2_unicode_compatible
class RTI_query(models.Model):
	def __unicode__(self):
		return self.description
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	query_text = models.TextField()
	description = models.CharField(max_length = 200)
	rti_file_date = models.DateTimeField()
	response_status = models.BooleanField(default = False)
	query_type = models.CharField(max_length = 50)
	# type : centre, state
	department = models.ForeignKey(Department, on_delete = models.CASCADE)
	authority = models.ForeignKey(Authority, on_delete = models.SET_NULL, null = True)

	entry_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now_add=True)

class RTI_query_file(models.Model):
	def __unicode__(self):
		return self.rti_query

	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	query_picture = models.ImageField(upload_to  = 'query_pictures', default = 'query_pictures/default.jpg')
	query_document = models.FileField(upload_to  = 'query_docs', null = True)
	def extension(self):
		name, extension = os.path.splitext(self.query_picture.name)
		return extension


# RESPONSE
class RTI_response(models.Model):
	def __unicode__(self):
		return self.description

	rti_query = models.OneToOneField(RTI_query, primary_key = True, on_delete = models.CASCADE)
	response_text = models.TextField()
	# check for response date > query date
	rti_response_date = models.DateTimeField(null = True)
	entry_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now_add=True)

class RTI_response_file(models.Model):
	def __unicode__(self):
		return self.rti_response

	rti_response = models.ForeignKey(RTI_response, on_delete = models.CASCADE)
	response_picture = models.ImageField(upload_to  = 'response_pictures', default = 'response_pictures/default.jpg')
	response_document = models.FileField(upload_to  = 'response_documents', null = True)

	def extension(self):
		name, extension = os.path.splitext(self.response_picture.name)
		return extension

class Tag(models.Model):
	def __unicode__(self):
		return self.tag_text
	tag_text = models.CharField(max_length = 200)
	entry_date = models.DateTimeField(auto_now_add=True)

class RTI_tag(models.Model):
	def __unicode__(self):
		return self.tag

	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
	entry_date = models.DateTimeField(auto_now_add=True)

class User_tag(models.Model):
	def __unicode__(self):
		return self.tag

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete = models.CASCADE)
	entry_date = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
	activity_choices = (
		('rti_query', 'rti_query'),
		('rti_response', 'rti_response'),
	    ('comment', 'comment'),
	    ('like', 'like'),
	    ('follow', 'follow'),
	    ('spam', 'spam'),
	)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	activity_type = models.CharField(max_length = 20, choices = activity_choices)
	meta_data = models.TextField(null = True)
	entry_date = models.DateTimeField(auto_now_add = True)

class Follow_user(models.Model):
	def __unicode__(self):
		return self.follower

	follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_follower')
	followee = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_followee')
	entry_date = models.DateTimeField(auto_now_add=True)
	

class Follow_state(models.Model):
	def __unicode__(self):
		return self.follower

	follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name='state_follower')
	followee = models.ForeignKey(State, on_delete = models.CASCADE, related_name='state_followee')
	entry_date = models.DateTimeField(auto_now_add=True)
	

class Follow_topic(models.Model):
	def __unicode__(self):
		return self.follower

	follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name='topic_follower')
	followee = models.ForeignKey(Tag, on_delete = models.CASCADE, related_name='topic_followee')
	entry_date = models.DateTimeField(auto_now_add=True)

class Follow_department(models.Model):
	def __unicode__(self):
		return self.follower

	follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name='department_follower')
	followee = models.ForeignKey(Department, on_delete = models.CASCADE, related_name='department_followee')
	entry_date = models.DateTimeField(auto_now_add=True)


class User_feed(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
	relevance = models.FloatField(default = 0.0)
	entry_date = models.DateTimeField(auto_now_add = True)

class Notification(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	notification_choices = (
		('user_follow', 'user_follow'),
		('rti_query', 'rti_query'),
	)
	notification_type = models.CharField(max_length = 20, choices = notification_choices)
	activity = models.ForeignKey(Activity, on_delete = models.CASCADE, null = True)
	follow = models.ForeignKey(Follow_user, on_delete = models.CASCADE, null = True)
	read_status = models.BooleanField(default = False)
	entry_date = models.DateTimeField(auto_now_add = True)

class Relevance(models.Model):
	def __unicode__(self):
		return self.relevance

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	relevance = models.FloatField(default = 0.0)
	views = models.IntegerField(default = 0)
	update_date = models.DateTimeField(auto_now_add=True)
	feed_head_line = models.TextField(null = True)

class Activity_relevance(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	activity = models.ForeignKey(Activity, on_delete = models.CASCADE)
	relevance = models.FloatField(default = 0.0)
	views = models.IntegerField(default = 0)
	update_date = models.DateTimeField(auto_now_add=True)

class RTI_unlinked_files(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	rti_hash = models.CharField(max_length = 200)
	query_picture = models.ImageField(upload_to  = 'query_pictures')
	linked = models.BooleanField(default = False)
	
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=RTI_unlinked_files)
def photo_post_delete_handler(sender, **kwargs):

    uf = kwargs['instance']
    storage, path = uf.query_picture.storage, uf.query_picture.path
    print "delete"
    if not uf.linked:
    	storage.delete(path)