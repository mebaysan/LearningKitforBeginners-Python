print(""" Bu ders dosyası Baysan tarafından hazırlanmıştır... """)
print("""

                          Hata Yakalama – try,except,finally

try , except blokları
try ,except bloklarının yapısı şu şekildedir;

try:
 
    Hata çıkarabilecek kodlar buraya yazılıyor.
    Eğer hata çıkarsa program uygun olan except bloğuna girecek.
    Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
except Hata1:
    Hata1 oluştuğunda burası çalışacak.
except Hata2:
    Hata2 oluştuğunda burası çalışacak.


try:
    
    a =  int("324234dsadsad") # Burası ValueError hatası veriyor.
    print("Program burada")
except:                       # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")      # Burası çalışır.
    
print("Bloklar sona erdi")


ÇIKTISI:

	""")
try:
    
    a =  int("324234dsadsad") # Burası ValueError hatası veriyor.
    print("Program burada")
except: # Hatayı belirtmezsek bütün hatalar bu kısma giriyor.
    print("Hata oluştu")  # Burası çalışır.
    
print("Bloklar sona erdi")

print("""
Burada a = int(“324234sadsad”) kodu sıkıntı verdiği için program bu bloktan çıkarak direk except bloğuna girdi ve “Hata oluştu” yazdı. 
try ,except bloğu bitince program ekrana “Bloklar sona erdi” yazdırdı.

**************************************************
try:
    
    a =  int("324234") # Burası normal çalışıyor
    print("Program burada")
except ValueError: # Hatayı belirtirsek ValueError hatası bu kısma giriyor.
    print("Hata oluştu") # Hata olmadığı için çalışmadı.
    
print("Bloklar sona erdi")

BUNUN ÇIKTISINI ALMAYACAĞIZ...
*************************************************

	""")
print("""
Şimdi de 2 adet sıkıntı çıkaran kodumuz bulunsun. Birincisi ZeroDivisionError , diğeri ValueError hatası.

try:
    x = int(input("Sayı1:"))
    y = int(input("Sayı2:")) # Hata burada oluşuyor. ValueError'a bloğuna giriyoruz. 
    print(x / y)
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")


ÇIKTISI:

	""")
try:
    x = int(input("Sayı1:"))
    y = int(input("Sayı2:")) # Hata burada oluşuyor. ValueError'a bloğuna giriyoruz. 
    print(x / y)
except ValueError:
    print("Lütfen inputları doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")

print("""
try:
    d = int(input("Sayı1:"))
    f = int(input("Sayı2:"))
    print(d / f) 
except (ValueError,ZeroDivisionError):
    print("ZeroDivision veya ValueError hatası")

 ÇIKTISI:
	""")
try:
    d = int(input("Sayı1:"))
    f = int(input("Sayı2:"))
    print(d / f) 
except (ValueError,ZeroDivisionError):
    print("ZeroDivision veya ValueError hatası")

print("""
try,except,finally blokları

Bazen programlarımızda her durumda mutlaka çalışmasını istediğimiz kodlar bulunabilir.
Bunun için biz kendi try,except bloklarına ek olarak bir tane finally bloğu ekleyebiliriz. 
finally blokları hata olması veya olmaması durumunda mutlaka çalışacaktır. 
Yapısı şu şekildedir;

try:
 
	Hata çıkarabilecek kodlar buraya yazılıyor.
	Eğer hata çıkarsa program uygun olan except bloğuna girecek.
	Hata oluşursa try bloğunun geri kalanındaki işlemler çalışmayacak.
except Hata1:
	Hata1 oluştuğunda burası çalışacak.
except Hata2:
	Hata2 oluştuğunda burası çalışacak.
finally:
	Mutlaka çalışması gereken kodlar buraya yazılacak.
	Bu blok her türlü çalışacak.
Çıktısını almayacağız. Kolay bir konu.
	""")
print("""
***************************************************************************************************
Hata fırlatmak
Bazen kendi yazdığımız fonksiyonlar yanlış kullanılırsa kendi hatalarımızı üretip Pythonda bu hataları fırlatabiliriz. Bunun içinde raise anahtar kelimesini kullanacağız. 
Hata fırlatma şu şekilde yapılabilmektedir;

raise HataAdı(opsiyonel hata mesajı)


 Verilen string'i ters çevirmek
def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]
    
print(terscevir("Python"))  # Hata vermiyor.
 
 Ancak;
 print(terscevir(12))   -> dersek hata verir ve çıktıyı görelim:


	""")
def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]
print(terscevir(12))