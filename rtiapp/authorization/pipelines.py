from django.http import HttpResponse
import json
import urllib2

def get_user_avatar(backend, user, response, details, *args, **kwargs):
    a = 5
    print "TEST"
    url = None
    # if backend.name == 'facebook':
    #     url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

    # elif backend.name == 'twitter':
    #     url = response.get('profile_image_url', '').replace('_normal', '')

    social_user = user.social_auth.filter(provider = 'facebook').first()
    if social_user:
        url = u'https://graph.facebook.com/{0}/' \
            u'user_friends?fields=id,name' \
            u'&access_token={1}'.format(
              social_user.uid,
              social_user.extra_data['access_token'],
            )

    print url
    request = urllib2.Request(url)
    friends = json.loads(urllib2.urlopen(request).read()).get('data')
    # print "lalala", friends
    for friend in friends:
        print friend
    # print social_user
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