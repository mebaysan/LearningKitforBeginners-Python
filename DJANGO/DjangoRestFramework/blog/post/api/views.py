from rest_framework.generics import ListAPIView, RetrieveAPIView
from post.models import Post
from .serializers import PostSerializer


class PostListAPIView(ListAPIView):  # ListAPIView -> listeleme işleme yapar
    queryset = Post.objects.all()  # bütün postları alır
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):  # detay sayfası için
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
