from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('detail/<int:id>', views.product_detail, name='product_detail'),
]
