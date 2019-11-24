from django.shortcuts import render, get_object_or_404
from store.models import Product, Category


def home(request, category_slug=None):
    products = None
    category_page = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category_page, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    context = {
        'products': products,
        'category': category_page
    }
    return render(request, 'store/home.html', context=context)


def detail(request):
    return render(request, 'store/detail.html')
