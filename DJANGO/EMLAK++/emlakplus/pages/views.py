from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings
    }
    return render(request, "pages/index.html", context)


def about(request):
    # Get all Realtors
    realtors = Realtor.objects.order_by('-hire_date') #hepsini aldık tutulma tarihlerine göre
    # Get MVP
    mvp_realtors = Realtor.objects.filter(is_mvp=True) #sadece mvp olanları aldık
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, "pages/about.html", context)
