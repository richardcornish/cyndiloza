from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cyndiloza.about.models import About
from cyndiloza.about.admin_select import NiceUserModelAdmin


class AboutOptions(NiceUserModelAdmin):
    list_display = ('user',)
    fieldsets = (
        (None, {
            'fields': ('user', 'body', 'photo', 'resume',)
        }),
    )

admin.site.register(About, AboutOptions)
