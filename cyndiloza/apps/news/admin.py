from django.contrib import admin

from cyndiloza.apps.news.models import *


class PublicationOptions(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


class Favorite_Inline(admin.TabularInline):
    model = Favorite
    extra = 10


class FavoriteOptions(admin.ModelAdmin):
    list_display = ('rank', 'article')


class FavoriteListOptions(admin.ModelAdmin):
    inlines = [Favorite_Inline]
    prepopulated_fields = {'slug': ("title",)}


class ArticleOptions(admin.ModelAdmin):
    list_display = ('headline', 'date', 'published', 'featured',)
    list_filter = ('date', 'publication', 'published', 'featured',)
    prepopulated_fields = {'slug': ('headline',)}
    search_fields = ('headline', 'body',)
    filter_horizontal = ('people',)
    fieldsets = (
        (None, {
            'fields': ('headline', 'slug', 'date', 'author', 'contributors', 'publication', 'url',)
        }),
        ('Content', {
            'fields': ('summary', 'body', 'note',)
        }),
        ('Location', {
            'fields': ('place', 'maptype',)
        }),
        ('Media', {
            'fields': ('photo', 'photo_url', 'caption', 'photographer', 'photographer_url', 'document_title', 'document', 'dipity',)
        }),
        ('Sidebar', {
            'classes': ('collapse',),
            'fields': ('sidebarheadline', 'sidebarcontent',)
        }),
        ('People', {
            'classes': ('collapse',),
            'fields': ('people',)
        }),
        ('Visibility', {
            'classes': ('collapse',),
            'fields': ('published', 'featured',)
        }),
    )
    # js = ('/tiny_mce/tiny_mce.js', '/media/js/textareas.js')


admin.site.register(Author)
admin.site.register(Publication, PublicationOptions)
admin.site.register(Favorite, FavoriteOptions)
admin.site.register(FavoriteList, FavoriteListOptions)
admin.site.register(Article, ArticleOptions)
