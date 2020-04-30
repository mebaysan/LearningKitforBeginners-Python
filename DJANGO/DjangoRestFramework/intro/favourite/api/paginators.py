from rest_framework.pagination import PageNumberPagination


class FavouritePaginator(PageNumberPagination):
    page_size = 4