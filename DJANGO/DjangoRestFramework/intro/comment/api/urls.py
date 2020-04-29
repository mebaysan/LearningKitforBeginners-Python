from django.urls import path, include
from comment.api import views

app_name = 'api'

urlpatterns = [
    path('create/', views.CommentCreateAPIView.as_view(), name='create'),
    path('list/', views.CommentListAPIView.as_view(), name='list'),
    path('delete/<int:pk>', views.CommentDeleteAPIView.as_view(), name='delete'),
    path('update/<int:pk>', views.CommentUpdateAPIView.as_view(), name='update')
]
