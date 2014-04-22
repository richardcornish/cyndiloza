from django.contrib.sitemaps import Sitemap

from cyndiloza.apps.news.models import Article
from cyndiloza.apps.places.models import Place


class ArticleSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Article.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date


class PlaceSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return Place.objects.all()
