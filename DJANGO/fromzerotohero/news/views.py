from django.shortcuts import render, get_object_or_404, redirect
from news.models import News
from main.models import Main


def news_detail(request, pk):
    news = News.objects.all()
    new = get_object_or_404(News, pk=pk)
    site = Main.objects.first()
    context = {
        'news': news,
        'site': site,
        'new': new,
    }
    return render(request, 'front/news_detail.html', context=context)
