print("""
**********************************
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
**********************************

sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    
    basamak = gecici_sayı % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayı //= 10
    

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")
    

""")
sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):
    
    basamak = gecici_sayı % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayı //= 10
    

if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")
    
