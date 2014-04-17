from django.conf.urls import patterns, url, include

from cyndiloza.apps.feeds.articles import ArticlesFeed
from cyndiloza.apps.feeds.places import PlacesFeed, PlacesByArticleFeed


urlpatterns = patterns('',

    # Articles
    url(r'^articles/$',
        ArticlesFeed(),
        name='articles_article_feed'
    ),

    # Places
    url(r'^places/$',
        PlacesFeed(),
        name='articles_place_feed'
    ),

    # Places by Article
    url(r'^places/(?P<slug>[-\w]+)/$',
        PlacesByArticleFeed(),
        name='articles_place_by_article_feed'
    ),

)
