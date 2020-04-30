from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from favourite.models import Favourite
from favourite.api.serializers import FavouriteListCreateAPISerializer, FavouriteAPISerializer
from rest_framework.permissions import IsAuthenticated
from favourite.api.permissions import IsOwner
from favourite.api.paginators import FavouritePaginator


class FavouriteListCreateAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListCreateAPISerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = FavouritePaginator

    def get_queryset(self):  # query gelirken
        return Favourite.objects.filter(user=self.request.user)  # o anki oturum açmış user'ın favorileri gelsin

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # save olurken user o anki user olsun


class FavouriteAPIView(RetrieveUpdateDestroyAPIView):  # hem siler, hem günceller
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated, IsOwner]
