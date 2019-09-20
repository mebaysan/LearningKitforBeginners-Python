from django.urls import path, include
from .views import PostListAPIView,PostDetailAPIView


urlpatterns = [
    path('list', PostListAPIView.as_view(), name="list"),
    path('detail/<slug>', PostDetailAPIView.as_view(), name="detail"),
]
