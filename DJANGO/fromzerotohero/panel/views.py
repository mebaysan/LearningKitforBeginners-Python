from django.shortcuts import render
from news.models import News


# Create your views here.
def home(request):
    return render(request, 'back/home.html')


def news_list(request):
    news_list = News.objects.all()
    context = {
        'news_list': news_list,
    }
    return render(request, 'back/news_list.html', context=context)
