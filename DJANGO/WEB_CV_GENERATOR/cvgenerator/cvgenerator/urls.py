"""cvgenerator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pdf import views

admin.site.site_header = "Web Based CV Generator Portal"  # admin login / oturum kapat hizasında
admin.site.site_title = "Web Based CV Generator"
admin.site.index_title = "Web Based CV Generator Admin"  # url title / admin index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accept, name='accept'),
]
