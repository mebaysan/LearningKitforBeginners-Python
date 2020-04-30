from django.urls import path, include
from account.api.views import ProfileRetrieveUpdateAPIView, UpdatePasswordAPIView, UserCreateAPIView

app_name = 'api'

urlpatterns = [
    path('me/', ProfileRetrieveUpdateAPIView.as_view(), name='me'),
    path('change-password/', UpdatePasswordAPIView.as_view(), name='change_password'),
    path('create/', UserCreateAPIView.as_view(), name='create'),

]
