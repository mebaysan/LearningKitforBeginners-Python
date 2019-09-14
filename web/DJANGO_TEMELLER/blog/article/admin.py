from django.contrib import admin
from .models import Article,Comment # admin panelinde göstermek için modeli import ettik
# Register your models here.
#bu uygulamanın admin'de nasıl gözükeceği vs. yer. burası uygulamayı admine bağlar

#admin.site.register(Article) # admine kayıt ettik

@admin.register(Article) # admin panelini özelleştirmek için
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_date'] # neleri göstermek istediğimizi burada belirtiyoruz
    list_display_links = ['title'] # bu özelliklere link verebiliriz.
    search_fields = ['title'] # hangi alanlara göre arama yapılsın
    list_filter = ['created_date'] # hangi field'a göre filtreleme yapılsın
    class Meta: # zorunlu alan Meta olmak zorunda burada modeli admine bağlıyoruz
        model = Article


@admin.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['comment_author','comment_content','comment_date']
    list_display_links = ['comment_content']
    search_fields = ['comment_content']
    list_filter = ['comment_date']
    class Meta:
        model = Article