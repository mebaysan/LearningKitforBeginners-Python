from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__','slug')
    readonly_fields = ('slug',)
    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin)