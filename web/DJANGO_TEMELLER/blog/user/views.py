from django.shortcuts import render, redirect
from user import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register(request):
    # 2. VE KOLAY OLAN YOL :)
    form = forms.RegisterForm(
        request.POST or None)  # eğer request methodu POST ise formu posttaki bilgiler ile doldur ama eğer değilse boş kalsın
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Başarıyla kayıt oldunuz")  # eğer başarıyla kayıt olursa request'e mesaj yolluyoruz.
        return redirect("index")
    else:
        context = {
            'form': form
        }
        return render(request, "user/register.html", context)
    """
                            1. YOL
       if request.method == "POST":  # eğer yapılan isteğin tipi post ise
        form = forms.RegisterForm(request.POST)  # formu posttan gelen değerler ile dolduruyoruz
        if form.is_valid():  # is_valid() fonksiyonunu çağırdığımız zaman django otomatik olarak gidip form classındaki celan methoduna bakar
            username = form.cleaned_data.get("username")
            # forms classında hangi key ile döndüysek o isimle almamız gerek
            password = form.cleaned_data.get("password")
            newUser = User(username=username)  # django orm shell kullandığımız gibi(komutlar dosyasında var)
            newUser.set_password(password)  # şifresi şifrelenerek gitsin diye
            newUser.save()
            login(request, newUser)  # sisteme otomatik olarak giriş yapmasını istersek bu fonksiyonu kullanıyoruz
            return redirect("index")  # name fieldı 'index' olan url'e yönlendirdik
        else:
            context = {
                "form": form
            }  # formu yollamak için bir değişken içerisinde yolladık
            return render(request, "user/register.html", context)
    else:  # get ise
        form = forms.RegisterForm()  # arkada yazdığımız form classından bir instance ulaştırdık
        context = {
            "form": form
        }  # formu yollamak için bir değişken içerisinde yolladık
        return render(request, "user/register.html", context)
    """


def login_user(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Kullanıcı adı veya Parola Hatalı")
            return render(request, "user/login.html", context)
        messages.success(request, "Başarıyla Giriş Yaptınız")
        login(request, user)
        return redirect("index")
    return render(request, "user/login.html", context)


def logout_user(request):
    logout(request) # otomatik olarak logout yapar
    messages.success(request,"Başarıyla çıkış yaptınız")
    return redirect("index")
