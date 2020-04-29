from rest_framework.pagination import PageNumberPagination


class PostPaginator(PageNumberPagination):
    page_size = 2 # her sayfada kaç adet olacak,