from django.shortcuts import render, redirect
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


def news_add(request):
    if request.method == "POST":
        news_title = request.POST.get('news_title')
        news_category = request.POST.get('news_category')
        news_short_txt = request.POST.get('news_short_txt')
        news_body_txt = request.POST.get('news_body_txt')
        if news_title == "" or news_category == "" or news_short_txt == "" or news_body_txt == "":
            error = "All fields required!"
            link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        news = News(name=news_title, short_txt=news_short_txt, body_txt=news_body_txt, date='2019', pic='-', writer='-',
                    category_name=news_category, category_id=0, show=0)
        news.save()
        return redirect('panel:news_list')
    return render(request, 'back/news_add.html')
