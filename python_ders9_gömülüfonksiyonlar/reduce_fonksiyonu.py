print("""
Reduce Fonksiyonu

reduce() fonksiyonu değer olarak aldığı fonksiyonu soldan başlayarak listenin 
ilk 2 elemanına uygular ve daha sonra çıkan sonucu listenin 3. elemanına uygular 
ve bu şekilde devam ederek liste bitince bir tane değer döner.

reduce(function, iterasyon yapılabilen veritipi(liste vb.))



from functools import reduce      # reduce fonksiyonu son sürümlerde functools modülüne taşındı.

def fonk(x,y):
	return x+y
liste1=[12,18,20,10]
print(reduce(fonk,liste1))


ÇIKTISI:
	""")
from functools import reduce      # reduce fonksiyonu son sürümlerde functools modülüne taşındı.

def fonk(x,y):
	return x+y
liste1=[12,18,20,10]
print(reduce(fonk,liste1))
print("""
Pek bir artısı yok bence mantık şu şekilde:
Önce listenin 1. ve 2. elemanı toplanıyor,Sonuç 2.elaman yerine atanıyor ve 3. eleman ile toplanıyor,bunun sonucu 3. eleman oluyor 4. eleman ile toplanıyor....
Bu şekilde gidiyor. Adım Adım Nasıl Olduğunu Yukardaki Listemize göre görelim:
1-) 12+18
2-)30+20
3-)50+10
4-)=60

Faktoriyel bulmak için kolaylıkla kullanılabilir.
	
import functools
def fakto(x,y):
	return x*y

liste=range(1,6)

print(functools.reduce(fakto,liste))


Gibi ;)


	""")