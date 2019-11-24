from django.contrib import admin
from django.db.models import Count

from store.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(comments_count=Count('product'))
        return queryset

    def no_of_products(self, blog):
        return blog.comments_count

    no_of_products.short_description = "Number of products"
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'no_of_products')


class ProductAdmin(admin.ModelAdmin):
    ordering = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
