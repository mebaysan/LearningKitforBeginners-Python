from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render (request,"index.html")

def about(request):
    return render(request,"about.html")