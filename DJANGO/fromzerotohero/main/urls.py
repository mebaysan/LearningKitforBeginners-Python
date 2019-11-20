from django.urls import path
from django.conf.urls import url
from main import views

app_name = 'main'

urlpatterns = [
    url('', views.home, name='home'),
]
