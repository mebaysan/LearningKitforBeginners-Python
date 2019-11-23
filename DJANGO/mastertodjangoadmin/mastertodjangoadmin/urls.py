from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "Special Admin"  # site url kısmındaki title'ı değiştirir
admin.site.index_title = "Special Admin Panel"  # admin anasayfasındaki header altını değiştirir
admin.site.site_header = "Special Admin Portal"  # login page ve ana sayfadaki kısımları değiştirir
urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),  # grappelli url'i, 3rd party
    path('summernote/', include('django_summernote.urls')),  # summernote kullanmak için gerekli url konfigürasyonu
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),  # secret ile admin panele giriş yapabileceğiz
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
