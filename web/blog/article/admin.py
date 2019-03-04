from django.contrib import admin

# Register your models here.
from .models import Article
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","author","created_date"]
    # list_display_links=[""] içine verdiğin değere link ekler
    search_fields=["title"]
    list_filter=["created_date"]
    class Meta:
        model = Article