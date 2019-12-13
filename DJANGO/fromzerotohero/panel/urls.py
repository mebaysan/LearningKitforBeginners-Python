from django.urls import path
from django.conf.urls import url
from panel import views

app_name = 'panel'

urlpatterns = [
    path('', views.home, name='home'),
]
