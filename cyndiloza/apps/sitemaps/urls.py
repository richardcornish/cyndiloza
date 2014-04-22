from django.conf.urls import patterns, include, url
from django.contrib.sitemaps import FlatPageSitemap

from cyndiloza.apps.sitemaps.views import ArticleSitemap, PlaceSitemap


sitemaps = {
    'articles': ArticleSitemap,
    'places': PlaceSitemap,
    'flatpages': FlatPageSitemap
}


urlpatterns = patterns('django.contrib.sitemaps.views',

    # Sitemap index
    url(r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}, name='sitemaps_index'),

    # Sitemap for individual apps
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),

)
