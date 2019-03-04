print("""			İLERİ SEVİYE LİSTE METODLARI

append() metodu
append metodu listenin en sonuna eleman eklememizi sağlar.
***********************************************************
extend() metodu
extend() metodu bir listeye başka bir listenin elemanları eklememizi sağlar.

liste=[1,2,3,4,5]
liste2=list()
liste2.extend(liste)
**********************************

insert() metodu
insert() metodu listenin belli bir indeksine bir eleman eklememizi sağlar.

liste.insert(2,"Python") # 2.indekse "Python" değerini ekliyoruz.
*****************************************************************
pop() metodu
pop() metodu içine hiçbir değer vermezsek listenin son elemanını silerek ekrana basar. 
İçine belli bir indeks değeri verirsek o indeksi siler ve ekrana basar.
*****************************************************

remove() metodu
remove() metodu verdiğimiz değeri listeden çıkarmamızı sağlar.

liste = ["Python","Php","Java","C"]
liste.remove("Python") # Python'ı siliyoruz./Eğer remove() içine gönderdiğimiz veri listede yoksa hata döner.
**********************************************************
index() metodu
index() metodu verilen bir değerin baştan başlayarak hangi indekste olduğunu söyler. 
Değer listede yoksa hata döner. 
Eğer ekstra index değeri belirtilirse, index metodu() değeri bu indeksten itibaren aramaya çalışır.
********************************************************

count() metodu
count() metodu verilen bir değerin listede kaç defa geçtiğini sayar.
liste = [1,2,3,4,5,6,1,1,1,1,1,1,1,1,8]
liste.count(1)   -> şeklinde kullanılır
***************************************************************

sort() metodu

sort() metodu bir listenin elemanlarını sayıysa küçükten büyüğe , 
string ise alfabetik olarak sıralar. 
Eğer özellikle içine reverse = True değeri verilirse elemanları büyükten küçüğe sıralar.
liste=[1,67,13,467,132123,-7,-10,-99]
liste.sort()
print(liste)
[-99, -10, -7, 1, 13, 67, 467, 132123]
liste.sort(reverse=True)
print(liste)
[132123, 467, 67, 13, 1, -7, -10, -99]




	""")