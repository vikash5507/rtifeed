"""
Django settings for RTIFeed project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8b0e$m=8_#-nj7-b=9c8s9h9)knu8-bg&5n&qni)9_pe+ye(xz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost:8000', '127.0.0.1', 'www.rtifeed.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'social.apps.django_app.default',
    'haystack',
    'django_social_share',
    'rtiapp',

    
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request'
)

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'social.backends.email.EmailAuth',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',  # <--- enable this one
    
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    
    'rtiapp.authorization.pipelines.get_user_avatar',
    'social.pipeline.mail.mail_validation',
    'rtiapp.authorization.pipelines.user_password',
    'social.pipeline.user.user_details',
)

# SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'twitter')
# SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
# SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'
# SOCIAL_AUTH_PARTIAL_PIPELINE_KEY = 'partial_pipeline'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'rtiapp.authorization.pipelines.SendVerificationEmail'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email_verify_sent/'

SOCIAL_AUTH_FACEBOOK_KEY              = '1659360547643851'
SOCIAL_AUTH_FACEBOOK_SECRET           = '7a3c2e356b7dde957856279052f31e68'

SOCIAL_AUTH_TWITTER_KEY              = 'neZJAlQOEeZUkNm7EV1p0fnVy'
SOCIAL_AUTH_TWITTER_SECRET           = 'beVCDHUxrILVxqu8msMhsORwux0LqXSL0l4vv9diWkhne1pCED'

SOCIAL_AUTH_TWITTER_SCOPE = [
    'email',
]

SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
    'user_friends',
    # 'gender',
    'public_profile'
]

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  # 'locale': 'ru_RU',
  'fields': 'id, name, email, age_range, gender'
}

SITE_ID = 1

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/home'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'

ROOT_URLCONF = 'RTIFeed.urls'

WSGI_APPLICATION = 'RTIFeed.wsgi.application'

ACCOUNT_ACTIVATION_DAYS = 2
REGISTRATION_OPEN = True


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'RTIFeed3',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_HOST_USER = 'rtifeedteam@rtifeed.com'
EMAIL_HOST_PASSWORD = 'erkoGUcWVOOJckxu53wgPw'
# Port 587 is the default port for smtp submission, but some will use 25, 465, or an arbitrary port #
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_SECRET_KEY = 'soochnakaadhikaar'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,"rtiapp/static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# STATIC_ROOT = '/rtiapp/static'
