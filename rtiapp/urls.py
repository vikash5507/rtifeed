from django.conf.urls import patterns, url
from rtiapp.views import views_test, views_profile
from rtiapp.views import views_login, views_home

urlpatterns = patterns('',
	url(r'^fblogintest$', views_test.fblogintest, name = 'fblogintest'),
	url(r'^logintest$', views_test.logintest, name = 'logintest'),


	url(r'^$', views_login.login_page, name = 'loginpage'),
	# url(r'^home$', views_home.home_page, name = 'homepage'),
	url(r'^base$', views_test.base, name = 'basepage'),
	url(r'^home$', views_home.home_page, name = 'homepage'),
	url(r'^get_feed$', views_home.get_feed, name = 'get_feed'),
	url(r'^post_comment$', views_home.post_comment, name = 'post_comment'),
	url(r'^post_delete_comment$', views_home.post_delete_comment, name = 'post_delete_comment'),
	url(r'^post_like$', views_home.post_like, name = 'post_like'),
	url(r'^post_unlike$', views_home.post_unlike, name = 'post_unlike'),
	url(r'^logout$', views_login.u_logout, name = 'logout'),
	url(r'^profile/(?P<username>\w+)/$', views_profile.get_user_profile, name="detail_profile")

)
