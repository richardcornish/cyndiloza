from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from cyndiloza.news.models import Place


class PlacesFeed(Feed):

    title_template = 'feeds/places/title.html'
    description_template = 'feeds/places/description.html'

    def title(self):
        return u"%s's places" % Site.objects.get_current().name

    def description(self):
        return u"The journalism portfolio of %s" % Site.objects.get_current().name

    def link(self):
        return reverse('news_place_list')

    def items(self):
        return Place.objects.all()[:20]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description


class PlacesByArticleFeed(Feed):

    title_template = 'feeds/articles/title.html'
    description_template = 'feeds/articles/description.html'

    def get_object(self, request, slug):
        return get_object_or_404(Place, slug=slug)

    def title(self, obj):
        return u"%s's articles at %s" % (Site.objects.get_current().name, obj.name)

    def description(self, obj):
        return u"The journalism portfolio of %s" % Site.objects.get_current().name

    def link(self, obj):
        return obj.get_absolute_url()

    def items(self, obj):
        return obj.article_set.all()[:20]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description
