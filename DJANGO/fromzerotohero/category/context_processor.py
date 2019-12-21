from category.models import Category


def footer_categories(request):  # template'a direkt veri yolluyor
    footer_categories = Category.objects.all()
    return dict(
        footer_categories=footer_categories)  # footer_categories diyerek direkt template'den çağırabiliriz. Sözlük olarak döndürür.
