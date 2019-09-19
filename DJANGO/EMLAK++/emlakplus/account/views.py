from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == "POST":
        # Register User
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'account/register.html')


def login(request):
    if request.method == "POST":
        # Login User
        pass
    else:
        return render(request, 'account/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'account/dashboard.html')
