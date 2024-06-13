from django.contrib import admin
from .models import Link



admin.site.site_header = "Link Stash Administration"
admin.site.site_title = "Link Stash Admin"


class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'time_saved', 'id',)

    search_fields = ('title__icontains', 'url__icontains', 'time_saved__icontains', 'id__icontains',)

    list_filter = ('time_saved',)

    ordering = ('-time_saved', 'id', 'title', 'url',)

admin.site.register(Link, LinkAdmin)
