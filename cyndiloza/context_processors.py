from django.conf import settings
from django.contrib.sites.models import get_current_site
from django.contrib.auth import get_user_model


def site(request):
    """
    Gets current website and adds it to the template context.
    """
    return {'site': get_current_site(request)}


def superuser(request):
    """
    Gets first saved user, typically the site owner, and adds him/her to the template context.
    """
    user = get_user_model()
    superuser = user.objects.get(pk=1)

    return {'superuser': superuser}


def map(request):
    """
    Gets the Google Maps API key from settings and adds it to the template context.
    """
    google_maps_key = getattr(settings, 'GOOGLE_MAPS_KEY', '')

    return {'GOOGLE_MAPS_KEY': google_maps_key}


def analytics(request):
    """
    Gets the Google Analytics web property ID from settings and adds it to the template context.
    """
    google_analytics = getattr(settings, 'GOOGLE_ANALYTICS', '')

    return {'GOOGLE_ANALYTICS': google_analytics}
