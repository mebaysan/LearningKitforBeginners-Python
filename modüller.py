print("Bu ders dosyası Baysan tarafından hazırlanmıştır...")

print("""                    MODÜLLER


Pythonda aslında herbir dosya bir modüldür ve her bir modül içinde fonksiyonlar, sınıflar ve objeler barındırır. 
Biz de bu modülleri programımıza dahil ederek içindeki fonksiyonlardan, sınıflardan ve objelerden faydalanabiliriz.

Pythonda da modül kavramı oldukça önemli bir kavramdır. 
Bir Python modülünü programımıza dahil ederek bu modüller içinde yazılan fonksiyonlardan ve sınıflardan kullanabilir ve programlarımızı daha efektif bir şekilde yazabiliriz. 
Eğer modül diye bir kavram olmasaydı, programlarımızdaki herbir fonksiyonu ve sınıfı kendimiz yazmak zorunda kalacaktık.
	""")
print("""
********************************************************************************************************************************************************************************************************
Modül Kullanımı -math modülü


hazır bir modül olan math modülünü kullanmaya başlayalım.

import math           # Modülü içeri aktarıyoruz. Artık bu modülün tüm fonksiyonlarını kullanabiliriz.

print(dir(math))      # Math modülünün içindekileri görmek için dir fonksiyonunu kullanabiliriz.
 
print(help(math))     # Fonksiyonların görevlerini görebilmek için help fonksiyonunu kullanabiliriz.

""")
import math 
print(dir(math))
print(help(math))


print("""

************************************************************************************************************************************

İçeri aktarma yöntemiyle math modülünün herhangi bir fonksiyonunu nasıl kullanacağız ?

modül_adı.fonksiyonadı()

Örneğin ilk olarak math modülünün içindeki factorial fonksiyonu ne iş yapıyor bakalım.
print(help(math.factorial))
	""")
print(help(math.factorial))
print("""
Örnek bir modül kullanalım;

print(math.factorial(5))
ÇIKTISI: """)
print(math.factorial(5))
print("""
*****************************************************
Peki biz bir modülü kendi belirlediğimiz isimle nasıl kullanıyoruz ? Bunun için de şu şekilde bir şey yapacağız.

import math as matematik
print(matematik.factorial(6))   # Modülü artık matematik ismiyle kullanabiliriz

ÇIKTISI:
""")
import math as matematik
print(matematik.factorial(6))
print("""
********************************************************
KENDİ MODÜLLERİMİZİ YAZMAK İÇİN;

1. Herhangi bir tane klasör oluşturuyoruz.
2. Modülümüz ve deneme Python dosyamız aynı dizinde olması gerektiği için 2 tane Python dosyasını da bu klasör altında oluşturuyoruz.
3. modul1.py ve deneme.py dosyası oluşturuyoruz.
4. modul1.py dosyasının içine istediğimiz kadar fonksiyonu yazıyoruz.
5. Son olarak da deneme.py dosyasının içinde bu modul1.py modülünü kullanıyoruz.


YAZDIĞIMIZ BİR MODÜLÜ HER YERDEN KULLANMAK İÇİN NE YAPACAĞIZ?
Bunun için yazdığımız modul1.py dosyasının Python35/Lib klasörünün altına atmamız gerekiyor. 
Böylelikle bu modülü de math modülü gibi her dosyada kullanabiliriz.

Eğer kapsamlı bir modül yazıp buna heryerden ulaşmak isterseniz;
Python'ın kendi klasörüne girip lib adlı klasör altına atıp herhangi bir python dosyası içinde kullanabilirsiniz.
	***********************************************************
	Yöntem2 – from modül_adı import *
	Bir modülü programımıza dahil etmek için bu yöntemi de kullanabiliriz. 
from math import * # Yıldızın anlamı math modülünün içindeki bütün fonksiyonları almak istediğimizi belirtiyor.

print(factorial(5)) # direk fonksiyon adını gireceğiz






	""")