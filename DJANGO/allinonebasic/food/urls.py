from django.urls import path
from food import views

urlpatterns = [
    path('', views.index, name="index"),
    path('item/', views.item, name="item"),
    path('detail/<int:id>', views.detail, name="detail"),
]
