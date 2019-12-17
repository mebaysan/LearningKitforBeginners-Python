from django.urls import path
from panel import views

app_name = 'panel'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/list', views.news_list, name='news_list'),
    path('news/add', views.news_add, name='news_add'),
    path('news/delete/<int:pk>', views.news_delete, name='news_delete'),
    path('category/delete/<int:pk>', views.category_delete, name='category_delete'),
    path('category/list/', views.category_list, name='category_list'),
    path('category/add/', views.category_add, name='category_add'),
    path('subcategory/delete/<int:pk>', views.subcategory_delete, name='subcategory_delete'),
    path('subcategory/list/', views.subcategory_list, name='subcategory_list'),
    path('subcategory/add/', views.subcategory_add, name='subcategory_add'),
]
