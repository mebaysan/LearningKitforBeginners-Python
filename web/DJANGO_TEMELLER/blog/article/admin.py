from django.contrib import admin
from .models import Article # admin panelinde göstermek için modeli import ettik
# Register your models here.
#bu uygulamanın admin'de nasıl gözükeceği vs. yer. burası uygulamayı admine bağlar

#admin.site.register(Article) # admine kayıt ettik

@admin.register(Article) # admin panelini özelleştirmek için
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_date'] # neleri göstermek istediğimizi burada belirtiyoruz
    list_display_links = ['created_date'] # bu özelliklere link verebiliriz.
    search_fields = ['title'] # hangi alanlara göre arama yapılsın
    list_filter = ['created_date'] # hangi field'a göre filtreleme yapılsın
    class Meta: # zorunlu alan Meta olmak zorunda burada modeli admine bağlıyoruz
        model = Article