from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from products.models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_context_data(self, *args, **kwargs):  # Her class based views bu fonksiyona sahip olmalıdır
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        # print(context)
        return context


def product_detail(req, id):
    try:
        # product = get_object_or_404(Product, id=id)  # Product modeli üstünde id'e göre arama yapılacak
        product = Product.objects.get(
            id=id)  # Product modeli üstünde id'e göre getirecek. Id bulunamazsa bize Product.DoesNotExist hatası verecek
    except Product.DoesNotExist:
        return HttpResponse("<h1> {} Id'li Ürün Bulunamadı!</h1>".format(
            id))  # istersek burda bir template döndürebiliriz. Böylece kendi 404 sayfamızı yazmış olduk
    context = {
        'product': product
    }
    return render(req, 'products/product_detail.html', context=context)


def product_featured_list(req):
    products = Product.objects.filter(featured=True)
    context = {
        'products': products
    }
    return render(req, "products/product_featured_list.html", context=context)


def product_featured_detail(req, id):
    try:
        product = Product.objects.get(id=id, featured=True) # id'si get'ten gelen product ve featured=True ise
    except Product.DoesNotExist:
        return HttpResponse("<h1>{} Id'li Ürün Bulunamadı veya Featured Değil</h1>".format(id))
    context = {
        'product': product
    }
    return render(req, 'products/product_featured_detail.html', context=context)
