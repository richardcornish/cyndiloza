from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from cyndiloza.news.models import Article


class ArticlesFeed(Feed):

    title_template = 'feeds/articles/title.html'
    description_template = 'feeds/articles/description.html'

    def title(self):
        return u"%s's articles" % Site.objects.get_current().name

    def description(self):
        return u"The journalism portfolio of %s" % Site.objects.get_current().name

    def link(self):
        return reverse('news_article_list')

    def items(self):
        return Article.objects.filter(published=True).order_by('-date')[:20]

    def item_title(self, item):
        return item.headline

    def item_description(self, item):
        return item.body
