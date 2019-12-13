from django.urls import path
from django.conf.urls import url
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
