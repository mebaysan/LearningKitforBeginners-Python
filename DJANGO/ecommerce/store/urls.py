from django.urls import path
from store import views
app_name = "store"

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/', views.detail, name="detail"),
]
