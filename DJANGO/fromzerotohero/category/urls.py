from django.urls import path
from category import views

app_name = 'category'

urlpatterns = [
    path('csv/export/', views.export_csv, name="export_csv"),
    path('csv/import/', views.import_csv, name="import_csv"),
]
