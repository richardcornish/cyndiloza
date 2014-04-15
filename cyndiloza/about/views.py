from django.views.generic import list_detail
from cyndiloza.about.models import About


def about_detail_view(request):
    queryset = About.objects.all()
    template_object_name = 'about'
    template_name = 'about/about_detail.html'
    response = list_detail.object_detail(
        request,
        queryset=queryset,
        object_id=1,
        template_object_name=template_object_name,
        template_name=template_name
    )
    return response
