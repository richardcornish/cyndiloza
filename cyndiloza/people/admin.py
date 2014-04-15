from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cyndiloza.people.models import Person


class PersonOptions(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'title', 'place',)
    list_filter = ('organization',)
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


admin.site.register(Person, PersonOptions)
