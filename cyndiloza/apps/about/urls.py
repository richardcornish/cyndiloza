from django.conf.urls import patterns, include, url


urlpatterns = patterns('cyndiloza.apps.about.views',

    url(r'^$',
        view='about_list',
        name='about_about_detail'
    ),

)
