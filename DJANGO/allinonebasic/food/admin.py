from django.contrib import admin
from food.models import Item

admin.site.site_header = "Food App All In One Header"  # admin panelde yazan kısmı değiştirir ve admin panele login olurken ki kısmı değiştirir
admin.site.site_title = "Food App All In One Title"  # admin panelde html title'ı değiştirir
admin.site.index_title = "Food App All In One Index Title"  # admin ana sayfadaki kısmı değiştirir


class ItemAdmin(admin.ModelAdmin):
    def change_is_free_to_free(self, request,
                               queryset):  # bu class'a bir action yazıyoruz. request zaten her view'da olduğu gibi gerekli bir parametre
        # queryset ise bizim model nesnelerimizi alır
        queryset.update(is_free=True)  # seçili model nesnelerimize ne yapacaksak yazıyoruz

    change_is_free_to_free.short_description = 'Change To Free'  # action'ın action list penceresinde nasıl gözükeceğini belirtiyoruz
    list_display = ('name', 'is_free')
    actions = ('change_is_free_to_free',)  # bu model için yazdığımız action'ı kayıt ediyoruz


admin.site.register(Item, ItemAdmin)
