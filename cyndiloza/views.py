from django.views.generic import list_detail
from django.shortcuts import render_to_response
from django.template import RequestContext

from cyndiloza.news.models import Article, Publication, FavoriteList
from cyndiloza.about.models import About


def home_view(request):
    queryset = Article.objects.filter(published=True)
    template_object_name = 'article'
    template_name = 'home.html'
    extra_context = {
        'featured_list': Article.objects.filter(published=True, featured=True)[0:1],
        'latest_list': Article.objects.filter(published=True)[0:3],
        'publication_list': Publication.objects.all().order_by('rank'),
        'favorite_list': FavoriteList.objects.filter(published=True).order_by('title'),
        'word_list': Article.objects.filter(published=True)[0:126],
        'about': About.objects.all()[0]
    }
    response = list_detail.object_list(
        request,
        queryset=queryset,
        template_object_name=template_object_name,
        template_name=template_name,
        extra_context=extra_context
    )
    return response


def server_error(request, template_name='500.html'):
    return render_to_response(
        template_name,
        context_instance = RequestContext(request)
    )
