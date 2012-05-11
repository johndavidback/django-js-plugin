from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'plugin.views.home', name='home'),
    url(r'^plugin/widget\.js$', 'plugin.views.widget', name='widget'),
    url(r'^plugin/widget2\.js$', 'plugin.views.widget2', name='widget2'),
    url(r'^plugin/load_image/', 'plugin.views.load_image', name='load_image'),

    url(r'(?P<page_id>\d+)/click', 'plugin.views.click', name='click'),
    # url(r'^plugin/', include('plugin.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
