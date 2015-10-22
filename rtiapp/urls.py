from django.conf.urls import patterns, url
from rtiapp.views import views_test, views_profile
from rtiapp.views import views_login

urlpatterns = patterns('',
	url(r'^fblogintest$', views_test.fblogintest, name = 'fblogintest'),
	url(r'^logintest$', views_test.logintest, name = 'logintest'),


	url(r'^$', views_login.login_page, name = 'loginpage'),
	# url(r'^home$', views_home.home_page, name = 'homepage'),
	url(r'^base$', views_test.base, name = 'basepage'),
	url(r'^home$', views_test.home, name = 'homepage'),
	url(r'^logout$', views_login.u_logout, name = 'logout'),
	url(r'^profile/(?P<username>\w+)/$', views_profile.get_user_profile, name="detail_profile")

)
