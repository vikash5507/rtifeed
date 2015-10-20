from django.conf.urls import patterns, url
from rtiapp import views
urlpatterns = patterns('',
	url(r'^fblogintest', views.fblogintest, name = 'fblogintest'),
	url(r'^logintest', views.logintest, name = 'logintest'),
)
