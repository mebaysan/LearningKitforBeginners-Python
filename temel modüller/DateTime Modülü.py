DateTime Modülü

from datetime import *  # datetime modülündeki bütün fonksiyonlar

Şu anki zamanı alma - now()
şu_an = datetime.now()
şu_an.year # Yılı alıyoruz.
şu_an.month # Ayı alıyoruz. (7. Ay -- Temmuz)
şu_an.day # Temmuzun  11'i
şu_an.hour # Saat 5 
şu_an.minute # 5'i 1 geçiyor.
şu_an.second # Saniye 36
şu_an.microsecond # Milisaniye 472991
*****************************************
ctime() fonksiyonu
Şu anki zamanı daha güzel göstermek için ctime() fonksiyonunu kullanabiliriz.
print(datetime.ctime(şu_an)) 
ÇIKTISI:
Tue Jul 11 17:01:36 2017

Peki şu anki zamanın yıl, ay , gün gibi özelliklerin sadece belli bir kısmını nasıl gösterebiliriz ? Bunun için de strftime fonksiyonunu kullanacağız.

strftime() fonksiyonu
    Yıl bilgisini almak için : %Y

    Ay ismini almak için : %B

    Gün ismini almak için : %A

    Saat bilgisini almak için : %X

    Gün bilgisini almak için : %D

print(datetime.strftime(şu_an,"%Y"))  # ve benzeri

Buradaki yazıları Türkçe yapmaya çalışalım.

import locale
print(locale.setlocale(locale.LC_ALL,""))

timestamp() ve fromtimestamp()
Şu anki zamanı saniye cinsinden bulmak için, datetime objemizi (şu_an objesi) timestamp() fonksiyonumuza gönderebiliriz. Aynı zamanda saniye cinsinden verilmiş bir zamanı da fromtimestamp fonksiyonuyla datetime objesine çevirebiliriz.


Belli iki tarih arasındaki farkı bulmak
tarih = datetime(2019,12,1) 
şu_an = datetime.now()
fark = tarih - şu_an
fark.days # 872 gün kalmış
fark.seconds # 23304 gün kalmış
fark.microseconds # 341519


