from django.conf.urls import patterns, url, include


urlpatterns = patterns('cyndiloza.news.views',

    # Article detail
    url(r'^(?P<slug>[-\w]+)/$',
        view='article_detail_view',
        name='news_article_detail'
    ),

    # Article list
    url(r'^$',
        view='article_list_view',
        name='news_article_list'
    ),

    # Publication detail
    url(r'^#(?P<slug>[-\w]+)$',
        view='publication_detail_view',
        name='news_publication_detail'
    ),

)
