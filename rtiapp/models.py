from django.db import models
from django.contrib.auth.models import User

#TO DO
# max_length attributes

# https://docs.djangoproject.com/en/1.8/ref/contrib/auth/
class State(models.Model):
	def __unicode__(self):
		return self.user.state_name

	state_name = models.CharField(max_length = 200)
	capital_name = models.CharField(null = True, max_length = 200)
	latitude = models.FloatField(null = True)
	longitude = models.FloatField(null = True)

class Address(models.Model):
	def __unicode__(self):
		return self.user.address_line

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
	profile_picture = models.ImageField(upload_to  = 'static/profile_picture', default = 'static/profile_picture/default.jpg')
	reputation = models.FloatField(default = 10)
	gender = models.CharField(max_length = 200, null = True)
	date_of_birth = models.DateTimeField(null = True)
	address = models.ForeignKey(Address, null = True)
	bio_description = models.CharField(max_length = 200, null = True)
	entry_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now_add=True)

class RTI_query(models.Model):
	def __unicode__(self):
		return self.description
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	query_text = models.TextField()
	description = models.CharField(max_length = 200)
	rti_number = models.CharField(max_length = 50)
	rti_file_date = models.DateTimeField()
	response_status = models.BooleanField(default = False)
	query_type = models.CharField(max_length = 50)
	# type : centre, state
	entry_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now_add=True)

class RTI_query_file(models.Model):
	def __unicode__(self):
		return self.rti_query

	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	query_picture = models.ImageField(upload_to  = 'static/query_picture', default = 'static/query_picture/default.jpg')
	query_document = models.FileField(upload_to  = 'static/query_document', null = True)

# STATE RTI QUERIES
class State_department(models.Model):
	def __unicode__(self):
		return self.department_name

	state = models.ForeignKey(State, on_delete = models.CASCADE)
	department_name = models.CharField(max_length = 200)

class State_authority(models.Model):
	def __unicode__(self):
		return self.authority_name

	department = models.ForeignKey(State_department, on_delete = models.CASCADE)
	authority_name = models.CharField(max_length = 200)

class State_RTI_query(models.Model):
	def __unicode__(self):
		return self.rti_query

	rti_query = models.OneToOneField(RTI_query, primary_key = True)
	department = models.ForeignKey(State_department, on_delete = models.SET_DEFAULT, default = 1)
	authority = models.ForeignKey(State_authority, on_delete = models.SET_NULL, null = True)

#CENTRAL RTI QUERIES
class Central_department(models.Model):
	def __unicode__(self):
		return self.department_name

	department_name = models.CharField(max_length = 200)
	website = models.CharField(max_length = 200, null = True)

class Central_authority(models.Model):
	def __unicode__(self):
		return self.authority_name

	department = models.ForeignKey(Central_department, on_delete = models.CASCADE)
	authority_name = models.CharField(max_length = 200)

class Central_RTI_query(models.Model):
	def __unicode__(self):
		return self.rti_query

	rti_query = models.OneToOneField(RTI_query, primary_key = True)
	department = models.ForeignKey(Central_department, on_delete = models.SET_DEFAULT, default = 1)
	authority = models.ForeignKey(Central_authority, on_delete = models.SET_NULL, null = True)

# RESPONSE
class RTI_response(models.Model):
	def __unicode__(self):
		return self.description

	rti_query = models.OneToOneField(RTI_query, primary_key = True, on_delete = models.CASCADE)
	response_text = models.TextField()
	description = models.CharField(max_length = 200)
	# check for response date > query date
	rti_response_date = models.DateTimeField(null = True)
	entry_date = models.DateTimeField()
	update_date = models.DateTimeField(auto_now_add=True)

class RTI_response_file(models.Model):
	def __unicode__(self):
		return self.rti_response

	rti_response = models.ForeignKey(RTI_response, on_delete = models.CASCADE)
	query_picture = models.ImageField(upload_to  = 'static/response_picture', default = 'static/response_picture/default.jpg')
	query_document = models.FileField(upload_to  = 'static/response_document', null = True)

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

class Like(models.Model):
	def __unicode__(self):
		return self.rti_query

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	entry_date = models.DateTimeField(auto_now_add=True)

class Share(models.Model):
	def __unicode__(self):
		return self.rti_query

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	share_text = models.TextField(null = True)
	entry_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	comment_text = models.TextField(null = True)
	entry_date = models.DateTimeField(auto_now_add=True)


class Follow_query(models.Model):
	def __unicode__(self):
		return self.rti_query

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	entry_date = models.DateTimeField(auto_now_add=True)

class Follow_user(models.Model):
	def __unicode__(self):
		return self.follower

	follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name='follower')
	followee = models.ForeignKey(User, on_delete = models.CASCADE, related_name='followee')
	entry_date = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
	def __unicode__(self):
		return self.follower

	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='notified')
	notification_text = models.CharField(max_length = 200)
	notification_url = models.CharField(max_length = 300)
	notification_type = models.CharField(max_length = 200)
	notification_status = models.BooleanField(default = False)
	seen_date = models.DateTimeField(null = True)
	rti_query = models.ForeignKey(RTI_query, null = True, on_delete = models.SET_NULL)
	other_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='notified_by')
	entry_date = models.DateTimeField(auto_now_add=True)

class Relevance(models.Model):
	def __unicode__(self):
		return self.relevance

	user = models.ForeignKey(User, on_delete = models.CASCADE)
	rti_query = models.ForeignKey(RTI_query, on_delete = models.CASCADE)
	relevance = models.FloatField(default = 0.0)
	views = models.IntegerField(default = 0)
	update_date = models.DateTimeField(auto_now_add=True)









	


	
