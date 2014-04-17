from django.views.generic import ListView, DetailView

from cyndiloza.apps.news.models import Article, Publication


class ArticleDetailView(DetailView):
    queryset = Article.objects.filter(published=True)

article_detail = ArticleDetailView.as_view()


class ArticleListView(ListView):
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['publication_list'] = Publication.objects.all()
        return context

article_list = ArticleListView.as_view()


class PublicationDetailView(DetailView):
    model = Publication

publication_detail = PublicationDetailView.as_view()
