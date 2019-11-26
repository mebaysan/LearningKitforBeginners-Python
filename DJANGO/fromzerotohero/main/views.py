from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main


def home(request):
    return render(request, 'front/home.html')


def about(request):
    return render(request, 'front/about.html')
