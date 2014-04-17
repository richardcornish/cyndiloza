from django.conf.urls import patterns, include, url


urlpatterns = patterns('cyndiloza.apps.places.views',

    # Latest 25 places in XML
    # TODO: CONVERT TO JSON!
    url(r'^latest.xml$',
        view='place_latest_feed',
        name='places_place_latest'
    ),

    # All places in KML
    url(r'^all.kml$',
        view='place_all_feed',
        name='places_place_kml'
    ),

    # Place detail
    url(r'^(?P<slug>[-\w]+)/$',
        view='place_detail',
        name='places_place_detail'
    ),

    # Place list
    url(r'^$',
        view='place_list',
        name='places_place_list'
    ),

)
