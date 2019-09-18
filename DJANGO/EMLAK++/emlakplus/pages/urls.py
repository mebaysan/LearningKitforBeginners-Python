from django.urls import path
from . import views  # bu dizindeki views'i dahil ettik

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

]
