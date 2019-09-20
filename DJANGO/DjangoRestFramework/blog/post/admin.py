from django.contrib import admin
from .models import Post



class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['id', 'title']
    list_per_page = 25
    search_fields = ['title']

admin.site.register(Post,PostAdmin)
