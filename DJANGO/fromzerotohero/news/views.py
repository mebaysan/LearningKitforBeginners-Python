from django.shortcuts import render, get_object_or_404
from news.models import News


def news_detail(request, pk):
    news = News.objects.all()
    new = get_object_or_404(News, pk=pk)
    new.show += 1
    new.save()
    url = "/news/detail/" + str(new.pk)
    tags = new.tag.split(',')
    comments = new.comment_set.filter(is_published=True)
    context = {
        'news': news,
        'new': new,
        'tags': tags,
        'comments': comments,
        'url':url,
    }
    return render(request, 'front/news_detail.html', context=context)
