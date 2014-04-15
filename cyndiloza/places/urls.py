from django.conf.urls import patterns, url, include


urlpatterns = patterns('cyndiloza.places.views',

    # Latest 25 places in XML
    # TODO: CONVERT TO JSON!
    url(r'^latest.xml$',
        view='place_latest_view',
        name='places_place_latest'
    ),

    # All places in KML
    url(r'^all.kml$',
        view='place_kml_view',
        name='places_place_kml'
    ),

    # Place detail
    url(r'^(?P<slug>[-\w]+)/$',
        view='place_detail_view',
        name='places_place_detail'
    ),

    # Place list
    url(r'^$',
        view='place_list_view',
        name='places_place_list'
    ),

)
