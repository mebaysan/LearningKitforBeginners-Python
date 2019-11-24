from django.shortcuts import render



def home(request):
    return render(request,'store/home.html')
def detail(request):
    return render(request,'store/detail.html')