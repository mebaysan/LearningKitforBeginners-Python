from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request): # bu değişken her view fonksiyonunda bulunmalı ve ilk parametre olmalı
   # return HttpResponse("RESPONSE DÖNDÜ")
     return render(request,"article/index.html")
   # ilk parametre request olmak zorunda ve ikinci parametre templates altındaki hangi dosya olacağı
