from rtiapp import models
users = models.User.objects.all()

for user in users:
	no_rtis = len(models.RTI_query.objects.filter(user = user))
	no_followers = len(models.Follow_user.objects.filter(followee = user))
	reputation = no_rtis + no_followers
	user_profile = models.User_profile.objects.filter(user = user).first()
	if user_profile:
		user_profile.reputation = reputation
		user_profile.save()
