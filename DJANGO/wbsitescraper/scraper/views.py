from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup


def scrape(request):
    if request.method == "POST" and request.is_ajax(): # eğer method post ve istek ajax ise
        site = request.POST.get('scrape_url')  # ajax isteği ile yolladığımız değişken ( bilgiler içindeki scrape_url )
        if site[0:4] != 'http':  # eğer gelen site adı http ile başlamıyorsa hata döndürecek
            data = {
                'success': False
            }
            return JsonResponse(data)
        page = requests.get(site)  # buraya (gelen siteye) bir istek atıyor
        soup = BeautifulSoup(page.text, 'html.parser')  # sayfanın html'i parçalıyor
        links = []
        for link in soup.find_all('a'):  # her a etiketini dolaşıyor
            new_link = {
                'link': link.get('href'),  # href attribute'larını alıyor listeye ekliyor
                'name': link.string, # isimleri alıyor
            }
            links.append(new_link)  # sözlük olarak listeye ekliyoruz
        data = {
            'success': True,
            'links': links,
            'site': site
        }
        return JsonResponse(data)
    return render(request, 'scraper/result.html')
