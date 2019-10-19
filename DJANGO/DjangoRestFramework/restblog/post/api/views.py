from rest_framework.generics import ListAPIView

from post.models import Post


class PostListAPIView(ListAPIView): # ListAPIView -> bir şeyleri listelemeye yarar
    queryset = Post.objects.all()