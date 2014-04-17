from django.conf.urls import patterns, include, url


urlpatterns = patterns('cyndiloza.apps.news.views',

    # Article detail
    url(r'^(?P<slug>[-\w]+)/$',
        view='article_detail',
        name='news_article_detail'
    ),

    # Article list
    url(r'^$',
        view='article_list',
        name='news_article_list'
    ),

    # Publication detail
    url(r'^#(?P<slug>[-\w]+)$',
        view='publication_detail',
        name='news_publication_detail'
    ),

)
