from django.shortcuts import render, redirect
from news.models import News
from category.models import Category
from subcategory.models import SubCategory
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
    subcategories = SubCategory.objects.all()
    context = {
        'subcategories': subcategories
    }
    if request.method == "POST":
        news_title = request.POST.get('news_title')
        news_category_id = request.POST.get(
            'news_category')  # html formunda selectbox içindeki option value'yi döndürür bize
        news_short_txt = request.POST.get('news_short_txt')
        news_body_txt = request.POST.get('news_body_txt')
        news_category = SubCategory.objects.get(pk=news_category_id).name
        if news_title == "" or news_category_id == "0" or news_short_txt == "" or news_body_txt == "":
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
                fs.delete(file_name)  # eğer desteklenmeyen bir dosya tipi gelirse bunu media/ altından silecek
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
    return render(request, 'back/news_add.html', context=context)


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


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'back/category_list.html', context=context)


def category_delete(request, pk):
    try:
        cat = Category.objects.get(pk=pk)
        cat.delete()
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    return redirect('panel:category_list')


def category_add(request):
    if request.method == "POST":
        cat_name = request.POST.get('category_name')
        if cat_name == "":
            error = "All fields required!"
            link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        if len(Category.objects.filter(
                name=cat_name)) != 0:  # Daha önce aynı isimle bir kategori eklenmişse hata verecek
            error = "This Name Used Before!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        category = Category(name=cat_name)
        category.save()
        return redirect('panel:category_list')
    return render(request, 'back/category_add.html')


def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    context = {
        'subcategories': subcategories
    }
    return render(request, 'back/subcategory_list.html', context=context)


def subcategory_delete(request, pk):
    try:
        subcat = SubCategory.objects.get(pk=pk)
        subcat.delete()
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    return redirect('panel:subcategory_list')


def subcategory_add(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    if request.method == "POST":
        subcat_name = request.POST.get('subcategory_name')
        subcat_catid = request.POST.get('category')  # html kısmında for ile dönerken category.pk'i alır

        if subcat_name == "" or subcat_catid == "0":
            error = "All fields required!"
            link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        if len(SubCategory.objects.filter(
                name=subcat_name)) != 0:  # Daha önce aynı isimle bir subkategori eklenmişse hata verecek
            error = "This Name Used Before!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        category = Category.objects.get(pk=subcat_catid)
        subcat_catname = category.name
        subcategory = SubCategory(name=subcat_name, category_name=subcat_catname, category_id=subcat_catid)
        subcategory.save()
        return redirect('panel:subcategory_list')
    return render(request, 'back/subcategory_add.html', context=context)
