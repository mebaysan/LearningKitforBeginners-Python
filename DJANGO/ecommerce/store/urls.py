from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<slug:category_slug>', views.home, name="products_by_category"),
    path('detail/<slug:category_slug>/<slug:product_slug>/', views.detail, name="detail"),
    path('cart', views.cart_detail, name="cart_detail"),
    path('cart/add/<int:product_id>', views.add_cart, name="add_to_cart"),
    path('cart/remove/<int:product_id>', views.cart_remove, name="remove_cart"),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name="remove_product_cart"),
]
