from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import bedroom_choices, price_choices, state_choices


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)  # hangi obje üzerinde pagination yapacak ve sayfa başına kaç tane gösterecek
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    context = {
        'state_choices': state_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices
    }
    return render(request, 'listings/search.html', context)
