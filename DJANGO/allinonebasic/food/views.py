from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from food.models import Item


def index(request):
    template = loader.get_template("food/index.html")
    items = Item.objects.all()
    context = {
        'items': items
    }
    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse("<h1>This is item view</h1>")


def detail(request, id):
    item = Item.objects.get(id=id)
    template = loader.get_template('food/detail.html')
    context = {
        'item': item
    }
    return render(request,'food/detail.html',context)