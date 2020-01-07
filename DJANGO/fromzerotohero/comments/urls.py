from django.urls import path
from comments import views

app_name = 'comments'

urlpatterns = [
    path('list/', views.get_all_comments, name='comment_list'),
    path('add/<int:npk>/', views.add_comment, name='add_comment'),
    path('delete/<int:cpk>/', views.delete_comment, name='delete_comment'),
]
