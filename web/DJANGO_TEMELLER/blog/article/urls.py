from django.urls import path
from article import views

app_name = "article"  # burası bizim için açıklayıcı olmalı
urlpatterns = [
    path('create/', views.index, name="index"),
]
