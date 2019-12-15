from django.shortcuts import render, redirect
from news.models import News
from django.core.files.storage import FileSystemStorage


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

        try:
            news_file = request.FILES['news_file']
            fs = FileSystemStorage()
            file_name = fs.save(news_file.name, news_file)  # dosyanın adı
            file_url = fs.url(file_name)  # dosyanın uzantısı
            if str(news_file.content_type).startswith('image'):  # eğer gelen dosyanın tipi 'image' ile başlıyorsa
                if news_file.size < 5000000:
                    news = News(name=news_title, short_txt=news_short_txt, body_txt=news_body_txt,
                                pic_name=file_name,
                                pic_url=file_url,
                                writer='-',
                                category_name=news_category, category_id=0, show=0)
                    news.save()
                    return redirect('panel:news_list')
                else:
                    error = "Your File Is Bigger Than 5MB!"
                    link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
                    context = {
                        'error': error,
                        'link': link
                    }
                    return render(request, 'back/error.html', context=context)
            else:
                error = "Your File Not Supported!"
                fs.delete(file_name) # eğer desteklenmeyen bir dosya tipi gelirse bunu media/ altından silecek
                link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
                context = {
                    'error': error,
                    'link': link
                }
                return render(request, 'back/error.html', context=context)
        except:
            error = "Please Input Your Image!"
            link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
    return render(request, 'back/news_add.html')


def news_delete(request, pk):
    try:
        news = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(news.pic_name)
        news.delete()
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    return redirect('panel:news_list')
