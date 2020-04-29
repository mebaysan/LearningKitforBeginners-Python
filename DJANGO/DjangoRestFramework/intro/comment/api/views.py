from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, RetrieveUpdateAPIView
from comment.models import Comment
from comment.api.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer
from comment.api.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from comment.api.paginators import CommentPaginator
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentListAPIView(ListAPIView):
    # queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    pagination_class = CommentPaginator

    def get_queryset(self):
        queryset = Comment.objects.filter(parent=None)
        query = self.request.GET.get('q')
        if query:
            queryset = Comment.objects.filter(post=query)
        return queryset


# class CommentDeleteAPIView(DestroyAPIView, UpdateModelMixin):
class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwner]

    # def put(self, request, *args, **kwargs): # bu view'a put isteği gelirse
    #     return self.update(request, *args, **kwargs)


class CommentUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):  # bu view'da hem update hem delete yapabiliriz
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteUpdateSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwner]

    def delete(self, request, *args, **kwargs):  # bu view'da hem update hem delete yapabiliriz
        self.destroy(request, *args, **kwargs)
