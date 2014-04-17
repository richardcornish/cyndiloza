from django.conf.urls import patterns, include, url


urlpatterns = patterns('cyndiloza.apps.about.views',

    # About detail
    # No need for slug because we always have one "about" entry
    url(r'^$',
        view='about_detail',
        name='about_about_detail'
    ),

)
