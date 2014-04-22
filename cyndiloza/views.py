from django.views.generic import ListView
from django.shortcuts import render

from cyndiloza.apps.news.models import Article, Publication, FavoriteList
from cyndiloza.apps.about.models import About


class HomeView(ListView):
    queryset = Article.objects.filter(published=True)
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['featured_list'] = Article.objects.filter(published=True, featured=True)[0:1]
        context['latest_list'] = Article.objects.filter(published=True)[0:3]
        context['publication_list'] = Publication.objects.all().order_by('rank')
        context['favorite_list'] = FavoriteList.objects.filter(published=True).order_by('title')
        context['word_list'] = Article.objects.filter(published=True)[0:126]
        context['about'] = About.objects.all()[0]
        return context

home = HomeView.as_view()


def not_found(request):
    return render(request, '404.html', {'request_path': request.path})

def server_error(request):
    return render(request, '500.html')
