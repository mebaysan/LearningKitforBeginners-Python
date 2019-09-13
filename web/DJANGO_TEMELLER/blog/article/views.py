from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):  # bu değişken her view fonksiyonunda bulunmalı ve ilk parametre olmalı
    # return HttpResponse("RESPONSE DÖNDÜ")
    return render(request, "article/index.html")  # template'a veri gönderirken sözlük yapısı kullanmamız gerekli


# ilk parametre request olmak zorunda ve ikinci parametre templates altındaki hangi dosya olacağı

def about(request):
    return render(request, "article/about.html")


def detail(request, id): # dinamik url oluşturduk, url'e id adında bir değişken gelecek
    return render(request, 'article/detail.html', {'id': id}) # gelen id'yi yolladık
