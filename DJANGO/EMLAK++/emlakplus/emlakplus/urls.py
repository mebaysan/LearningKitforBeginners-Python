from django.contrib import admin
from django.urls import path, include
#  ========== MEDIA DOSYALARI ICIN =========
from django.conf import settings
from django.conf.urls.static import static
#  ========== MEDIA DOSYALARI ICIN =========
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('account/', include('account.urls')),
    path('contact/', include('contact.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #  ========== MEDIA DOSYALARI ICIN =========
