from news.models import News


def get_last_news(request):
    get_last_news = News.objects.all().order_by('-date')[:3]
    return dict(get_last_news=get_last_news)


def get_popular_posts(request):  # bu şekilde tek fonksiyon ile 2 veri seti döndürebiliriz
    get_popular_posts = News.objects.all().order_by('-show')
    get_popular_posts_detail = News.objects.all().order_by('-show')[:3]
    get_popular_posts_home = News.objects.all().order_by('-show')[:3]
    return dict(get_popular_posts=get_popular_posts, get_popular_posts_detail=get_popular_posts_detail,
                get_popular_posts_home=get_popular_posts_home)
