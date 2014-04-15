from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    # Admin password reset
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    (r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # News
    (r'^articles/', include('cyndiloza.news.urls')),

    # Places
    (r'^places/', include('cyndiloza.places.urls')),

    # About
    (r'^about/', include('cyndiloza.about.urls')),

    # Feeds
    (r'^feeds/', include('cyndiloza.feeds.urls')),

    # Robots
    (r'^robots\.txt$', include('robots.urls')),

    # Sitemaps
    (r'^', include('cyndiloza.sitemaps.urls')),

    # Home
    url(r'^$', 'cyndiloza.views.home_view', name='home'),

)

handler500 = 'cyndiloza.views.server_error'
