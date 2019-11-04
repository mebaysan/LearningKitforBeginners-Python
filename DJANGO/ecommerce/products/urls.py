from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('detail/<slug:slug>', views.product_detail, name='product_detail'),
    path('featured_products', views.product_featured_list, name='product_featured_list'),
    path('featured_products/detail/<slug:slug>', views.product_featured_detail, name='product_featured_detail'),
]
