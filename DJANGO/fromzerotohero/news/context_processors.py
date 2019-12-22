from news.models import News


def get_last_news(request):
    get_last_news = News.objects.all().order_by('-date')[:3]
    return dict(get_last_news=get_last_news)
