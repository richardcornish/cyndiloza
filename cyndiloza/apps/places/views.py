from django.views.generic import ListView, DetailView

from cyndiloza.apps.news.models import Article, Publication
from cyndiloza.apps.places.models import Place


class PlaceLatestFeedView(ListView):
    queryset = Article.objects.filter(published=True).filter(place__isnull=False)[0:25]
    template_name = 'places/place_list_latest.html'

    def render_to_response(self, context, **kwargs):
        return super(PlaceAllFeedView, self).render_to_response(context, content_type='application/xml', **kwargs)

place_latest_feed = PlaceLatestFeedView.as_view()


class PlaceAllFeedView(ListView):
    model = Publication
    template_name = 'places/place_list_kml.html'

    def render_to_response(self, context, **kwargs):
        return super(PlaceAllFeedView, self).render_to_response(context, content_type='application/vnd.google-earth.kml+xml', **kwargs)

place_all_feed = PlaceAllFeedView.as_view()


class PlaceDetailView(DetailView):
    model = Place

place_detail = PlaceDetailView.as_view()


class PlaceListView(ListView):
    model = Publication

    def get_context_data(self, **kwargs):
        context = super(PlaceListView, self).get_context_data(**kwargs)
        context['article_list'] = Article.objects.filter(published=True).filter(place__isnull=False)[0:51]
        return context

place_list = PlaceListView.as_view()
