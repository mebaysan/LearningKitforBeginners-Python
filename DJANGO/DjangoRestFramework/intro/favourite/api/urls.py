from django.urls import path, include
from favourite.api import views

app_name = 'api'

urlpatterns = [
    path('list-create/', views.FavouriteListCreateAPIView.as_view(), name='list_create'),
    path('update-delete/<int:pk>', views.FavouriteAPIView.as_view(), name='update_delete'),
]
