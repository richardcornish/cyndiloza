from django.views.generic import list_detail
from cyndiloza.news.models import Article, Publication
from cyndiloza.places.models import Place


def place_latest_view(request):
    queryset = Article.objects.filter(published=True).filter(place__isnull=False)[0:25]
    template_object_name = 'article'
    template_name = 'places/place_list_latest.html'
    mimetype = 'application/xml'
    response = list_detail.object_list(
        request,
        queryset=queryset,
        template_object_name=template_object_name,
        template_name=template_name
    )
    return response


def place_kml_view(request):
    queryset = Publication.objects.all()
    template_object_name = 'publication'
    template_name = 'places/place_list_kml.html'
    mimetype = 'application/vnd.google-earth.kml+xml'
    response = list_detail.object_list(
        request,
        queryset=queryset,
        template_object_name=template_object_name,
        template_name=template_name
    )
    return response


def place_detail_view(request, slug):
    queryset = Place.objects.all()
    template_object_name = 'place'
    template_name = 'places/place_detail.html'
    response = list_detail.object_detail(
        request,
        queryset=queryset,
        template_object_name=template_object_name,
        template_name=template_name,
        slug=slug
    )
    return response


def place_list_view(request):
    queryset = Publication.objects.all()
    template_object_name = 'publication'
    template_name = 'places/place_list.html'
    extra_context = {
        'article_list': Article.objects.filter(published=True).filter(place__isnull=False)[0:51]
    }
    response = list_detail.object_list(
        request,
        queryset=queryset,
        template_object_name=template_object_name,
        template_name=template_name
    )
    return response
