from selenium import webdriver  # selenium'dan webdriver'ı dahil ettik
import random  # random sayfalara gitmek istediğimiz için
import time

driver = webdriver.Chrome()  # driver adında bir nesne oluşturduk.

url = "https://eksisozluk.com/python--109286?p="  # kendimizce statik url yapısı oluşturmaya çalışıyoruz
pageCount = 1
entries = list() # entry'leri depolayacağımız listeyi oluşturduk
entryCount = 1
while pageCount <= 10: # bir döngü kurduk ve sayfa sayımız 10'a eşit olduğu sürece dedik
    randomPage = random.randint(1, 96) # random bir sayfa numarası oluşturduk
    newUrl = url + str(randomPage) # yeni url'i eski url sonuna sayfa numarası ekleyerek oluşturduk(bu sitede sayfa route yapısı bu şekilde)
    driver.get(newUrl) # oluşan yeni url'e gittik
    elements = driver.find_elements_by_css_selector(".content") # her sayfada class'ı content olan css selectorları aldık
    for element in elements: 
        entries.append(element.text) # ve her sayfada eelements içindeki element(css).textleri entries listemize taşıdık
    #time.sleep(2) # sayfayı 2 saniye açık beklettik
    pageCount += 1 # her seferinde sayfa sayısını bir artırdık

for entry in entries: # en son entries listemizdeki her entry'i ekrana bastırdık
    print(str(entryCount)+"Entry\n"+entry+"\n**********************")
    entryCount+=1
driver.close()  # sayfayı kapatıyoruz
