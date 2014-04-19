from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from cyndiloza.apps.news.models import Article, Place


class ArticlesFeed(Feed):

    title_template = 'feeds/articles/obj_headline.html'
    description_template = 'feeds/articles/obj_body.html'

    def title(self):
        return u"%s's news articles" % Site.objects.get_current().name

    def description(self):
        return u"RSS feed for %s's journalism portfolio articles" % Site.objects.get_current().name

    def link(self):
        return reverse('news_article_list')

    def items(self):
        return Article.objects.filter(published=True).order_by('-date')[:20]

feed_articles = ArticlesFeed()



class ArticlesByPlaceFeed(Feed):

    title_template = 'feeds/articles/obj_headline.html'
    description_template = 'feeds/articles/obj_body.html'

    def get_object(self, request, slug):
        return get_object_or_404(Place, slug=slug)

    def title(self, obj):
        return u"%s's news articles at %s" % (Site.objects.get_current().name, obj.name)

    def description(self, obj):
        return u"RSS feed for %s's journalism portfolio articles at %s" % (Site.objects.get_current().name, obj.name)

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        return obj.article_set.all().filter(published=True)[:20]

feed_articles_by_place = ArticlesByPlaceFeed()
