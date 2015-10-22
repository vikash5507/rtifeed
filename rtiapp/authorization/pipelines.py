from django.http import HttpResponse
import json
import urllib2
from datetime import datetime

from rtiapp import models
from time import mktime

def get_user_avatar(backend, user, response, details, *args, **kwargs):
    a = 5
    print "TEST"
    url = None
    profile = models.User_profile.objects.filter(user = user).first()

    if not profile:
        profile = models.User_profile()
        profile.user = user
        profile.entry_date = datetime.now()

    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        profile.profile_picture = url
        print response
        fb_data = {
            # 'city': response['location']['name'],
            'gender': str(response['gender']),
            # 'locale': response['locale'],
            # 'dob': response['birthday']
        }
        # profile.city = fb_data['city']
        profile.gender = fb_data['gender']
        print "gendefr", fb_data['gender']
        # profile.city = fb_data['city']
        # profile.date_of_birth = fb_data['dob']

    profile.save()


    # elif backend.name == 'twitter':
    #     url = response.get('profile_image_url', '').replace('_normal', '')

    # social_user = user.social_auth.filter(provider = 'facebook').first()
    # if social_user:
    #     url = u'https://graph.facebook.com/{0}/' \
    #         u'user_friends?fields=id,name' \
    #         u'&access_token={1}'.format(
    #           social_user.uid,
    #           social_user.extra_data['access_token'],
    #         )

    # print url
    # request = urllib2.Request(url)
    # friends = json.loads(urllib2.urlopen(request).read()).get('data')
    # # print "lalala", friends
    # for friend in friends:
    #     print friend
    # # print social_user
    # if url:
        # profile = user.get_profile()
        # avatar = urlopen(url).read()
        # fout = open(filepath, "wb") #filepath is where to save the image
        # fout.write(avatar)
        # fout.close()
        # profile.photo = url_to_image # depends on where you saved it
        # profile.save()
    # print url
    # return HttpResponse("Done")