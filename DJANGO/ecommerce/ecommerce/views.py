from django.shortcuts import render, get_object_or_404, HttpResponse

def home(request):
    return HttpResponse("<h1>Home</h1>")


def contact(request):
    return HttpResponse("<h1>Contact</h1>")



def register(request):
    return HttpResponse("<h1>Register</h1>")


def login(request):
    return HttpResponse("<h1>Login</h1>")


def about(request):
    return HttpResponse("<h1>About</h1>")



