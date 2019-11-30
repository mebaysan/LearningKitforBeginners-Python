from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main
from news.models import News

def home(request):
    site = Main.objects.first()
    news = News.objects.all()
    context = {
        'site': site,
        'news':news
    }
    return render(request, 'front/home.html', context=context)


def about(request):
    site = Main.objects.first()
    context = {
        'site': site
    }
    return render(request, 'front/about.html',context=context)
