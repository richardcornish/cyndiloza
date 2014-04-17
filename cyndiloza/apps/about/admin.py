from django.contrib import admin

from cyndiloza.apps.about.models import About
from cyndiloza.apps.about.admin_select import NiceUserModelAdmin


class AboutOptions(NiceUserModelAdmin):
    list_display = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'body', 'photo', 'resume',)
        }),
    )

admin.site.register(About, AboutOptions)
