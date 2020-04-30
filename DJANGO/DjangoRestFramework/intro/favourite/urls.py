from django.urls import path, include

app_name = 'favourite'

urlpatterns = [
    path('api/', include('favourite.api.urls')),
]
