from django.contrib import admin

from cyndiloza.apps.about.models import About
from cyndiloza.apps.about.admin_select import NiceUserModelAdmin


class AboutOptions(NiceUserModelAdmin):
    list_display = ('full_name',)
    fieldsets = (
        (None, {
            'fields': ('user', 'blurb', 'body', 'photo', 'resume',)
        }),
    )

    def full_name(self, obj):
        return obj.user.get_full_name()
    full_name.admin_order_field = 'user__full_name'

admin.site.register(About, AboutOptions)
