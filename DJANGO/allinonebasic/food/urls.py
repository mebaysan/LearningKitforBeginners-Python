from django.urls import path
from food import views

app_name = "food"  # <a href="{% url 'food:detail' id=item.id %}"></a> URL'i bu şekilde kullanabilmek için app_name belirlenir

urlpatterns = [
    path('', views.index, name="index"),
    path('item/', views.item, name="item"),
    path('detail/<int:id>', views.detail, name="detail"),
]
