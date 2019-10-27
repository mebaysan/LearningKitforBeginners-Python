from django.shortcuts import render, get_object_or_404
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
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(req, 'products/product_detail.html', context=context)
