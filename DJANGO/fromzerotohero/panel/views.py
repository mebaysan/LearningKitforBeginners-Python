from django.shortcuts import render, redirect, get_object_or_404
from news.models import News
from category.models import Category
from subcategory.models import SubCategory
from django.core.files.storage import FileSystemStorage
from main.models import Main, ContactForm
from django.http import JsonResponse
from django.core import serializers
import json
from trending.models import Trending


# Create your views here.
def home(request):
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
    return render(request, 'back/home.html')


def news_list(request):
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
    news_list = News.objects.all()
    context = {
        'news_list': news_list,
    }
    return render(request, 'back/news_list.html', context=context)


def news_add(request):
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
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
        news_tag = request.POST.get('news_tag')
        news_category = SubCategory.objects.get(pk=news_category_id).name
        ocategory_id = SubCategory.objects.get(pk=news_category_id).category_id
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
                                category_name=news_category, category_id=0, show=0, ocategory_id=ocategory_id,
                                tag=news_tag)
                    news.save()
                    count = len(
                        News.objects.filter(ocategory_id=ocategory_id))  # bu kategorideki haber sayısını buluyoruz
                    category = Category.objects.get(pk=ocategory_id)  # kategoriyi seçiyoruz
                    category.count = count  # kategorinin sayısını yeni sayı ile eşitliyoruz
                    category.save()
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
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
    try:
        news = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(news.pic_name)
        ocat_id = News.objects.get(pk=pk).ocategory_id
        news.delete()
        count = len(News.objects.filter(ocategory_id=ocat_id))  # bu kategorideki haber sayısını buluyoruz
        category = Category.objects.get(pk=ocat_id)  # kategoriyi seçiyoruz
        category.count = count  # kategorinin sayısını yeni sayı ile eşitliyoruz
        category.save()
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    return redirect('panel:news_list')


def news_edit(request, pk):
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
    news = News.objects.filter(pk=pk)  # filter olunca bize array döndürür
    if len(news) == 0:  # eğer array'in eleman sayısı 0'a eşitse böyle bir haber yok demektir
        error = "News Not Found!"
        link = '/panel/news/list'
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    news = News.objects.get(pk=pk)
    subcategories = SubCategory.objects.all()
    context = {
        'pk': pk,
        'news': news,
        'subcategories': subcategories,
    }
    if request.method == "POST":
        news_title = request.POST.get('news_title')
        news_category_id = request.POST.get(
            'news_category')  # html formunda selectbox içindeki option value'yi döndürür bize
        news_short_txt = request.POST.get('news_short_txt')
        news_body_txt = request.POST.get('news_body_txt')
        news_tags = request.POST.get('news_tag')
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
            file_name = fs.save(news_file.name, news_file)
            file_url = fs.url(file_name)  # dosyanın uzantısı
            if str(news_file.content_type).startswith('image'):
                if news_file.size < 5000000:
                    news = News.objects.get(pk=pk)
                    fs.delete(news.pic_name)  # güncelleme işleminden önce eski resmi siler
                    news.name = news_title
                    news.short_txt = news_short_txt
                    news.body_txt = news_body_txt
                    news.pic_name = file_name
                    news.pic_url = file_url
                    news.writer = "-"
                    news.category_name = news_category
                    news.category_id = news_category_id
                    news.tag = news_tags
                    news.save()
                    return redirect('panel:news_list')
                else:
                    error = "Your File Is Bigger Than 5MB!"
                    link = request.META.get('HTTP_REFERER')
                    context = {
                        'error': error,
                        'link': link
                    }
                    return render(request, 'back/error.html', context=context)
            else:
                error = "Your File Not Supported!"
                fs.delete(file_name)
                link = request.META.get('HTTP_REFERER')
                context = {
                    'error': error,
                    'link': link
                }
                return render(request, 'back/error.html', context=context)
        except:
            news = News.objects.get(pk=pk)
            news.name = news_title
            news.short_txt = news_short_txt
            news.body_txt = news_body_txt
            news.writer = "-"
            news.category_name = news_category
            news.category_id = news_category_id
            news.tag = news_tags
            news.save()
            return redirect('panel:news_list')
    return render(request, 'back/news_edit.html', context=context)


def category_list(request):
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'back/category_list.html', context=context)


def category_delete(request, pk):
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
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
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
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
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
    subcategories = SubCategory.objects.all()
    context = {
        'subcategories': subcategories
    }
    return render(request, 'back/subcategory_list.html', context=context)


def subcategory_delete(request, pk):
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
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
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
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


def site_settings(request):
    # login kontrol başlangıç
    if not request.user.is_authenticated:  # eğer mevcut kullanıcı authenticate değilse
        return redirect('main:my_login')
    # login kontrol bitiş
    if request.method == "POST" and request.is_ajax():
        site_title = request.POST.get(
            "site_title")  # ajax kısmında nasıl yolluyorsak o isim ile yakalamalıyız. site_settings.js altında 15.satıra bakınız
        site_phone = request.POST.get("site_phone")
        site_facebook = request.POST.get("site_facebook")
        site_twitter = request.POST.get("site_twitter")
        site_youtube = request.POST.get("site_youtube")
        site_link = request.POST.get("site_link")
        site_about = request.POST.get("site_about")
        if not site_facebook: site_facebook = "#"
        if not site_twitter: site_twitter = "#"
        if not site_youtube: site_youtube = "#"
        if not site_link: site_link = "#"
        if not site_title or not site_phone or not site_about:
            error = "All fields required!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        site = Main.objects.first()
        try:
            site_pic = request.FILES['site_pic']  # resmi yakaladık
            fs = FileSystemStorage()
            site_pic_name = fs.save(site_pic.name, site_pic)
            site_pic_url = fs.url(site_pic_name)
            site.name = site_title
            site.about = site_about
            site.facebook_address = site_facebook
            site.twitter_address = site_twitter
            site.youtube_address = site_youtube
            site.phone = site_phone
            site.link = site_link
            site.link_name = site_link
            site.pic_url = site_pic_url
            site.pic_name = site_pic_name
            site.save()  # instance'i save ediyoruz
            data = {
                'success': True
            }
            return JsonResponse(data)
        except:
            site.name = site_title
            site.about = site_about
            site.facebook_address = site_facebook
            site.twitter_address = site_twitter
            site.youtube_address = site_youtube
            site.phone = site_phone
            site.link = site_link
            site.link_name = site_link
            site.save()
            data = {
                'success': True
            }
            return JsonResponse(data)
    site = Main.objects.first()
    context = {
        'site': site,
    }
    return render(request, 'back/settings.html', context=context)


def message_box(request):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    if request.method == "POST" and request.is_ajax():
        if request.POST.get('process') and request.POST.get('process') == "is_it_read":
            pk = request.POST.get('message_pk')
            try:
                message = ContactForm.objects.get(pk=pk)
                message.is_it_read = True
                message.save()
                data = {
                    'success': True,
                    'name': message.name,
                    'email': message.email,
                    'message': message.message,
                }
            except:
                data = {
                    'success': False,
                }
            return JsonResponse(data)
        elif request.POST.get('process') and request.POST.get('process') == 'get_page_data':
            data = {
                'success': True,
                'messages': list(ContactForm.objects.all().values())
            }
            return JsonResponse(data, safe=False)
        elif request.POST.get('process') and request.POST.get('process') == 'delete_message':
            pk = request.POST.get('message_pk')
            try:
                message = ContactForm.objects.get(pk=pk)
                message.delete()
                data = {
                    'success': True,
                }
            except:
                data = {
                    'success': False,
                }
            return JsonResponse(data)
    messages = ContactForm.objects.all()
    context = {
        'messages': messages,
    }
    return render(request, 'back/message_box.html', context=context)


def trends(request):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    trends = Trending.objects.all()
    context = {
        'trends': trends,
    }
    return render(request, 'back/trends.html', context=context)


def trends_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    try:
        trend = get_object_or_404(Trending, pk=pk)
        trend.delete()
        return redirect('panel:trends_list')
    except:
        error = "All fields required!"
        link = request.META.get('HTTP_REFERER')
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)


def trends_update(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    trend = get_object_or_404(Trending, pk=pk)
    context = {
        'trend': trend,
    }
    if request.method == "POST":
        try:
            text = request.POST.get('trend_text')
            publish = request.POST.get('trend_is_published')
            trend.txt = text
            trend.is_publish = publish
            trend.save()
            return redirect('panel:trends_list')
        except:
            error = "Something Wrong!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)

    return render(request, 'back/trends_update.html', context=context)


def trend_add(request):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    if request.method == "POST":
        text = request.POST.get('trend_text')
        publish = request.POST.get('trend_is_published')
        try:
            trend = Trending(txt=text, is_publish=publish)
            trend.save()
        except:
            error = "Something Wrong!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        return redirect('panel:trends_list')
    return render(request, 'back/trends_add.html')
