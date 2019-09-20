from rest_framework.generics import ListAPIView
from post.models import Post
from .serializers import PostSerializer

class PostListAPIView(ListAPIView): #ListAPIView -> listeleme işleme yapar
    queryset = Post.objects.all() #bütün postları alır
    serializer_class = PostSerializer