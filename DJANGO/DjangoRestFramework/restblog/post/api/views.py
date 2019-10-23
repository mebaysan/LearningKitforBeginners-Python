from rest_framework.generics import ListAPIView

from post.models import Post
from post.api.serializers import PostSerializer

class PostListAPIView(ListAPIView): # ListAPIView -> bir şeyleri listelemeye yarar
    queryset = Post.objects.all() # bütün postları yakaladı
    serializer_class = PostSerializer # her modelin bir serializer'ı olmalıdır