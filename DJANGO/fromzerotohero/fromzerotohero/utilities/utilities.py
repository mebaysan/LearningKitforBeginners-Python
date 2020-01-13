from django.urls import get_resolver
from django.urls import reverse


def get_all_urls():
    all_url = get_resolver()  # bütün url'leri aldık
    tum_hepsi = list(all_url.url_patterns)
    tum_hepsi.pop(0)
    """
       aldığımız listenin kopyasını başka bir listeye atıyoruz (8. satır) Sebebi ise;
       eğer direkt olarak all_url.url_patterns.pop(0) yaparsak method bir kere daha çağrıldığında listedeki diğer
       foo.urls'de siliniyor. Ve elimizdeki url'ler silinmeye başlıyor.
       """
    liste = list()
    for url in tum_hepsi:
        # print(url.pattern) # bize url'in başlığını verir. root url'de nasıl tanımladıysak ('panel/'),include('panel.urls')
        for link in url.url_patterns:
            #   print(link.name) # pattern altındaki linkleri(url) gezmeye başladık bu seferde
            new = "{}{}".format(url.pattern, link.name)
            liste.append(new)
    return liste


def get_url_path(app_name, path, **kwargs):
    url = app_name + ':' + path
    if kwargs:
        return reverse(url, kwargs=kwargs)
    return reverse(url)
