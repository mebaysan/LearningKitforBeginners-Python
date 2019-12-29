from trending.models import Trending
from random import randint


def get_trendings(request):
    trendings = Trending.objects.all().filter(is_publish=True).order_by('?')  # bu sayede random getirdik
    return dict(get_trendings=trendings)
