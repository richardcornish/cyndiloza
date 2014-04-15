from django.conf.urls import patterns, url, include


urlpatterns = patterns('cyndiloza.about.views',

    # About detail
    # No need for slug because we always have one "about" entry
    url(r'^$',
        view='about_detail_view',
        name='about_about_detail'
    ),

)
