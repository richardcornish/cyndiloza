from django.contrib import admin

from cyndiloza.apps.people.models import Person


class PersonOptions(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'title', 'place',)
    list_filter = ('organization',)
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


admin.site.register(Person, PersonOptions)
