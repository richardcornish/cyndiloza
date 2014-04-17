from django.conf.urls import patterns, url, include
from django.contrib.sitemaps import GenericSitemap, FlatPageSitemap

from cyndiloza.apps.news.models import Article
from cyndiloza.apps.news.models import Place


article_dict = {
    'queryset': Article.objects.filter(published=True),
    'date_field': 'date',
}

place_dict = {
    'queryset': Place.objects.all(),
}


sitemaps = {
    'article': GenericSitemap(article_dict, priority=0.5),
    'place': GenericSitemap(place_dict, priority=0.5),
    'flatpages': FlatPageSitemap,
}


urlpatterns = patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'sitemap', {'sitemaps': sitemaps}),
)
