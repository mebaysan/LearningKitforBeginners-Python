*************Web Sayfası Kaynağını Alma**************
import requests 
from bs4 import BeautifulSoup

url =  "https://yellowpages.com.tr/ara?q=Ankara" # Site linkimiz 

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


print(soup.prettify()) # Daha güzel bir görüntü için prettify() fonksiyonunu kullanıyoruz.






**********Web Sayfasındaki < a > etiketlerini alma**********
import requests 
from bs4 import BeautifulSoup

url =  "https://yellowpages.com.tr/ara?q=Ankara" # Site linkimiz 

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


print(soup.find_all("a")) # Bize tüm <a> etiketlerini liste şeklinde dönüyor.

*****************************< a > etiketlerinin içindeki "href" değerlerini alma********************************
import requests 
from bs4 import BeautifulSoup

url =  "https://yellowpages.com.tr/ara?q=Ankara" # Site linkimiz 

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


for i in soup.find_all("a"):
    print(i.get("href"))
********************************< a > etiketlerinin içindeki yazı değerlerini alma********************************
import requests 
from bs4 import BeautifulSoup

url =  "https://yellowpages.com.tr/ara?q=Ankara" # Site linkimiz 

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.


for i in soup.find_all("a"):
    print(i.text)
************************class değerleri "yp-poi-box-2" olan < div > etiketlerini alma**********************************
import requests 
from bs4 import BeautifulSoup

url =  "https://yellowpages.com.tr/ara?q=Ankara" # Site linkimiz 

response =  requests.get(url) # Web sayfamızı çekiyoruz.

html_icerigi = response.content  # Web sayfamızın içeriğini alıyoruz.

soup =  BeautifulSoup(html_icerigi,"html.parser") # Web sayfamızı parçalamak için BeautifulSoup objesine atıyoruz.

 # Bu kullanımın anlamı div etiketlerinden class'ı yp-poi-box-2 yi al anlamına geliyor.
for i in soup.find_all("div",{"class":"yp-poi-box-2"}):