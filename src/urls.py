from synchroKitTesterServer import views
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SynchroKitTesterServer.views.home', name='home'),
    # url(r'^SynchroKitTesterServer/', include('SynchroKitTesterServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^get/(?P<model>[a-zA-Z]+)/$', views.get_model),
    url(r'^get/updateDate/(?P<model>[a-zA-Z]+)/$', views.get_update_date),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
)
