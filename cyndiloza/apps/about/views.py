from django.views.generic import ListView

from cyndiloza.apps.about.models import About


class AboutDetailView(ListView):
    queryset = About.objects.all()[0]
    context_object_name = 'about'
    template_name = 'about/about_list.html'

about_list = AboutDetailView.as_view()
