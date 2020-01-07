from django.urls import path
from comments import views

app_name = 'comments'

urlpatterns = [
    path('list/', views.get_all_comments, name='comment_list'),
    path('add/<int:npk>/', views.add_comment, name='add_comment'),
    path('delete/<int:cpk>/', views.delete_comment, name='delete_comment'),
    path('publish/<int:cpk>/', views.publish_comment, name='publish_comment'),
    path('draft/<int:cpk>/', views.draft_comment, name='draft_comment'),
]
