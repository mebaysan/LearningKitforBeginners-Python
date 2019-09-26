from django.urls import path
from .views import index, allProdCat

app_name = 'shop'
urlpatterns = [
    path('', allProdCat, name="allProdCat"),
    path('<slug:c_slug>/', allProdCat, name='products_by_category')
]
