print("Bu ders notları Baysan tarafından hazırlanmıştır...")
#MANTIKSAL DEĞERLER VE KARŞIŞALTIRMA OPERATÖRLERİ
#Mantıksal Değerler (Boolean)
print("Mantıksal Değerler (Boolean)")
a=True
print("a=True için type(a)\n->",type(a))
b=False
print("b=False için type(b)\n->",type(b))
#Python'da sayı 0dan farklı ise true,0 ise false.
# bool(*) yıldızlı yere sayı gelir.
print("////////////////")
print("bool() örnekleri")
print("bool(15)->{}\nbool(0)->{}".format(bool(15),bool(0)))
print("Ve ayrıca yukarıda formatlama sistemini kullandık bunun için kaynak kodlara daha detaylı bakabilirsin.")
#Bir değişken atamak istiyoruz fakat daha değerini belirlemediysek None komutu kullanabiliriz-> c=None 
print("////////////")
print("None eşiti")
c=None
print("c=None için,print(\"c\")\n->",c)
"""
KARŞILAŞTIRMA OPERATÖRLERİ
== iki değer birbirine eşitse true,değilse false döner.
!= iki değer birbirine eşit değilse true,değilse false döner.
> soldaki değer sağdaki değerden büyükse true,değilse false döner.
< soldaki değer sağdaki değerden küçükse true,değilse false döner.
>= soldaki değer sağdaki değerden büyük veya eşitse true,değilse false döner.
<= soldaki değer sağdaki değerden küçükse veya eşitse true,değilse false döner.
"""
print("**************************")
print("Karşılaştırma Operatörleri")
print("12==12 için\n->",12==12)
print("Bunu çok açıklamayacağım matematikte bildiğimiz olaylar.Tek farkı bunu sadece sayılara değil aynı zamanda stringlere de uygulayabiliriz.Sözlük sırasına göre bakar.")

#Mantıksal Bağlaçlar
print("*****************")
print("MANTIKSAL BAĞLAÇLAR")
"""
Mantıksal Bağlaçlar
Mantıksal bağlaçlar daha çok karşılaştırma işlemini kontrol ettiğimiz zamanlarda kullanılır. Bu konuda bunları öğrenmeye çalışacağız.

and Operatörü
Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonucunun True olmasına bakar. Bağlanan karşılaştırma işlemlerinin hepsinin kendi içinde sonucu True ise genel sonuç True , diğer durumlarda ise sonuç False çıkar.

İşlemlerin birinin bile sonucu False ise genel işlemin sonucu False çıkmaktadır.

or Operatörü
Bu mantıksal bağlaç, bütün karşılaştırma işlemlerinin sonuçlarından en az birinin True olmasına bakar. Bağlanan karşılaştırma işlemlerinin en az birinin Trueolmasında genel sonuç True , diğer durumlarda ise sonuç False çıkar.

not operatörü
not operatörü aslında bir mantıksal bağlaç değildir. Bu operatör sadece bir mantıksal değeri veya karşılaştırma işlemininin tam tersi sonuca çevirir. Yani, not operatörü True olan bir sonucu False , False olan bir sonucu True sonucuna çevirir. 
"""
print("**************")
print("Koşullu durumlar if-else")
"""
if (koşul): 
    # if bloğu - Koşul sağlanınca (True) çalışır. Bu hizadaki 
    # her işlem bu if bloğuna ait.
    # if bloğu - Girintiyle oluşturulur.
    # Yapılacak İşlemler

if bloğu eğer koşul sağlanırsa anlamı taşır. Eğer if kalıbındaki koşul sağlanırsa (True) if bloğu çalıştırılır, koşul sağlanmazsa (False) if bloğu çalıştırılmaz.


"""
print("if İle Basit bir uyarı programı burayı kaynak kodlarda daha detaylı açıkladım")
a=int(input("Yaşınızı Giriniz:"))
if (a<18):
	print("Daha 18 olmamışsın la bebe")
	pass         # -> pass kullanmak zorunda değilsin. sublime text kendisi koyuyor otomatik.
else:
	print("18 oldun adam mı oldun bebe")
	

print("************************************")	
print("\n\n\nif-elif-else blokları") # elif-> elseif'in kısaltması
"""
if-elif-else Blokları

Önceki konumuzda koşullu durumlarımızla sadece tek bir koşulu kontrol edebiliyorduk. Ancak programlamada bir durum bir çok koşula bağlı olabilir. Örneğin bir hesap makinesi programı yazdığımızda kullanıcının girdiği işlemlere göre koşullarımızı belirleyebiliriz. Bu tür durumlar için if-elif-else kalıplarını kullanırız. Kullanımı şu şekildedir;

Python

if koşul: 
    Yapılacak İşlemler
elif başka bir koşul:
     Yapılacak İşlemler
elif başka bir koşul:
     Yapılacak İşlemler

        //
        //
else:
     Yapılacak İşlemler

if koşul: 
    Yapılacak İşlemler
elif başka bir koşul:
     Yapılacak İşlemler
elif başka bir koşul:
     Yapılacak İşlemler
 
        //
        //     -> istedğini kadar elif kullanabilirsin.
else:
     Yapılacak İşlemler
Programlarımızda, Kaç tane koşulumuz var ise o kadar elif bloğu oluşturabiliriz. Ayrıca else in yazılması zorunlu değildir. if – elif – else kalıplarında, hangi koşul sağlanırsa program o bloğu çalıştırır ve if-elif-blokları sona erer.
"""
işlem=input("İşlem giriniz:")
if (işlem=="1"):
	print("işlem 1 seçildi")
	pass
elif işlem=="2":                 # -> mutlaka alt satırına bir tab boşluk bırak.Yani altına girinti oluşturup blok oluştur yoksa syntax hatası verir.
	print("İşlem 2 seçildi")
elif (işlem=="3"):
	print("İşlem 3 seçildi")     # -> parantez kullanmak zorunda değilsiniz koşul kısmında ister kullanın ister kullanmayın.Ben karışıklık olmasın diye kullanmayı tercih ediyorum.
elif (işlem=="4"):
	print("İşlem 4 seçildi")
else:
	print("Yanlış işlem seçtiniz/İşlem bulunamadı")

print("*********************")
print("\n\n\nNot Programı deneme")
note=float(input("Notunuzu Giriniz:"))
if (note>=90):
	print("AA")
	pass
elif (note>=85):
	print("BA")
elif (note>=80):
	print("BB")
elif (note>=75):
	print("CB")
elif (note>=70):
	print("CC")
elif (note<70):
	print("KALDIN!")

print("******************************")
print("\n\n\n\tBU DERS NOTUMUZUN DA SONUNA GELDİK. DİĞER NOTLARDA GÖRÜŞMEK ÜZERE.")