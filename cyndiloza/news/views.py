from django.views.generic import list_detail
from cyndiloza.news.models import Article, Publication


def article_list_view(request):
    queryset = Article.objects.filter(published=True)
    template_object_name = 'article'
    template_name = 'news/article_list.html'
    extra_context = {
        'publication_list': Publication.objects.all()
    }
    response = list_detail.object_list(
        request,
        queryset=queryset,
        template_object_name=template_object_name,
        template_name=template_name,
        extra_context=extra_context
    )
    return response


def article_detail_view(request, slug):
    queryset = Article.objects.filter(published=True)
    template_object_name = 'article'
    template_name = 'news/article_detail.html'
    response = list_detail.object_detail(
        request,
        queryset=queryset,
        template_object_name=template_object_name,
        template_name=template_name,
        slug=slug
    )
    return response


def publication_detail_view(request, slug):
    queryset = Publication.objects.all()
    response = list_detail.object_detail(
        request,
        queryset=queryset,
        slug=slug
    )
    return response
