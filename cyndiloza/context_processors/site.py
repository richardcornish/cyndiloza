from django.template import RequestContext
from django.contrib.sites.models import Site


def get_site(request):
    return {
        'site': Site.objects.get_current()
    }
