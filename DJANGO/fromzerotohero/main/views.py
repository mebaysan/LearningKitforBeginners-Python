from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main


def home(request):
    site = Main.objects.first()
    context = {
        'site': site
    }
    return render(request, 'front/home.html', context=context)


def about(request):
    site = Main.objects.first()
    context = {
        'site': site
    }
    return render(request, 'front/about.html',context=context)
