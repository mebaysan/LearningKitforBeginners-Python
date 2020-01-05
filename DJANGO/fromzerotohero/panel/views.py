from django.shortcuts import render, redirect, get_object_or_404
from news.models import News
from category.models import Category
from subcategory.models import SubCategory
from django.core.files.storage import FileSystemStorage
from main.models import Main, ContactForm
from django.http import JsonResponse
from trending.models import Trending
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group, Permission
from users.models import Manager
from django.contrib.contenttypes.models import ContentType


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
                                writer=request.user.username,
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
    news = News.objects.get(pk=pk)
    if request.user.username != news.writer:
        error = "Access Denied!"
        link = request.META.get('HTTP_REFERER')  # bir önceki url'i alır
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    try:
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
                   # news.writer = request.user.username
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
           # news.writer = request.user.username
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


def change_pass(request):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    if request.method == "POST":
        old_pass = request.POST.get('old_pass')
        new_pass = request.POST.get('new_pass')
        user = authenticate(username=request.user.username, password=old_pass)  # user'i auth ediyoruz
        if user != None:  # eğer auth olmazsa demek ki şifresi yanlıştır, olursa şifresi doğrudur
            if len(new_pass) < 3:
                error = "Your new pass < 3 character"
                link = request.META.get('HTTP_REFERER')
                context = {
                    'error': error,
                    'link': link
                }
                return render(request, 'back/error.html', context=context)
            user = User.objects.get(pk=request.user.pk)
            user.set_password(new_pass)
            user.save()
            return redirect('main:my_logout')
        else:
            error = "Your Password Is Not Correct!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
    return render(request, 'back/change_pass.html')


def manager_list(request):
    if not request.user.is_authenticated:
        return redirect('main:my_login')

    managers = Manager.objects.all()
    context = {
        'managers': managers,
    }
    return render(request, 'back/manager_list.html', context=context)


def manager_del(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    if len(request.user.groups.filter(name='Master User')) < 1:
        error = "Access Denied!"
        link = request.META.get('HTTP_REFERER')
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    try:
        manager = Manager.objects.get(pk=pk)
        user = manager.user
        user.delete()
        manager.delete()
        return redirect('panel:manager_list')
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)


def manager_group_list(request):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    # groups = Group.objects.all().exclude(name='Master User')  # exclude bu filtreye uyan objeyi listeden çıkartır
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    return render(request, 'back/manager_group_list.html', context=context)


def manager_group_add(request):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    if request.method == "POST":
        group_name = request.POST.get('group_name')
        if not group_name:
            error = "Please Enter The Group Name!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        elif Group.objects.filter(name=group_name).exists():
            error = "Group name has been used!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        group = Group(name=group_name)
        group.save()
        return redirect('panel:manager_group_list')
    return render(request, 'back/manager_group_add.html')


def manager_group_del(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    try:
        group = Group.objects.get(pk=pk)
        group.delete()
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    return redirect('panel:manager_group_list')


def users_groups(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    user = Manager.objects.get(pk=pk).user
    groups = Group.objects.all()
    context = {
        'user': user,
        'groups': groups,
    }
    return render(request, 'back/users_groups.html', context=context)


def users_groups_delete(request, uid, gid):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    user = User.objects.get(pk=uid)
    group = Group.objects.get(pk=gid)
    user.groups.remove(group)
    return redirect('panel:users_groups', pk=user.manager.pk)


def users_groups_add(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    user = User.objects.get(pk=pk)
    new_group_pk = request.POST.get('group_name')
    new_group = Group.objects.get(pk=new_group_pk)
    user.groups.add(new_group)
    user.save()
    return redirect('panel:users_groups', pk=user.manager.pk)


def permission_list(request):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    if request.method == "POST":
        permission_name = request.POST.get('perm_name')
        permission_code_name = request.POST.get('perm_code_name')
        ctypepk = request.POST.get('ctypepk')
        if len(Permission.objects.filter(name=permission_name)) == 0:
            content_type = ContentType.objects.get(pk=ctypepk)
            permission = Permission.objects.create(codename=permission_code_name, name=permission_name,
                                                   content_type=content_type)
            permission.save()
        else:
            error = "This Permission Name is has been used!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
    permissions = Permission.objects.all()
    content_types = ContentType.objects.all()
    context = {
        'permissions': permissions,
        'content_types': content_types,
    }
    return render(request, 'back/permission_list.html', context=context)


def permission_delete(request, pk):
    try:
        perm = Permission.objects.get(pk=pk)
        perm.delete()
        return redirect('panel:permission_list')
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)


def users_perms(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    user = Manager.objects.get(pk=pk).user
    perms = Permission.objects.filter(user=user)
    all_perms = Permission.objects.all()
    context = {
        'user': user,
        'perms': perms,
        'all_perms': all_perms,
    }
    return render(request, 'back/users_permissions.html', context=context)


def users_perms_delete(request, uid, pid):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    user = User.objects.get(pk=uid)
    perm = Permission.objects.get(pk=pid)
    user.user_permissions.remove(perm)
    return redirect('panel:users_permissions', pk=user.manager.pk)


def users_perms_add(request, uid):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    try:
        user = User.objects.get(pk=uid)
        pid = request.POST.get('perm_pk')
        perm = Permission.objects.get(pk=pid)
        user.user_permissions.add(perm)
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    return redirect('panel:users_permissions', pk=user.manager.pk)


def group_perms(request, pk):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    group = Group.objects.get(pk=pk)
    perms = Permission.objects.filter(group=group)
    all_perms = Permission.objects.all()
    context = {
        'group': group,
        'perms': perms,
        'all_perms': all_perms,
    }
    return render(request, 'back/group_perms.html', context=context)


def group_perms_delete(request, gid, pid):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    group = Group.objects.get(pk=gid)
    perm = Permission.objects.get(pk=pid)
    group.permissions.remove(perm)
    return redirect('panel:group_permissions', pk=group.pk)


def group_perms_add(request, gid):
    if not request.user.is_authenticated:
        return redirect('main:my_login')
    try:
        group = Group.objects.get(pk=gid)
        pid = request.POST.get('perm_pk')
        perm = Permission.objects.get(pk=pid)
        group.permissions.add(perm)
    except:
        error = "Something Wrong!"
        link = request.META.get('HTTP_REFERER')
        context = {
            'error': error,
            'link': link
        }
        return render(request, 'back/error.html', context=context)
    return redirect('panel:group_permissions', pk=group.pk)
