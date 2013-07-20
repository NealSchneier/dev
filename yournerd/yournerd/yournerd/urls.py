from django.conf.urls import patterns, include, url
from shownerd import views 
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

#    url(r'^hello/$', views.hello),
#    url(r'^time/$', views.current_datetime),
#    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^smartphone/$', views.smartphones),
#    url(r'^users/$', views.users),
    # Examples:
    # url(r'^$', 'yournerd.views.home', name='home'),
    # url(r'^yournerd/', include('yournerd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
import os
urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
