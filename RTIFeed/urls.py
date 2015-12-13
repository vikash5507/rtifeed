from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RTIFeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'', include('rtiapp.urls')),
    (r'^search/', include('haystack.urls')),
    # url(r'^admin/', include('admin.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'rtiapp.views.views_error.bad_request'
handler403 = 'rtiapp.views.views_error.permission_denied'
handler404 = 'rtiapp.views.views_error.page_not_found'
handler500 = 'rtiapp.views.views_error.server_error'