from django.urls import path, include

from post.api.views import PostListAPIView

urlpatterns = [
    path('list/', PostListAPIView.as_view(), name="list"),
]
