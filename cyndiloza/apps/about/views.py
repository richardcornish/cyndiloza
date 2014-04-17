from django.views.generic import DetailView

from cyndiloza.apps.about.models import About


class AboutDetailView(DetailView):
    model = About

about_detail = AboutDetailView.as_view()
