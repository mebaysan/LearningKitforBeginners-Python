from selenium import webdriver # selenium'dan webdriver'ı dahil ettik
import time

driver = webdriver.Chrome() # driver adında bir nesne oluşturduk.

url = "https://eksisozluk.com/python--109286" # url'i bir değişkene atadık istersek direk driver.get() içine de verebiliriz

driver.get(url) # url'e gidiyoruz
time.sleep(3) # 3 saniye bekliyoruz
elements = driver.find_elements_by_css_selector(".content") # class'ı content olan bütün css selectorları al ve elements adlı değişkene at
for element in elements:  # oluşturduğumuz elements değişkeni içinde geziniyourz
    print(element.text+"\n*************") # her element değişkeninin text özelliğini bastırıyoruz

driver.close() # sayfayı kapatıyoruz