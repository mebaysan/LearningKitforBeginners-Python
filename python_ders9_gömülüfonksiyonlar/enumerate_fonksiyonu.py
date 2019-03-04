print("""
ENUMERATE FONKSİYONU
herbir elemanı indekslerle numaralandırıyor ve 
demet çiftleri oluşturuyoruz. for döngüsü yazarken bazen 
hem elemanları hem de indeksleri almak isteyebiliriz. 
Böyle bir durumda numaralandırma işlemi yapan enumerate fonksiyonunu kullanabiliriz.

ÖRNEK:

liste=["elma","armut","kiraz","portakal"]
print(list(enumerate(liste)))
ÇIKTISI:
	""")
liste=["elma","armut","kiraz","portakal"]
print(list(enumerate(liste)))
print("""
*********************************************************

Örneğin bir listenin çift indekslerini(0,2,4) 
enumerate kullanarak nasıl yazdırabiliriz ? 

liste1 = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste1):
    if (index % 2 == 0):
        print("Eleman: ",eleman)

ÇIKTISI:
	""")
liste1 = ["a","b","c","d","e","f","g"]

for index,eleman in enumerate(liste1):
    if (index % 2 == 0):
        print("Eleman: ",eleman)

print("Yani sadece çift değere sahip olan indexleri bastı")
