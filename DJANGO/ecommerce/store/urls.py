from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<slug:category_slug>', views.home, name="products_by_category"),
    path('detail/<slug:category_slug>/<slug:product_slug>/', views.detail, name="detail"),
]
