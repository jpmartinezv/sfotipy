from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-]+)/', 'tracks.views.track_view', name = 'track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name = 'singup'),
    url(r'^signin/', 'userprofiles.views.signin', name = 'singin'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT,})
    )
