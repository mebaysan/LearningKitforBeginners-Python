print("Bu ders dosyası Baysan tarafından hazırlanmıştır...")
print("""
****************************
             METODLAR	

Metod nedir ?
Şimdiye kadar Pythonda kullanabildiğimiz bir çok veri tipi gördük ve 
bazı veritipleri üzerinde bu veritiplerinin metodlarını kullandık. 
Aslında bu veritiplerin oluşturulan her bir değişken Pythonda obje( object) olarak düşünülür
ve Python geliştiricileri bu objelere birçok metod tanımlamıştır. Peki nedir bu metodlar ?

Metodlar bir obje üzerinde belli işlemleri gerçekleştiren objelere özgü fonksiyonlardır
 ve objelerin üzerinde metodlar şu şekilde kullanılır.

obje.herhangi_bir_metod(değerler(opsiyonel))
Örneğin bir liste objesi oluşturduğumuz zaman bu objenin
üzerinde belli metodları uygulayabiliriz.

liste=[1,2,3,4,5]
liste.insert(1,"Baysan")
print(liste)
	""")
#insert() metodu içine verdiğimiz ilk parametreden sonra verdiğimiz ikinci parametreyi objeye ekler.
liste=[1,2,3,4,5]
liste.insert(1,"Baysan")
print(liste)
print("**********************************")
print("""
                  FONKSİYONLAR


Python geliştiricilerin yazdığı fonksiyonlara yani bizim hazır kullandığımız fonksiyonlara(print(),type() vs.) gömülü fonksiyonlar(built-in function) denilmektedir.
Ancak bunlardan hariç olarak biz kendi özel fonksiyonlarımızı(user-defined functions) da tanımlayabiliriz.
Fonksiyonlar bizim gereksiz kod tekrarı yapmamamızı sağlar.
Fonksiyonlar şu şekilde tanımlanır:
def fonksiyon_adı(parametre1,parametre2..... (opsiyonel)):
    # Fonksiyon bloğu
    Yapılacak işlemler
    # dönüş değeri - Opsiyonel

   Selamla isimli bir fonksiyon tanımlayalım;
   def selamla():
   	print("Selamunaleyküm...")
   	print("Nasılsınız?")
	""")
def selamla():
	print("Selamunaleyküm...")
	print("Nasılsınız...")
print("""
Fonksiyonumuzu tanımladık şimdi de python'da type fonksiyonu ile daha detaylı görelim;
print(type(selamla))
	""")
print(type(selamla))
print("*****************************")
print("""
                    FONKSİYONLARIN KULLANILMASI	
Tanımlanan bir fonksiyonun kullanılmasına programlama dillerinde Fonksiyon Çağrısı denmektedir. 
O halde selamla fonksiyonumuzu nasıl çağıracağımızı öğrenelim. Fonksiyon çağrısı şu şekilde yapılabilmektedir;
fonksiyon_adı(Argüman1,Argüman2....)  -> fonksiyon çağırmak için

selamla()                              ->Fonksiyon parametre almadığında içine argümanlarımızı göndermiyoruz.
""")
selamla()
print("""
	Burada gördüğünüz gibi, fonksiyonumuz çağrıldığı zaman, kendi bloğundaki işleri yaptı 
	ve ekrana 2 tane değer yazdırdı. Bu fonksiyonu istediğimiz yerde tekrar tekrar çağırabiliriz.

selamla()
selamla()
selamla()  

""")
selamla()
selamla()
selamla()
print("**************************")
print("""
Peki fonksiyonumuzu içine değer verirsek ne olur?
selamla("Enes")
Bu selamla fonksiyonunun içine değer vermediğimiz için çalışmaz ve hata verir.
	""")
print("""***************************************
	                  Parametreler ve Argümanlar

Biliyorsunuz biz selamla fonksiyonunun içine herhangi bir değer göndermiyorduk ve fonksiyonumuz hep aynı işi yapıyordu. 
Ancak çoğu zaman fonksiyonlarımız içine gönderdiğimiz değerlerle farklı işlemler yaparlar.
Örneğin katı meyve sıkacağına eğer “Elma” verirsek elma suyu, “Nar” verirsek nar suyu hazırlayacaktır. 
Fonksiyonlarda da Parametreleri bu şekilde düşünebilirsiniz.
İsterseniz şimdi selamlama fonksiyonumuzu bir tane parametre alacak şekilde tanımlayalım

def selamla1(isim):          -> isim değişkenimiz burada parametre olmaktadır
	print("Merhaba",isim)
selamla1("Baysan")           -> "Baysan" değeri burda argüman olmaktadır.
selamla1("Kardeşim")         -> "Kardeşim" değeri burda argüman olmaktadır.
Çıktısı:
	""")
def selamla1(isim):
	print("Merhaba",isim)
selamla1("Baysan")
selamla1("Kardeşim")
print("""


Bizim fonksiyon tanımlarken tanımladığımız herbir değişken birer Parametre ,
fonksiyon çağrısı yaptığımız zaman içine gönderdiğimiz değerler ise Argümanolmaktadır. 
Burada fonksiyonu çağırırken gönderdiğimiz “Kemal” değeri “isim” isimli parametreye eşit oluyor 
ve fonksiyonumuz bu değere göre işlem yapıyor. “Ayşe” değerini gönderdiğimizde ise fonksiyonumuz bu değere göre işlem yaparak ekrana farklı bir değer yazdırıyor. 
Şimdi isterseniz farklı bir fonksiyon tanımlayalım ve 3 tane parametre alsın.

def toplama(a,b,c):
	print("Toplamları:",a+b+c)
toplama(3,4,5)
toplama(23,12,3)

Çıktısı :
	""")
def toplama(a,b,c):
	print("Toplamları:",a+b+c)
toplama(3,4,5)
toplama(23,12,3)
print("******************")
print("""
Şimdi de örnek olması için bir sayının faktoriyelini tanımlayan bir fonksiyon yazalım:
# Eğer sayımız “5” ise faktoriyel 5 x 4 x 3 x 2 x 1 = 120 olacaktır

faktoriyel için fonksiyon:
def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel",faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel *= sayı
            sayı -=1
        print("Faktoriyel", faktoriyel)
faktoriyel(5)
faktoriyel(6)
faktoriyel(3)
faktoriyel(1)
faktoriyel(0)

ÇIKTISI:

""")
def faktoriyel(sayı):
    faktoriyel = 1
    if (sayı == 0 or sayı == 1):
        print("Faktoriyel",faktoriyel)
    else:
        while (sayı >= 1):
            faktoriyel *= sayı
            sayı -=1
        print("Faktoriyel", faktoriyel)
faktoriyel(5)
faktoriyel(6)
faktoriyel(3)
faktoriyel(1)
faktoriyel(0)
print("*******************************************************************")
print("""

                       FONKSİYONLARDA RETURN
Bu konuda fonksiyonlardan değer döndürmemizi sağlayan return ifadesini görmeye çalışacağız. 
Önceki bölümde yazdığımız fonksiyonları hatırlayacak olursak, bu fonksiyonlar sadece ekrana print ile değer yazdırıyordu. 
Ancak bu fonksiyonlar yaptıklar işlemler bize herhangi bir değer vermiyorlardı. 
Ancak biz programlarımızda bir fonksiyon sonucunda elde edilen değerleri alıp programlarımızın bambaşka yerlerinde kullanmak isteyebiliriz. 
Bu derste bunu nasıl yapacağımızı öğrenmeye çalışacağız.
return ifadesi fonksiyonun işlemi bittikten sonra çağrıldığı yere değer döndürmesi anlamı taşır. 
Böylelikle, fonksiyonda aldığımız değeri bir değişkende depolayabilir 
ve değeri programın başka yerlerinde kullanabiliriz. Şimdi iki tane çok basit fonksiyon yazalım 
ve return neden gereklidir anlamaya çalışalım.

def toplama1(a,b,c):          -> Birinci fonksiyon
	print("Toplamları:",a+b+c)
def ikiyleçarp(a):            -> İkinci fonksiyon
	print("ikiyle çarp",a*2)

toplam = toplama1(3,4,5)
ikiyleçarp(toplam)           -> Hata alırız

toplamları:12
Type Error        verecektir
Burada hata almamızın sebebi fonksiyonları herhangi bir değer döndürmemesi yani return kullanmamasıdır.



Burada toplama fonksiyonundan herhangi bir değer döndürülmediği için toplam değişkenimiz hiçbir değere sahip olmadı
ve tipi NoneType(atanmamış) olmuş oldu. 
İsterseniz burada fonksiyonları tekrardan tanımlayalım ve return mantığını anlamaya çalışalım.

Doğru olan:
def toplama1(a,b,c):
	print("Toplamları:",a+b+c)
def ikiyle_çarp(a):
	return a*2
toplam=toplama1(3,4,5)
print(ikiyle_çarp(toplam))

ÇIKTISI:

	""")
def toplama1(a,b,c):
    return a+b+c     # return 'un kullanımı
def ikiyle_çarp(a):
    return a*2
 
toplam = toplama1(3,4,5)
print(ikiyle_çarp(toplam))
print("""
şte return ifadesinin anlamı tam olarak budur.
return yardımıyla fonksiyonlar değerleri çağrıldığı yere döndürebilir ve biz de bu değerleri istediğimiz yerde kullanabiliriz
	""")
print("""
Bir örnek daha yapalım:
def üçleçarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a + 2
def dördeböl(a):
    print("3.fonksiyon çalıştı")
    return a / 4
# 3 ünü beraber kullanalım.
 
print(dördeböl(ikiyletopla(üçleçarp(5))))


ÇIKTISI:
	""")
def üçleçarp(a):
    print("1.fonksiyon çalıştı")
    return a*3
def ikiyletopla(a):
    print("2.fonksiyon çalıştı")
    return a + 2
def dördeböl(a):
    print("3.fonksiyon çalıştı")
    return a / 4
# 3 ünü beraber kullanalım.
 
print(dördeböl(ikiyletopla(üçleçarp(5))))
print("""******************************************
return ifadesinden sonra fonksiyonumuz tamamıyla sona erer. Yani, return ifadesinden sonra yapılan herhangi bir işlem çalıştırılmaz. """)
print("""

def toplama2(a,b,c):
    return a + b + c
    print("Toplama fonksiyonu") -> Çalıştırılmadı.

doğrusu şu şekildedir:
def toplama2(a,b,c):
    print("Toplama fonksiyonu") # Çalıştırıldı.
    return a + b + c
 
toplama2(1,2,3)

	""")
def toplama2(a,b,c):
    print("Toplama fonksiyonu") # Çalıştırıldı.
    return a + b + c
 
toplama2(1,2,3)

print("""
	fonksiyonlarda çağrıldığı yere herhangi bir değer döndürmeyen(return kullanılmayan) fonksiyonlara void fonksiyonlar denmektedir. Bunu da genel kültür olarak bilmekte fayda var.

	***********************************************************************
	""")
print("""
                       FONKSİYONLARDA PARAMETRE TÜRLERİ

--Parametrelerin Varsayılan Değerleri--

def selamla(isim):
    print("Selam",isim)
selamla("Baysan")
Çıktısı:
Selam Baysan
*************
selamla()  -> Bu kullanım hata verecektir çünkü isim parametresi girmedik.

->Ancak biz eğer bir parametrenin değerini varsayılan olarak belirlemek istersek, 
bunu varsayılan değerler ile yapabiliriz. 
Varsayılan değerleri anlamak için selamla fonksiyonunu varsayılan parametre değeri ile yazalım.

def selamla5(isim="varsayılan isim"):
    print("Selam",isim)
selamla5()                -> Hiç bir değer göndermedik isim parametresinin değeri varsayılan olarak "varsayılan isim" olarak belirlendi
selamla5("Baysan")        -> Değer verirsek varsayılan değerin yerine bizim verdiğimiz değer geçer.


	""")
def selamla5(isim="varsayılan isim"):
    print("Selam",isim)
selamla5()
selamla5("Baysan")
print("""**************************************
    peki birden fazla parametreye sahip olursak ne olacak?
Birden fazla parametreye sahip olduğumuz bir fonksiyon daha tanımlayalım...

def bilgilerigöster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara =  "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)

bilgilerigöster()
bilgilerigöster("Enes","Baysan")

    """)
def bilgilerigöster(ad = "Bilgi Yok",soyad = "Bilgi Yok",numara =  "Bilgi Yok"):
    print("Ad:",ad,"Soyad:",soyad,"Numara:",numara)
bilgilerigöster()
bilgilerigöster("Enes","Baysan")
print("""**********
Ancak böyle bir durumda argümanları gönderirken sıralı vermemiz gerekiyor.
Peki sadece numara parametresine değer vermek istersek ne yapmalıyız?

bilgilerigöster(numara="12345")         -> numara parametresini özel olarak belirtiyoruz.
 
ÇIKTISI:
  """)
bilgilerigöster(numara="12345")

print("""********
    Bir diğer örnek:

    bilgilerigöster(ad="Enes",numara="12345")
Çıktısı:

    """)
bilgilerigöster(ad="Enes",numara="12345")
print("""**************
print fonksiyonunun sep parametresini hatırlayalım
print("Muhammed","Enes","Baysan")             -> sep parametresine değer vermeyince varsayılan olarak boşluk karakteri verildi.
print("Muhammed","Enes","Baysan",sep = "/")   -> sep parametresine özel olarak değer atadık.
 ÇIKTISI:""")
print("Muhammed","Enes","Baysan")
print("Muhammed","Enes","Baysan",sep="/")
print("""****************************
 Esnek Sayıda Değerler
Biliyorsunuz bir fonksiyon yazıldığında özel olarak kaç tane parametresi olacağını önceden belirtmemiz gerekiyor. 
Örneğin, bir toplama fonksiyonu yazalım.

def toplama6(a,b,c):
    print(a+b+c)
toplama6(7,8,9)
ÇIKTISI:
    """)
def toplama6(a,b,c):
    print(a+b+c)
toplama6(7,8,9)

print("""**************
toplama6(3,4,5,6)  -> bunu yaparsak hata alırız. 3 argüman tanımladığımız bir fonksiyona 4. argümanı veremeyiz.

Eğer bu fonksiyonu 4 argüman alacak şekilde tanımlamak istersek, tekrardan tanımlamamız gerekiyor.
def toplama6(a,b,c,d):
    print(a+b+c+d)
toplama6(1,2,3,4)
Ancak bu seferde 3 argüman veremeyiz
toplama6(1,2,3)     -> hata alırız  """)
print("""******************

Peki ben bir fonksiyonu esnek sayıda argümanla kullanmak istersem ne yapacağım ?
Bunun için de Yıldızlı Parametre kullanmam gerekiyor. 
Kullanımı şu şekildedir;

def toplama7(*parametreler): -> Artık parametreler değişkenini bir demet gibi kullanabilirim.
    toplam1 =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam1 += i
    return toplam1
print(toplama7(3,4,5,6,7,8,9,10))
 ÇIKTISI:     """)
def toplama7(*parametreler):
    toplam1 =  0
    print("Parametreler:",parametreler)
    for i in parametreler:
        toplam1 += i
    return toplam1
print(toplama7(3,4,5,6,7,8,9,10))
print("""
    print(toplama7())
Çıktısı: """)
print(toplama7())

print("""*************
print(toplama7(1,2,3))
ÇIKTISI:  """)
print(toplama7(1,2,3))
print("*******************************")
print("""
                FONKSİYONLARIN KAPSAMI GLOBAL VE YEREL DEĞİŞKENLER

Pythonda her bir değişkenin, fonksiyonun ve ileride göreceğimiz sınıfların(class) aslında bir kapsamı(scope) bulunur 
ve Python herbir değişkeni bir isim alanında (namespace) tanımlar. 
Değişkenlerin İsim alanı ise, bu değişkenlerin nerelerde var olduğunu ve nerelerde kullanılabileceğini gösterir.
Pythonda fonksiyonlarda tanımlanan değişkenler Python tarafından Yerel (Local) değişkenler olarak tanımlanırlar. 
Yani bir fonksiyon bloğunda oluşturulan değişkenler fonksiyona özgüdür ve fonksiyon çalışmasını bitirdikten sonra bu değişkenler bellekten silinir 
ve yok olur. Böylelikle , fonksiyon içinde tanımlanmış bir değişkene başka bir yerden erişilemez.
Pythonda en genel kapsama sahip değişkenler ise Global değişkenler olarak tanımlanırlar ve global değişkenlere tanımlandığı andan itibaren programın her yerinden ulaşabiliriz.

Yerel değişkenleri anlamak için bir tane fonksiyon tanımlayalım.
def fonksiyon():
    a = 10 # Yerel isim alanında bir değişken
    print(a)
     
fonksiyon() 
print(a)  # a değişkeni yok oldu. -> hata verecektir

Burada fonksiyon içinde tanımlanan a değişkeni fonksiyon çağrıldığında bellekte oluşur ve fonksiyon bloğunu çalıştırdıktan sonra yok olur. Yani, a değişkeni burada bir yerel değişkendir.
***********************************
Global Değişkenleri anlamak içinse şöyle bir örnek yapalım.

a = 5 # Global isim alanında bir değişken .
 
def fonksiyon():
    print(a) # a değişkeni globalde tanımlandığı için burada tanımlı.
    
fonksiyon()
ÇIKTISI:
5
*****************************************************************
Peki şöyle bir kodda nasıl bir sıkıntı çıkıyor ?

def fonksiyon():
    print(s)
 
fonksiyon() # s global değişkeni henüz tanımlanmadığı için Python hata veriyor.
s = "Python"    -> bu kodda hata verecektir..
*********************************************************
Peki şöyle bir durumda kodumuz nasıl bir çıktı verecek ?

c = 10 # Globalde tanımlanmış bir değişken 
def fonksiyon():
    c = 2 # Yerelde tanımlanmış bir değişken
    print(c)  # Yerel değişken kullanılıyor.
 
fonksiyon()
print(c)

ÇIKTISI:
2
10  ->Kodumuz çalıştığında ilk olarak c isimli global değişken oluşuyor. fonksiyon çağrıldığında ise c isimli başka bir yerel değişken oluşuyor gibi düşünebilirsiniz. Böyle bir durumda elimizden iki tane c değişkeni var. Python bu durumda global c değişkeni yerine kendi yerel c değişkenini kullanıyor.
**********************************************************************************************************************************************************************************************************************************************************************************************************************

Global Deyimi
Peki bir fonksiyonda globalde tanımlanmış bir değişkeni nasıl kullanacağız ? Bunun için Pythonda global ifadesi bulunmaktadır. Şimdi aşağıdaki kodu beraber inceleyelim.

d = 10
 
def fonksiyon():
    global d
    
    d = 4
    print(d)
fonksiyon()
print(d)

ÇIKTISI:
4
4

->Bu durumda kodumuz ne yapıyor ? İlk olarak program başladığı zaman, bir tane global d değişkeni oluşuyor ve fonksiyonumuz çağrıldığında global d ifadesiyle globaldeki d değişkenini kullanmak istediğimizi söylüyoruz. Böyle d = 4 ifadesiyle bir tane daha d değişkeni oluşturmuyoruz. Böylelikle d =4 ifadesiyle globaldeki değişkeninin değerini değiştirmiş oluyoruz.

*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************

İşte Global ve Yerel değişkenler bu şekilde düşünülebilir. Burada gördüğümüz gibi, Yerel değişkenler bir fonksiyon bloğunda içinde tanımlanır. Peki bir if veya while bloğunda yerel bir değişken tanımlanır mı hemen bakalım.

if True:
    t = 10
    print(t)
 
print(t)

ÇIKTISI:
10
10
******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************


while True:
    deger =  10
    print(deger)
    break
 
print(deger)

ÇIKTISI:
10
10

->Burada gördüğümüz gibi, if ve while bloklarında tanımlanan değişkenler yerel bir değişken yerine global bir değişken olmaktadır.
""")

print("""
*******************************************************************

                            Lambda İfadeleri

Bu konuda lambda ifadelerini(expression) öğrenmeye çalışacağız. lambda ifadeleri fonksiyonlarımızı oluşturmak için Pythonda bulunan pratik bir yöntemdir ve gerektiği yerlerde bu ifadeleri kullanabiliriz. Biliyorsunuz listelerimizi oluşturmak için List Comprehension yöntemini kullanabiliyorduk. İsterseniz List Comprehension yöntemini hatırlayalım.

liste1 = [1,2,3,4,5] 
liste2 = list()
for i in liste1: # Bu klasik liste oluşturma yöntemi
    liste2.append(i*2)
print(liste2)

ÇIKTISI:
[2, 4, 6, 8, 10]


Aynı buradaki gibi bir fonksiyonu da tek satır halinde lambda ifadeleriyle oluşturabiliriz. İlk önce yapısına bakalım sonra örneklerimize geçelim.

etiket = lambda parametre1,parametre2.... :  İşlem


Bir tane iki ile çarpma görevini yerine getiren fonksiyon yazalım.

def ikiyleçarp(x): # Klasik fonksiyon tanımlama
    return x * 2
print(ikiyleçarp(2))
ÇIKTISI:
    """)
def ikiyleçarp(x):
    return x * 2
print(ikiyleçarp(2))

print("""


# Şimdi de bu fonksiyonu lambda ifadelerini kullanarak tek satırda yazalım.
 
ikiyleçarp = lambda x : x * 2 # x parametre x* 2 return ifadesi ve ikiyleçarp değeri de bir etikettir(değişken gibi düşünelim)
 
ikiyleçarp(3) # Buradaki 3 argümanı lambda ifadesindeki x'in yerine geçiyor.
ÇIKTISI:
    """)
ikiylecarp = lambda x : x * 2
print(ikiylecarp(3))

print("""
    ************************************************************************
def toplama(a,b,c):
    return a + b + c
 
print(toplama(3,4,5))   yerine

topla = lambda x,y,z : x + y + z
 
print(topla(3,4,5))    yazabiliriz
*********************************************************
Stringi ters çevirme

def terscevir(s):
    return s[::-1]
 
print(terscevir("Python Programlama"))
 yerine;

ters =  lambda s : s[::-1]

print(ters("Python Programlama"))

kullanabiliriz
ÇIKTISI:
    """)
ters =  lambda s : s[::-1]

print(ters("Python Programlama"))
print("""
    İşte lambda ifadesini bu şekilde küçük fonksiyonlar için kullanabiliriz. lambda ifadelerini özellikle kısa bir fonksiyonu def ifadesiyle yazmanın zahmetli olduğu zamanlarda kullanılabilir.


*******************************************************************************************************************************************************************************************************************
    """)