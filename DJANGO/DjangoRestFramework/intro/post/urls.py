from django.urls import path, include

app_name = 'post'

urlpatterns = [
    path('api/', include('post.api.urls')),
]
