from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('', views.posts_list, name="posts_list"),
    path('post_create/', views.post_create, name="post_create"),
    path('post_detail/<slug:slug>', views.post_detail, name="post_detail"),  # id parametresi alacağını belirttik
    path('post_update/<slug:slug>', views.post_update, name="post_update"),
    path('post_delete/<slug:slug>', views.post_delete, name="post_delete"),
]
