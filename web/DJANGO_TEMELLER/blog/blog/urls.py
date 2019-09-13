from django.contrib import admin
from django.urls import path, include
from article import views  # article uygulaması içindeki views dosyasından index methodunu al

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('detail/<int:id>', views.detail, name="detail"),
    # dinamik url tanımladık. int tipinde bir id değişkeni gelecek dedik
    # '' -> ana sayfa demektir php'deki / gibidir. ikinci parametre ise hangi fonksiyonun kullanılacağı, name ile urllerimize isim verebiliriz
    path('articles/', include("article.urls")),
    # eğer url'e articles diye bir şey gelirse sen git article uygulaması içindeki urls dosyasına bak dedik. bu sayede uygulamamızı daha modüler bir hale getiriyoruz
    path('user/', include("user.urls")),
    # yani user ile başlayan urllerin devamını git user klasöründeki urls dosyasından çek dedik

]
