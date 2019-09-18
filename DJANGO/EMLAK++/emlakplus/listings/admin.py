from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'price', 'list_date', 'realtor']
    list_display_links = ['id', 'title']
    list_filter = ['realtor']
    list_editable = ['is_published'] # listelenirken editlenebilsin mi
    search_fields = ['title','description','address','state','city','zipcode']
    list_per_page = 25 # bir sayfada en fazla 25 tane olsun dedik


admin.site.register(Listing, ListingAdmin)
