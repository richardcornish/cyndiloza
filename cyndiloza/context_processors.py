from django.contrib.sites.models import get_current_site


def site(request):
    """
    Gets current website and adds it to the template context.
    """
    return {'site': get_current_site(request)}
