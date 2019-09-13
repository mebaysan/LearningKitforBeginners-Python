from django.urls import path
from article import views

app_name = "article"  # burası bizim için açıklayıcı olmalı
urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addarticle/', views.add_article, name="add_article"),
    path('update/<int:id>', views.update_article, name="update"),
    path('delete/<int:id>', views.delete_article, name="delete"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('', views.articles, name="articles"),
]
