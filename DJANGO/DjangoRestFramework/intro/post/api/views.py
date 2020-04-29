from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     DestroyAPIView,
    # UpdateAPIView,
                                     RetrieveUpdateAPIView,
                                     CreateAPIView, )
from post.models import Post
from post.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from post.api.permissions import IsOwner
from rest_framework.filters import SearchFilter, OrderingFilter
from post.api.paginators import PostPaginator


class PostListAPIView(ListAPIView):  # listeleme view (http get)
    # queryset = Post.objects.all()  # tüm verileri getir
    serializer_class = PostSerializer
    filter_backends = [SearchFilter,
                       OrderingFilter]  # ?search=AranacakString (restframework'un otomatik kendi fonksiyonu)
    search_fields = ['title']  # title'a göre arama yapacağız
    ordering = 'user'  # istersek burada yapabiliriz, istersek de url'de ?ordering=-user şeklinde arama yapabiliriz
    pagination_class = PostPaginator # ?page=sayfa_no
    def get_queryset(self):  # get_queryset override edersek üstteki queryset'i eklememize gerek yok
        queryset = Post.objects.filter(draft=False)  # filtreleme yaptık
        return queryset


class PostDetailAPIView(RetrieveAPIView):  # detay getirmek için kullanılır (http get)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'  # default olarak pk'dir, fakat biz slug'a göre filtreleme yaptık


class PostDeleteAPIView(DestroyAPIView):  # silmek için kullanılır (http delete)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = 'slug'


# class PostUpdateAPIView(UpdateAPIView):  # güncellemek için kullanılır (http put)
class PostUpdateAPIView(RetrieveUpdateAPIView):  # güncellemek için kullanılır (http put)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)


class PostCreateAPIView(CreateAPIView):  # güncellemek için kullanılır (http post)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # hangi izinleri kullanacağız

    def perform_create(self, serializer):  # override ediyoruz. Instance oluşturulmadan önce
        serializer.save(user=self.request.user)  # serializer'ın user'ını request.user set ettik
