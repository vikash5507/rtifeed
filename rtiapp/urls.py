from django.conf.urls import patterns, url
from rtiapp.views import views_test
urlpatterns = patterns('',
	url(r'^fblogintest', views_test.fblogintest, name = 'fblogintest'),
	url(r'^logintest', views_test.logintest, name = 'logintest'),
)
