from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^weekly$', 'fantasy.views.weekly'),
    url(r'^teams$', 'fantasy.views.teams'),
    url(r'^scoreboards/date/(\d{8})/$', 'fantasy.views.scoreboards'),
    url(r'^game/name/(\d+)/$', 'fantasy.views.league'),
    url(r'^game/date/(\d{8})/$', 'fantasy.views.game'),
    url(r'^league/(\d+)/$', 'fantasy.views.league_weekly'),
    url(r'^user/$', 'fantasy.views.add_user'),
    url(r'^addLeague/$', 'fantasy.views.add_league'),
    url(r'^user/(\d{8})/daily/(\d{8})/$', 'fantasy.views.daily_picks'),
    url(r'^temp/$','fantasy.views.temp'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
import os
urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), '../fantasy/media')}),
)
