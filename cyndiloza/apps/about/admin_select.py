from django.contrib import admin
from django.contrib.auth.models import User


class NiceUserModelAdmin(admin.ModelAdmin):
    """
    In addition to showing a user's username in related fields, show their full
    name too (if they have one and it differs from the username).
    http://djangosnippets.org/snippets/1642/
    """
    always_show_username = True

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        kwargs['initial'] = request.user.id
        field = super(NiceUserModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        if db_field.rel.to == User:
            field.label_from_instance = self.get_user_label
        return field

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super(NiceUserModelAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.rel.to == User:
            field.label_from_instance = self.get_user_label
        return field

    def get_user_label(self, user):
        name = user.get_full_name()
        username = user.username
        if not self.always_show_username:
            return name or username
        return (name and name != username and '%s (%s)' % (name, username) or username)
