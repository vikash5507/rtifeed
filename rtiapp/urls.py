from django.conf.urls import patterns, url
from rtiapp.views import views_test, views_profile
from rtiapp.views import views_login, views_home
from rtiapp.views import views_tds
from rtiapp.views import views_shareRTI

urlpatterns = patterns('',
	url(r'^fblogintest$', views_test.fblogintest, name = 'fblogintest'),
	url(r'^logintest$', views_test.logintest, name = 'logintest'),
	url(r'^departmenttest$', views_test.departmenttest, name = 'departmenttest'),

	url(r'^$', views_login.login_page, name = 'loginpage'),
	url(r'^login_error$', views_login.login_error_page, name = 'loginerror_page'),
	# url(r'^home$', views_home.home_page, name = 'homepage'),
	url(r'^base$', views_test.base, name = 'basepage'),
	url(r'^home$', views_home.home_page, name = 'homepage'),
	url(r'^rti_page$', views_home.rti_page, name = 'rti_page'),
	url(r'^get_feed$', views_home.get_feed, name = 'get_feed'),
	url(r'^view_rti$', views_home.view_rti, name = 'view_rti'),

	url(r'^get_profile_feed$', views_profile.get_profile_feed, name = 'get_profile_feed'),
	url(r'^get_profile_follow$', views_profile.get_profile_follow, name = 'get_profile_follow'),
	


	url(r'^post_comment$', views_home.post_comment, name = 'post_comment'),
	url(r'^post_edit_comment$', views_home.post_edit_comment, name = 'post_edit_comment'),
	url(r'^post_delete_comment$', views_home.post_delete_comment, name = 'post_delete_comment'),
	url(r'^load_prev_comments$', views_home.load_prev_comments, name = 'load_prev_comments'),
	
	url(r'^post_like$', views_home.post_like, name = 'post_like'),
	url(r'^post_unlike$', views_home.post_unlike, name = 'post_unlike'),
	url(r'^post_follow_query$', views_home.post_follow_query, name = 'post_follow_query'),
	url(r'^post_unfollow_query$', views_home.post_unfollow_query, name = 'post_unfollow_query'),

	url(r'^share_rti_query$', views_shareRTI.share_rti_query, name = 'share_rti_query'),
	url(r'^get_departments_of$', views_shareRTI.get_departments_of, name = 'get_departments_of'),
	url(r'^post_rti_query$', views_shareRTI.post_rti_query, name = 'post_rti_query'),
	
	url(r'^logout$', views_login.u_logout, name = 'logout'),
	url(r'^register', views_login.register, name = 'register'),
	
	url(r'^profile/(?P<username>[-\w.]+)/$', views_profile.display_user_profile, name="detail_profile"),
	url(r'^profile/(?P<username>[-\w.]+)/(?P<details_required>\w+)/$', views_profile.display_user_details, name="user_details"),
	url(r'^post_follow_user$', views_profile.post_follow_user, name = 'post_follow_user'),
	url(r'^post_unfollow_user$', views_profile.post_unfollow_user, name = 'post_unfollow_user'),

	url(r'^department/(?P<department_id>\w+)/$', views_tds.display_department_profile, name="department_detail_profile"),
	url(r'^department/(?P<department_id>\w+)/(?P<details_required>\w+)/$', views_tds.display_department_details, name="department_details"),

	url(r'^topic/(?P<topic_id>\w+)/$', views_tds.display_topic_profile, name="topic_detail_profile"),
	url(r'^topic/(?P<topic_id>\w+)/(?P<details_required>\w+)/$', views_tds.display_topic_details, name="topic_details"),

	url(r'^state/(?P<state_id>\w+)/$', views_tds.display_state_profile, name="state_detail_profile"),
	url(r'^state/(?P<state_id>\w+)/(?P<details_required>\w+)/$', views_tds.display_state_details, name="state_details"),

	url(r'^get_tds_feed$', views_tds.get_tds_feed, name = 'get_tds_feed'),
	url(r'^post_follow_tds$', views_tds.post_follow_tds, name = 'post_follow_tds'),
	url(r'^post_unfollow_tds$', views_tds.post_unfollow_tds, name = 'post_unfollow_tds'),
	# url(r'^department/(?P<department_id>\w+)/$', views_department.get_department_profile, name="detail_department_profile"),
	# url(r'^department/(?P<department_id>\w+)/(?P<details_required>\w+)/$', views_department.get_department_details, name="department_details")

)
