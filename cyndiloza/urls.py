from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # News
    (r'^articles/', include('cyndiloza.apps.news.urls')),

    # Places
    (r'^places/', include('cyndiloza.apps.places.urls')),

    # About
    (r'^about/', include('cyndiloza.apps.about.urls')),

    # Feeds
    (r'^feeds/', include('cyndiloza.apps.feeds.urls')),

    # Sitemaps
    (r'^', include('cyndiloza.apps.sitemaps.urls')),

    # Admin password reset
    url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
    (r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),

    # Admin
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/admin/'}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Robots
    (r'^robots\.txt$', include('robots.urls')),

    # Home
    url(r'^$', 'cyndiloza.views.home', name='home'),

)


# Static/media for local development
if getattr(settings, 'DEBUG', False):
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Custom 500 error handler to render {{ site }}
handler500 = 'cyndiloza.views.server_error'
