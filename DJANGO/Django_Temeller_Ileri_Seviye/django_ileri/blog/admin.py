from django.contrib import admin
from .models import Blog


# Register your models here.

# admin.site.register(Blog) # modelimize admin panelimizde görüntülemek için kayıt ettik
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date','slug']  # neleri göstermek istediğimizi burada belirtiyoruz
    list_display_links = ['title']  # bu özelliklere link verebiliriz.
    search_fields = ['title']  # hangi alanlara göre arama yapılsın
    list_filter = ['created_date']  # hangi field'a göre filtreleme yapılsın



admin.site.register(Blog, BlogAdmin)
