from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from post.models import Post
from post.api.serializers import PostSerializer


class PostListAPIView(ListAPIView):  # ListAPIView class'ı listelemeye yarar
    queryset = Post.objects.all()  # bir sorgu belirledik. Kalıp olarak bir ORM sorgu ister
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):  # tek bir değer döndürür (detay çin birebir)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'  # slug'a göre detay sayfasına gideceğimiz için böyle bir şey yaptık. routing gibi düşünebiliriz.


class PostDeleteAPIView(DestroyAPIView): # silmek için class based
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView): # güncellemek için class based
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
