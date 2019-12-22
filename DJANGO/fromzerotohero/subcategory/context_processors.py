from subcategory.models import SubCategory


def get_subcategories(request):
    get_subcategories = SubCategory.objects.all()
    return dict(get_subcategories=get_subcategories)
