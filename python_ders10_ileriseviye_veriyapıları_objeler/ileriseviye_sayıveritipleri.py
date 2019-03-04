print("""
İleri Seviye Sayılar

bin() fonksiyonu:
10'luk tabandaki bir sayıyı 2'lik tabana çevirmek için kullanılır.
ÖRNEKLER
1-)bin(4)  # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
2-)bin(19) # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
3-)bin(521) # bin fonksiyonu . Sayımız 2'lik tabanda yazıldı. (1 ve 0)
ÇIKTISI:
	""")
print(bin(4))
print(bin(19))
print(bin(521))
print("""********************************
hex() fonksiyonu:
10'luk tabandaki bir sayıyı 16'lık tabana çevirmek için kullanılır.
ÖRNEKLER:
1-)hex(32) # Sayımız 16'lık tabanda yazıldı.
2-)hex(54) # Sayımız 16'lık tabanda yazıldı.
3-)hex(1212) # Sayımız 16'lık tabanda yazıldı.
ÇIKTISI:
	""")
print(hex(32))
print(hex(54))
print(hex(1212))
print("""********************************************
							FONKSİYONLAR

abs fonksiyonu
Sayının mutlak değerini almamızı sağlar.
ÖRNEKLER:
1-)abs(-4)
2-)abs(4.5)
3-)abs(0)
4-)abs(-10)
ÇIKTISI:
	""")
print(abs(-4))
print(abs(4.5))
print(abs(0))
print(abs(-10))
print("""********************************************

round fonksiyonu
Sayıları alta veya üste yuvarlar.
ÖRNEKLER:
1-)round(3.7)
2-)round(3.2)
3-)round(3)
4-)round(3.21329321321323,4) # Ondalıklı sayının 4. hanesine göre yuvarlar
5-)round(3.21324321321323,4) # Ondalıklı sayının 4. hanesine göre yuvarlar
ÇIKTISI:
	""")
print(round(3.7))
print(round(3.2))
print(round(3))
print(round(3.21329321321323,4))
print(round(3.21324321321323,4))
print("""****************************************

max ve min fonksiyonu
max() fonksiyonu verdiğimiz değerlerin en büyüğünü döndürür.
ÖRNEKLER:
1-)max(3,4)  # İstediğimiz kadar değer verebiliriz.
2-)max[100,-2,3,4,1,131]  # Sayıları liste olarak yollayabiliriz./ya da herhangi bir liste veri tipi yollayabiliriz.
ÇIKTISI:
	""")
liste=[100,-2,3,4,1,131]
print(max(3,4))
print(max(liste))
print("""
min() fonksiyonu verdiğimiz değerlerin en küçüğünü döndürür.
ÖRNEKLER:
1-) min(3,4)
2-) min(100,-2,3,4,1,131)
ÇIKTISI:
	""")
liste1=[100,-2,3,4,1,131]
print(min(3,4))
print(min(liste1))
print("""**********************************************


sum fonksiyonu

sum() fonksiyonu verilen değerleri toplayarak döndürür. Değerlerin liste,demet vb. şeklinde verilmesi gerekir.

ÖRNEKLER:
liste3=[3,4,5,6,7]
sum(liste3)
ÇIKTISI:
	""")
liste3=[3,4,5,6,7]
print(sum(liste3))
print("""*****************************************

pow fonksiyonu
pow() fonksiyonu üs alma işlemlerinde kullanılır. 1. değer taban, 2. değer üs değeridir.
ÖRNEKLER:
pow(2,4)    # 2 üzeri 4
pow(17,2)   # 17 üzeri 2
ÇIKTISI:
	""")
print(pow(2,4))
print(pow(17,2))
