from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'employee', 'year')
    list_display_links = ('id', 'title')
    list_filter = ('employee',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'make', 'model', 'year', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
