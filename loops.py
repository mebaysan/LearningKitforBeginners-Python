print("Bu ders dosyası Baysan tarafından hazırlanmıştır...")
print("BU DOSYANIN KAYNAK KODLARI KARIŞIK OLDUĞU İÇİN CMD'DE ÇALIŞMAYABİLİR")
#DÖNGÜ YAPILARI
#döngüler işlem tekrar ettirir diyebiliriz aslında.
"""
in Operatörü
Pythondaki in operatörü , bir elemanın başka bir listede,demette veya stringte (karakter dizileri) bulunup bulunmadığını kontrol eder.
"""
print("in operatörü")
print("print(\"4 in [1,2,3])\" ->",4 in [1,2,3])
# 	for DÖNGÜSÜ
print("**********************")
print("for DÖNGÜSÜ")
liste = [1,2,3,4,5,6,7]
 
for eleman in liste:
    print("Eleman",eleman)
  #Liste elemanlarını toplama
  print("*****Liste Elemanlarını Toplama******")
  liste = [1,2,3,4,5,6,7]
toplam = 0
for eleman in liste:
    toplam += eleman
print("Toplam",toplam)

# Çift elemanları bastırma
print("******Çift Elemanları Bastırma*******")
liste = [1,2,3,4,5,6,7,8,9]
 
for eleman in liste:
    if eleman % 2 == 0:
        print(eleman)


#WHILE DÖNGÜSÜ

"""
while döngüleri belli bir koşul sağlandığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder. 
while döngülerinin sona ermesi için koşul durumunun bir süre sonra False olması gereklidir.
"""

# Döngüde i değerlerini ekrana yazdırma
 
i = 0 
 
while (i < 10):
    print("i'nin değeri",i)
    i += 1 # Koşulun bir süre sonra False olması için gerekli - Unutmayalım
 

 # Ekrana 40 defa "Python Öğreniyorum" yazdıralım.
i = 0
 
while (i < 40):
    print("Python Öğreniyorum")
    i +=1


# Liste üzerinde indeks ile gezinme
liste = [1,2,3,4,5]
 
a = 0 
 
while (a < len(liste)):
    print("Indeks:",a,"Eleman:",liste[a])
    a +=1



"""    Sonsuz Döngü Olayları
while döngüsü kullanırken biraz dikkatli olmamızda fayda var. Çünkü, while döngü koşulunun bir süre sonra
 False olması gerekecek ki döngümüz sonlanabilsin. 
Ancak eğer biz while döngülerinde bu durumu unutursak , döngümüz sonsuza kadar çalışacaktır.
 Biz buna sonsuz döngü olayı diyoruz. Örneğimize bakalım.



# Bu kodu çaıştırmayalım.
i = 0 
while (i < 10):
    print(i)
    # i değişkenini artırma işlemi yapmadığımız için i değişkeninin değeri sürekli 0 kalıyor 
    # ve döngü koşulu sürekli True kalıyor.
    """
    

    # range() Fonksiyonu
    """Pythondaki bu hazır fonksiyon bizim verdiğimiz değerlere göre range isimli bir yapı oluşturur
    ve bu yapı listelere oldukça benzer. Bu yapı başlangıç, bitiş ve opsiyonel olarak artırma değeri alarak
     listelere benzeyen bir sayı dizisi oluşturur.
     Kullanımlarını öğrenmeye başlayalım."""

     # print(*range(0,20)) # Yazdırmak için başına "*" koymamız gerekiyor.
 #   liste = list(range(0,20)) # list fonksiyonuyla listeye dönüştürebilir.
 #           print(liste)
 #   print(*range(15)) # Başlangıç değeri vermediğimiz 0'dan başlar
 #   print(*range(5,20,2)) # 5'ten 20'ye kadar olan sayıları 2 atlayarak yazar
 #   print(*range(20,0)) # 20'den geri gelen sayıları oluşturmaz.
 #   print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.
 #   print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.

 """
  for sayı in range(1,20):
    print("* " * sayı)
 Çıktı
 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * * 
* * * * * * * * * * * * * 
* * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * 
 
"""


#BREAK VE CONTINUE İFADELERİ
#BREAK İfadesi
"""
Döngü herhangi bir yerde ve herhangi bir zamanda break ifadesiyle karşılaştığı zaman
çalışmasını bir anda durdurur. Böylelikle döngü hiçbir koşula bağlı kalmadan
break ifadesi sadece ve sadece içindeki bulunduğu döngüyü sonlandırır. Eğer iç içe döngüler bulunuyorsa ve
 en içteki döngüde break kullanılmışsa sadece içteki döngü sona erer.
"""
"""
i = 0 # break kullanmaya çalışalım.
 
while (i < 20):
    print(i)
    if (i == 10):
        break # i'nin değeri 10 olunca bu koşul sağlanıyor ve  break ifadesiyle karşılaşıldığı için döngü anında sona eriyor.
    i +=1
    """
#Continue İfadesi
"""
Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini
yapmadan direk bloğunun başına döner."""
"""
liste = [1,2,3,4,5,6,7,8,9] # continue kullanalım.
 
 
for i in liste:
    if (i == 3 or i == 5):
        continue
    print("i:",i)
"""
# while True:  bu kod herhangi bir yerde break kullanılmamışsa sonsuza kadar çalışır.
#List Comprehension
"""
# Listelerdeki append metodunu hatırlayalım.
liste = [1,2,3,4]
liste.append(5)
 
print(liste)
"""
"""
# liste1'den liste2'yi oluşturalım.
 
liste1 = [1,2,3,4,5]
 
liste2 = list() # veya liste2 = [] ikisi de boş liste oluşturur.
 
 
for i in liste1:
    liste2.append(i) # liste2 'ye liste1 in elemanları for döngüsü yardımıyla atıyoruz.
    
print(liste2)


liste1 = [1,2,3,4,5] # Örnek 1 
 
liste2 = [i for i in liste1] # List Comprehension
 
print(liste2)



**************************
liste1 = [1,2,3,4,5] # Örnek 2
 
liste2 = [i*2 for i in liste1] # List Comprehension
 
print(liste2)
*****************

liste1 = [(1,2),(3,4),(5,6)] # Örnek 3
 
liste2 = [i*j for (i,j) in liste1] # List Comprehension
 
print(liste2)
*************
liste1 = [1,2,3,4,5,6,7,8,9,10] # Örnek 4
 
liste2 = [i for i in liste1 if not (i == 4 or i == 9)] # List Comprehension
 
print(liste2)
"""


print("BİRDAHAKİ DERS DOSYASINDA GÖRÜŞMEK DİLEĞİYLE...")
