print("""			İleri Seviye Kümeler (Sets)

Kümeler, matematikte olduğu gibi bir elemandan sadece bir adet tutan bir veritipidir. Bu açıdan kullanıldıkları yerlerde çok önemli bir veritipi olmaktadırlar. 

x = set() # boş küme
aynı zamanda x={\\1,2,3,1,2,3,1,2,3} dersekte küme oluşur yani {\\} süslü parantez

liste = [1,2,3,3,1,1,2,2,2] # Aynı elemanı birçok defa  barındıran bir liste
x = set(liste)			    # Veri tipi dönüşümü 
print(x)
ÇIKTISI:
	""")
liste=[1,2,3,3,1,1,2,2,2]
x=set(liste)
print(x)
print("""
y = set("Python Programlama Dili")  # Aynı karakterler tek bir karaktere indirgendi.
print(y)
ÇIKTISI:
	""")
y = set("Python Programlama Dili")
print(y)
print("""
For döngüsüyle Gezinmek
Kümeler de tıpkı sözlükler gibi sırasız bir veri tipidir. Bunu for döngüsüyle görebiliriz.
 z= {"Python","Php","Java","C","Javascript"}
for i in z:
	print(i)
ÇIKTISI:
	""")
z= {"Python","Php","Java","C","Javascript"}
for i in z:
	print(i)
print("""
				Kümelerin Metodları


Eleman Eklemek : add() metodu

Kümeye eleman eklemimizi sağlar. Aynı eleman eklenmeye çalışırsa hata vermez ve herhangi bir ekleme işlemi yapmaz.

x={1,2,3,4}
x.add(4)        -> şeklinde kullanılır

*****************************************************

difference() metodu:
Bu metod birinci kümenin ikinci kümeden farkını döner.
    
    küme1.difference(küme2) # Küme1'in Küme2'den farkı

küme1={1,2,3,4,5,6,-1,-2,-16}
küme2={2,3,4,5,6,7}
küme1.difference(küme2)    -> kullanım bu şekildedir.
*************************************************************
difference_update() metodu
Bu metod birinci kümenin ikinci kümeden farkını dönerek birinci kümeyi bu farka göre günceller.
küme1.difference_update(küme2) # Küme1'in Küme2'den farkı

küme1={1,2,3,4,5,6,-1,-2,-16}
küme2={2,3,4,5,6,7}
küme1.difference_update(küme2)  -> şeklinde kullanılır/kısaca küme1 ve küme 2'nin farkının küme1'e atanması
****************************************************************
discard() metodu
İçine verilen değeri kümeden çıkartır. Eğer kümede öyle bir değer yoksa, bu metod hiçbir şey yapmaz(Hata vermez).

küme1 = {1,2,3,4,5,6}
küme1.discard(7)       -> şeklinde kullanılır
**********************************************************

intersection() metodu

Bu metod iki kümenin kesişimleri bulmamızı sağlar.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.intersection(küme2) -> şeklinde kullanılır
**************************************************************
 intersection_update() metodu

Bu metod birinci kümeyle ikinci kümenin kesişimlerini bulur ve birinci kümeyi bu kesişime göre günceller.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.intersection_update(küme2)   -> şeklinde kullanılır
**************************************************************
isdisjoint() metodu

Bu metod, eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.isdisjoint(küme2)   -> şeklinde kullanılır
**************************************************

Alt kümesi mi ? : issubset() metodu

Bu metod , birinci küme ikinci kümenin alt kümesiyse True, değilse False döner.

küme1 = {1,2,3}
küme2 = {1,2,3,4}
küme1.issubset(küme2)   -> şeklinde kullanılır
******************************************************
union() metodu

Bu metod, iki kümenin birleşim kümesini döner.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.union(küme2)              -> şeklinde kullanılır

***************************************************************

Birleşim Kümesi ve update : update() metodu

Bu birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.


küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.update(küme2)                -> şeklinde kullanılır








	""")
