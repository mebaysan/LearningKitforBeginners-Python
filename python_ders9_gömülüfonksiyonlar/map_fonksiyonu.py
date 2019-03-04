print("""
Map Fonksiyonu

Bu konuyla beraber Pythonda gömülü olan bazı fonksiyonlarımızı öğrenmeye başlıyoruz.

Pythonda gömülü bir fonksiyon olan map() fonksiyonunun yapısı şu şekildedir.

                map(fonksiyon,iterasyon yapılabilecek veritipi(liste,demet vb),....)


map() fonksiyonu ilk parametre olarak bir tane fonksiyon objesi alır. (Fonksiyonlar da birer obje olduğu için başka bir fonksiyona gönderilebilir.) 
2. parametre olarak da bir tane iterasyon yapılacak veritipi alarak , gönderilen fonksiyonu her bir eleman üzerinde uygulayarak sonuçları bir map objesi olarak döner.


Örnek olması için bir adet fonksiyon yazalım;
liste1=[1,2,3,4,5]

def ikikat(x):
    return x * 2
print(list(map(ikikat,liste1)))   -> ikikat fonksiyonunu liste1'in her elemanına uygulamak için map fonksiyonu koyduk.Bunu da listelemek için list,ekrana bastırmak için print kullandık.


list(map(double,liste1)) -> map() fonksiyonunun içine bir adet fonksiyon() yollayıp,ardından
 								  ->iterasyonal yani liste demet vb. gibi veri tipi yollarız.

ÇIKTISI:

	""")
def ikikat(x):
	return x*2

liste1=[1,2,3,4,5]
print(list(map(ikikat,liste1)))


print("""
Map fonksiyonu birden fazla liste veya demet alabilir. Aynı zamanda map fonksiyonu içine gönderdiğimiz fonksiyonları 'lambda' ifadesiyle de yazabiliriz.

ÖRNEK:
liste2=[6,7,8]
liste3=[1,2,3]
liste4=[3,4,5]

def deneme(x,y):
	return x*y
print(list(map(deneme,liste2,liste3)))


ÇIKTISI:
	""")
liste2=[6,7,8]
liste3=[1,2,3]
liste4=[3,4,5]

def deneme(x,y):
	return x*y
print(list(map(deneme,liste2,liste3)))
print("""
Yani burda;
liste2 ve liste3'ün birinci elemanlarını , ikinci elemanlarını, üçüncü elemanlarını sırasıyla çarpıp ekrana bastırdı.


	""")