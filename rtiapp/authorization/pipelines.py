from django.shortcuts import redirect
from django.http import HttpResponse
import json
import urllib2
from datetime import datetime
from rtiapp.rtiengine import relevance
from rtiapp import models
from time import mktime
from urllib2 import urlopen, HTTPError
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile
from django.core import signing
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login, logout

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
        avatar = urlopen(url)
        profile.profile_picture.save(slugify(user.username + " social") + '.jpg', 
                            ContentFile(avatar.read()))
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
    if not models.Relevance.objects.filter(user = user).first():
        relevance.make_relevance_for_user(user)
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

def user_password(backend, user, response, details, is_new, *args, **kwargs):
    print "DETAILS", details
    if backend.name != 'email':
        return
    print "IS NEW ", is_new
    password = response['password']
    if type(password) is list:
        password = password[0]
    print "RESPONSE", response
    print "password ", password
    user_profile = models.User_profile.objects.filter(user = user).first()
    print "USER", user.username, user.email
    if not user_profile.email_signed_up:
        user.set_password(password)
        user.save()
        user_profile.email_signed_up = True
        user_profile.save()
    elif not user.check_password(password):
        print password
        print "ERRRRR"
        # return {'user': None, 'social': None}
        return redirect('/login_error')


def SendVerificationEmail(strategy, backend, code):
    """
    Send an email with an embedded verification code and the necessary details to restore the required session
    elements to complete the verification and sign-in, regardless of what browser the user completes the
    verification from.
    """

    if backend.name == 'email':
        signature = signing.dumps({"session_key": strategy.session.session_key, "email": code.email},
                                  key=settings.EMAIL_SECRET_KEY)
        verifyURL = "{0}?verification_code={1}&signature={2}".format(
            reverse('social:complete', args=(backend.name,)),
            code.code, signature)
        verifyURL = strategy.request.build_absolute_uri(verifyURL)
        

        print verifyURL
#     emailHTML = # Include your function that returns an html string here
#     emailText = """Welcome to MyApp!
# In order to login with your new user account, you need to verify your email address with us.
# Please copy and paste the following into your browser's url bar: {verifyURL}
# """.format(verifyURL=verifyURL)
 
#     kwargs = {
#         "subject": "Verify Your Account",
#         "body": emailText,
#         "from_email": "MyApp <noreply@myapp.com>",
#         "to": ["recipient@email.address"],
#     }
 
#     email = EmailMultiAlternatives(**kwargs)
#     email.attach_alternative(emailHTML, "text/html")
#     email.send()

