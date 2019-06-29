print("Bu dosya BAYSAN tarafından hazırlanmıştır...")
print("""					İç içe Fonksiyonlar ve Fonksiyon Parametreleri


*args ve **kwargs
Fonksiyonlara argüman göndermenin esnek bir şekilde yapıldığını biliyoruz. İsterseniz ilk olarak yıldızlı argümanları hatırlamaya çalışalım.

def fonksiyon(*args): # İstediğimiz sayıda argüman gönderebiliyoruz.
    print(args)
    for i in args:
        print(i)

******************************************************************************
def fonksiyon(**kwargs):
    print(kwargs)
fonksiyon(isim = "Murat", soyisim = "Coşkun", numara = 12345)


Dikkat ederseniz 2 yıldız koyarak keyword argümanlar ile (anahtar kelimeli argümanlar) fonksiyonumuzu tanımladık ve 
argümanlara isim vererek fonksiyonumuzu çağırdığımızda isimleri anahtar kelime , 
argüman değerlerini değer olarak alarak fonksiyonumuz sözlük oluşturdu. 
İşte keyword argümanlar bu şekilde kullanılabiliyor.
*****************************************************	""")
print("""
					İç içe fonksiyonlar

Pythonda fonksiyonlar da birer obje oldukları için hem bir tane değişkene atanabilirler, hem de başka bir fonksiyonun içinde tanımlanabilirler. 
Şimdi bunlara bakmaya başlayalım;

def selamla(isim):
    print("Selam",isim)

merhaba=selamla			-> # merhaba obje tipi fonksiyon oldu,#Değişkene atayalım

del selamla             -> # selamla fonksiyonunu siliyoruz.
***********************************************************
	""")
print("""
					Iteratorların Oluşturulması ve Kullanılması

Iteratorlar nedir?
Iteratorlar aslında Pythonda çoğu yerde biz görmesek de kullanılır. Iteratorlar özellikle for döngülerinde , list comprehensionlarında, ve bir sonraki derste göreceğimiz generatorlarda karşımıza çıkar.

Iteratorlar en genel anlamıyla üzerinde gezinilebilecek bir objedir ve bu obje her seferinde bir tane eleman döner.

Pythonda kendisinden iterator oluşturabileceğimiz her obje iterable bir objedir.. Örneğin, demetlerden,listelerden ve stringlerden oluşturduğumuz bütün objeler iterable bir objedir.

Bir objenin iterable olması için hazır metodlar olan __iter()__ ve __next()__ metodlarını mutlaka tanımlaması gerekir.
Iterator oluşturma
Bir iterator objesini , iterable bir objeden (liste,demet,string vs) oluşturmak için Pythonda iter() fonksiyonunu kullanıyoruz ve bu objenin bir sonraki elemanını almak için next() fonksiyonu kullanıyoruz.


İşte iterable bir objeden bir iterator’ı bu şekilde oluşturup, next() fonksiyonuyla objenin sıradaki elemanını alabiliyoruz. Ancak eleman kalmayınca StopIterationhatasını alıyoruz. 
İşte iteratorların kullanımı bu şekildedir. 
Aslında biz farketmesek de Pythondaki for döngüleri aslında bir objenin üzerinde gezinirken iteratorları kullanır.

*********************************************************************************
	""")
print("""
						Generatorların Oluşturulması ve Kullanılması

Generatorlar Pythonda iterable objeler (örnek olarak fonksiyonlar) oluşturmak için kullanılan objelerdir ve bellekte herhangi bir yer kaplamazlar. Örneğin, 100.000 tane değer üretip, bu değerleri bir listede tutmak bellekte oldukça fazla yer kaplayacaktır. O yüzden bu işlemi gerçekleştiren bir fonksiyonu generator fonksiyon şeklinde yazmak oldukça mantıklı olacaktır. Generatorları anlamak için isterseniz bir fonksiyonu ilk olarak generator kullanmadan yazmaya çalışalım.


Generatorlerin değer üretmesi için yield anahtar kelimesini kullanacağız.






	""")