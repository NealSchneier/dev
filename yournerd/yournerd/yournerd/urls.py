from django.conf.urls import patterns, include, url
from shownerd import views 
from django.conf import settings
from rest_framework import routers
from webService import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)



urlpatterns = patterns('',

#    url(r'^hello/$', views.hello),
#    url(r'^time/$', views.current_datetime),
#    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
#    url(r'^smartphone/$', views.smartphones),
#    url(r'^users/$', views.users),
    # Examples:
    # url(r'^$', 'yournerd.views.home', name='home'),
    # url(r'^yournerd/', include('yournerd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
import os
urlpatterns += patterns('',
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
