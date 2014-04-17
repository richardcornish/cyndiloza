from django.contrib import admin

from cyndiloza.apps.places.models import Place, District
from cyndiloza.apps.places.forms import PlaceForm


class DistrictAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state',)
    list_filter = ('city', 'state',)
    prepopulated_fields = {'slug': ('name',)}
    form = PlaceForm
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description', 'url',)
        }),
        ('Location', {
            'fields': ('address', 'city', 'district', 'state', 'zipcode', 'country', 'latitude', 'longitude',)
        }),
        ('Media', {
            'fields': ('photo', 'photo_url', 'photographer', 'photographer_url', 'street',)
        }),
    )


admin.site.register(District, DistrictAdmin)
admin.site.register(Place, PlaceAdmin)
