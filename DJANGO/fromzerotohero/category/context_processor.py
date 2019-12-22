from category.models import Category


def get_categories(request):  # template'a direkt veri yolluyor
    get_categories = Category.objects.all()
    return dict(
        get_categories=get_categories)  # get_categories diyerek direkt template'den çağırabiliriz. Sözlük olarak döndürür.
