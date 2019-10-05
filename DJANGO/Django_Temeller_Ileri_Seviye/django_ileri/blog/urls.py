from django.urls import path
from . import views
app_name="blog"
urlpatterns = [
    path('', views.posts_list, name="posts_list"),
    path('post_create/', views.post_create, name="post_create"),
]
