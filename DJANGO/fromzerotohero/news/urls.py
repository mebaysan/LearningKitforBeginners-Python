from django.urls import path
from django.conf.urls import url
from news import views

app_name = 'news'

urlpatterns = [
    path('news/<int:pk>', views.news_detail, name='news_detail'),
    path('panel/news/list', views.news_list, name='news_list'),
]
