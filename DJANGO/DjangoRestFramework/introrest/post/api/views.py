from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from post.models import Post
from post.api.serializers import PostSerializer


class PostListAPIView(ListAPIView):  # ListAPIView class'ı listelemeye yarar
    queryset = Post.objects.all()  # bir sorgu belirledik. Kalıp olarak bir ORM sorgu ister
    serializer_class = PostSerializer


class PostDetailAPIView(RetrieveAPIView):  # tek bir değer döndürür (detay çin birebir)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'  # slug'a göre detay sayfasına gideceğimiz için böyle bir şey yaptık. routing gibi düşünebiliriz.


class PostDeleteAPIView(DestroyAPIView):  # silmek için class based
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView):  # güncellemek için class based
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user)  # serializer'ı save ederken bazı işlemleri yapabiliyoruz. form.save(commit=False) gibi

    """
    Postman ile örnek bir post request (http://127.0.0.1:8000/post/api/create/)
    {
    "title": "create api ile eklenen",
    "content": "create api ile eklenen post'un içeriği",
    "image": null
    }
    
    """
