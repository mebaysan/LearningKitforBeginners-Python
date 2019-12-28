from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main
from news.models import News
from django.contrib.auth import authenticate, login, logout


def home(request):
    news = News.objects.all().order_by('-date')  # büyükten küçüğe sıralar
    context = {
        'news': news,
    }
    return render(request, 'front/home.html', context=context)


def about(request):
    return render(request, 'front/about.html')


def my_login(request):
    if request.method == "POST":
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        if username != "" and password != "":
            user = authenticate(username=username, password=password)  # user'i doğruladık
            if user != None:  # eğer user nesnesi varsa
                login(request, user)  # login yaptık
                return redirect('panel:home')
    return render(request, 'front/login.html')


def my_logout(request):
    logout(request)
    return redirect('main:my_login')
