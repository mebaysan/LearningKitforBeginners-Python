from django.urls import path
from post.api import views

app_name = 'post_api'  # url yönlendirmeleri yaparken işimizi çok kolaylaştırır

urlpatterns = [
    path('list/', views.PostListAPIView.as_view(), name='list'),
    path('detail/<slug:slug>/', views.PostDetailAPIView.as_view(), name='detail'),
    path('delete/<slug:slug>/', views.PostDeleteAPIView.as_view(), name='delete'),
    path('update/<slug:slug>/', views.PostUpdateAPIView.as_view(), name='update'),
    path('create/', views.PostCreateAPIView.as_view(), name='create'),
]
