from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


def register(request):
    # Register User
    if request.method == "POST":
        # Get Form Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check Passwords Match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():  # Username veritabanında kayıtlı ise
                messages.error(request, "That username is taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():  # Email veritabanında kayıtlı ise
                    messages.error(request, "That email is used")
                    return redirect('register')
                else:
                    # Her şey yolunda ise
                    newUser = User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name)
                    newUser.set_password(password) # şifresini hashleyerek yolluyoruz
                    newUser.save() # commit ediyoruz
                    messages.success(request,"You are registered success <3")
                    # Eğer kayıttan hemen sonra kullanıcıya giriş yaptırmak istersek
                    # auth.login(request,newUser)
                    # return redirect('login')
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
    else:
        return render(request, 'account/register.html')


def login(request):
    if request.method == "POST":
        # Login User
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password) # authenticate fonksiyonu ile true gelirse bir user instance oluşacak
        if user is not None: # user instance boş değilse
            auth.login(request,user) # kullanıcıya giriş yaptırıyoruz
            messages.success(request,"You are now logged in")
            return redirect('dashboard')
        else: # user instance boş gelirse
            messages.error(request,'Invalid credentials')
            return redirect("login")
    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request,"You are now logged out")
        return redirect('index')


def dashboard(request):
    return render(request, 'account/dashboard.html')
