from django.urls import path
from django.conf.urls import url
from main import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.my_login, name='my_login'),
    path('logout/', views.my_logout, name='my_logout'),
    path('contact/', views.contact, name='contact'),
]

