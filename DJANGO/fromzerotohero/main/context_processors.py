from main.models import Main


def get_site_settings(request):
    site = Main.objects.first()
    return dict(site_settings=site)
