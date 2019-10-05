from django.shortcuts import render, HttpResponse
from .models import Blog


def posts_list(request):
    posts = Blog.objects.all()
    if (request.GET.get('deneme')):
        get = request.GET.get('deneme')
        return render(request,
                      "blog/posts_list.html", context={
                'posts': posts, 'get': get})
    return render(request,
                  "blog/posts_list.html", context={
            'posts': posts})  # ilk önce zorunlu olarak request'i göndermeliyiz, daha sonra template'i daha sonra contexti. context bir sözlüktür


def post_update(request):
    return HttpResponse("update")


def post_delete(request):
    return HttpResponse("delete")


def post_create(request):
    return HttpResponse("create")
