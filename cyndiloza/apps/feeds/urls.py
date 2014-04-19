from django.conf.urls import patterns, include, url


urlpatterns = patterns('cyndiloza.apps.feeds.views',

    # Articles
    url(r'^articles/$',
        view='feed_articles',
        name='feed_articles'
    ),

    # Articles by Place
    url(r'^places/(?P<slug>[-\w]+)/$',
        view='feed_articles_by_place',
        name='feed_articles_by_place'
    ),

)
