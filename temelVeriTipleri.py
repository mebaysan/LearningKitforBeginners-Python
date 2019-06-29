print("Bu ders dosyaları Baysan tarafından hazırlanmıştır...")
#cmd ile python kodlarını test etmek istersen cd komutu ile dosyanın olduğu yere git ve python ****.py (dosya adı) ile çalıştır
#cmd ile kodları test ederken türkçe karakter (ı,ç,ş,ö,ü) kullanmamalısın. cmd tanımlamaz ve hata verir.
#Python da # yorum satırıdır
#python da verilerin içine hangi değeri atarsan at direk o değeri alır
# Örnek
baysan=50
sonuç=baysan*baysan*baysan #baysan=50 baysan*baysan*baysan=>50*50*50
print(sonuç)

#Dairenin çevresini hesaplamak için alttaki gibi bir kod dizilimi yazabiliriz bunu kendi isteğimize göre çoğaltıp üretebiliriz
print("Daire çevre Hesaplama Kaynak Kodlarda Daha Detaylı")
pi_sayisi=3.14
cap=4
cevre=pi_sayisi*cap
print(cevre)

# iki veri içindeki değeri değiştirmek için böyle bir yöntem kullanabilirsin : a,b=b,a
a=5
b=10
print("a:",a,"b:",b)
print("Arada a,b=b,a","  ","Komutu kullandık")
a,b=b,a
print("a:",a,"b:",b)

# mesela i=5 i=i+1  yeni değeri kendisi + 1(değer değişebilir kendinizce) olsun dediğimizde daha kolay yolu var i+=1(sadece toplama değil aynı işlem ile * / + - yapabilirsiniz)
print("******")
print("Değişkeni kendisi + 1 ile değiştirmek")
i=6
print("i:",i)
i=i+1
print("i+1:",i)
print("kolay yazım kodumuz:")
i+=1
print("i+=1:",i)
print("burada 8 vermesinin sebebi aynı kod dizininde yazıldı yukarda i tekrar tanımlandığı için aşağıda i=7 olarak devam etti")
print("******")
print("Kendisi ile çarptırma (i için)")
i*=5
print("i*=5:",i," ","kendisini 5 ile çarptırma")
"""
python da çoklu yorum satırı yapmak için kullanılır (" üç tane)
Toplama İşlemi (+)
Çıkarma İşlemi (-)
Çarpma İşlemi (*)
Bölme İşlemi (/)
Tamsayı Bölmesi (//) (kalanı vermez yani)
Kalanı Bulma (%) (sadece kalanı verir)
Üs bulma (**)
python matematiksel işlemler sırası:
1. Parantez içi her zaman önce yapılır.
 Çarpma ve Bölme her zaman Toplama ve Çıkarma işlemine göre önce yapılır.
İşlemler soldan sağa değerlendirilir
"""
print("******","    ", "*******")
print("String Oluşturmak")
#String oluşturma '****' "***" """**""" tek tırnak/çift tırnak/üç çift tırnak
# Kaç tırnak ile başladıysan o kadar ile bitir
# \ yok sayma işaretidir. ters slash kendisinden sonraki komutu saymaz.
x="Merhaba"
print("x=Merhaba"," ","print(x): Merhaba")
#indexler 0'dan başlar python da. index parçalamak için string adı ["kaçıncı index lazımsa"]
print("******")
print("İndeks Kullanma")
z="Merhaba"
print("z=Merhaba")
print("z[4] için :",z[4])
#İndeks parçalama [*:*:*] başlama indexi,bitiş indexi,atlama değeri(sırasıyla)
print("İndeks Parçalama Örnek","  ","Formül:[*:*:*]")
g="Sanane İHH banane AGD"
print("g=",g)
print(g[2:8:3])
print("g için index parçalama","  ","g[2:8:3]")
#atlama değeri vermeyebilirsin,o zaman başlama değerinden başla bitiş indexine git ama bitiş indexini dahil etme demek
print("atlama değeri vermezsek")
print("g[2:8] için : ",g[2:8])
#başlangıç indexini de vermeyebilirin o zaman da başlangıç indexinden başla belirtilen indexe git vb varyasyonları var
print("başlama değeri vermezsek")
print("g[:10] için:",g[:10])
# [:-1] verirsek baştan başla sondaki karaktere kadar git demek oluyor.Eksi (-) olarak ta parçalanabilir
print("başlama ve bitiş değeri vermezsek")
print("g[::2] için:",g[::2])
#stringi tersten parçalatır(yazdırır) *[::-1]
print("Stringi tersten parçalamak")
print("g[::-1] için:",g[::-1])
# stringin kaç karakterden(indexten) oluştuğunu bulmak için len() fonksiyonu kullanılır
print("Stringin kaç indexten oluştuğunu bulmak/len() fonksiyonu")
print("len(g) için :",len(g))
#sayıları sayılar gibi toplayabilirsin çarpabilirsin
print("Unutma stringleri toplayıp çarpabilirsin")
print("********")
#Veri Tipi Dönüşümleri

"""
Tamsayıyı Ondalıklı Sayıya Çevirme
Bir tamsayı değeri(integer) ondalıklı sayıya(float) çevirmek için float() fonksiyonunu kullanabiliriz.

Ondalıklı Sayıyı Tamsayıya Çevirme
Bir ondalıklı sayıyı tamsayıya çevirmek için int() fonksiyonunu kullanabiliriz.Sonuç, ondalıklı sayının tam kısmı olarak karşımıza çıkacak.

Sayıları Stringlere Çevirme
Bir sayıyı string’e çevirmek için str() fonksiyonunu kullanabiliriz.Sayıyı oluşturan tüm rakamlar veya noktalar birer karaktere dönüşecek.

Stringleri Tamsayıya Çevirme
Bir string’i bir tamsayıya çevirmek istediğimiz zaman int() fonksiyonunu kullanabiliriz. Ancak biraz dikkatli olmamızda fayda var. Dönüştürme işlemini yaparken stringin herbir karakterinin bir rakam olduğundan emin olmalıyız.

Stringleri Ondalıklı Sayıya Çevirme
Bir string’i bir ondalıklı sayıya çevirmek istediğimiz zaman float() fonksiyonunu kullanabiliriz. Ancak biraz dikkatli olmamızda fayda var. Dönüştürme işlemini yaparken stringin ondalıklı sayı formatına uygun olduğundan emin olmalıyız.

"""
k=25
print("Tam sayıyı ondalıklı sayıya çevirmek")
print("k= 25","print(float(k)) :",float(k))
print("*****")
print("Ondalıklı sayıyı tam sayıya çevirmek")
j=6.7
print("j=6.7 için:","print(int(j)) ->",int(j))
print("**Sayıları Stringe Çevirmek**")
m=150
print("m=150 için:","print(str(m)) ->",str(m),"/cmd de çok belli olmayabilir ancak genelde input fonksiyonunda çok iş görür")

print("Stringi Tam Sayıya Çevirmek")
n="123"
print("n=123 için:","print(int(n)) ->",int(n),"/cmd de çok belli olmayabilir ancak program yazarken bu fonksiyon da çok iş görür")

print("Stringi Ondalıklı Sayıya Çevirmek")
l="12.3"
print("l=12.3 için:","print(float(l)) ->",float(l),"yine bu da cmd de çok belli olmayabilir ama çok iş görür")
# tamsayı->integer(int)     ondalıklı sayı->float(float)

print("******")
#Stringlerdeki özel karakterler
# \n koyarsak alt satıra geçer
# \t bir tab boşluk bırakır
print("\\n koymak bir alt satıra geçirir,\\t koymak bir tab boşluk bıraktırır")
print("print(\"Enes\\nBaysan\\nMuhammed\"","alt satırda örneği var")
print("Enes\nBaysan\nMuhammed")
print("Diğer örnek")
print("print(\"Enes\\tBaysan\\tMuhammed\"","alt satırda örneği var")
print("Enes\tBaysan\tMuhammed")

#Type fonksiyonu bize içine gönderdiğimiz değerin hangi türde olduğunu söyler
print("type() fonksiyonu bize içine gönderdiğimiz değerin hangi türde olduğunu söyler")
print("print(type(12)) için: ->",type(12))

#sep parametresi print fonksiyonunda kullanlır ve araya ne koydurmak istersek onu koydurur ,sep="."
print("print(\"a\",\"b\",\"c\",\"d\")   için sep parametresi ->","print(\"a\",\"b\",\"c\",\"d\",sep='.'")
print("a","b","c","d",sep=".")
print("diğer örnek")
print(35,56,78,88,sep="<")


print("*****")
#Yıldızlı parametreler print(*"Ör1","Ör2")
print("Yıldızlı parametre aralarında boşluk bırakır")
print("print(*\"a\",\"b\",\"c\"","için ->")
print(*"a","b","c")
print("Hem sep Hem * parametresi kullanımı")
print("print(*\"TBMM\",sep=\".\")","çıktısı alt satırda")
print(*"TBMM",sep=".")
print("*************************")
# String formatlama işlemi -> "{} {} {}".format(*,*,*) süslü parantez içindeki stringler yıldızlılarla yer değiştirir sırasıyla
#Örnek
print("String Formatlama Örneği")
sayi_1=25
sayi_2=15
print("sayi_1=25,sayi_2=15 için alttaki formül kullanılır.Stringin çokça yolu vardır.Bunun için şu siteye bakabilirsin-> https://pyformat.info/")
print("print(\"{} + {} toplamı = {}\".format(sayi_1,sayi_2,sayi_1+sayi_2))")
print("Çıktısı ise alttaki gibidir ->")
print("{} + {} toplamı = {}".format(sayi_1,sayi_2,sayi_1+sayi_2))
#string formatlamanın çok fazla yolu vardır. Hepsini akılda tutmak zor olur bunun için lazım oldukça şu siteye bakabilirsin ->  https://pyformat.info/
print("*********************************************")
#Liste veri tipi a=["elma",1,2,3,12312,5,6,7,"asdsda","böyle işler"] bir listedir.Listeler değiştirilebilir.Listeler [] köşeli parantezler içinde oluşturulur.
print("LİSTE VERİ TİPİ")
liste=["karpuz",12,"Merhaba",45,]
print(liste)
#boş liste oluşturmak için liste=list()
print("print(len(liste)) için çıktı alt satırda","Liste kaç indexten oluşuyor onu gösterir")
print(len(liste))
print("Listelerde de index parçalama aynı şekildedir.Örnek:","  ","print(liste[2])")
print(liste[2])
#2 listeyi toplayabilirsin
#Stringlerde index değiştiremiyorduk fakat listelerde index değiştirilebilir.ÖRNEK: liste[1]="sanane"
print("Listelerde veri değiştirme")
print("print(liste)   için ->")
print(liste)
print("şimdi 2. indexi değiştirelim")
print("liste[2]=değiştir","-> bu kod zincirini kullanırız")
liste[2]="değiştir"
print(liste,"-> Gördüğün gibi değişti")
#listede mesela ilk 2 elemanı değiştirmek istersek -> liste[:2]="değiştir1",2
print("listede mesela ilk 3 elemanı değiştirmek istersek -> liste[:2]=\"elma\",\"muz\",\"votka\"")
print("Çıktı aşağıda ->")
liste[:2]="elma",2,"votka"
print(liste)
"""
LİSTE METODLARI
append metodu
append metodu, verdiğimiz değeri listeye eklememizi sağlar-> liste.append()

pop metodu
Bu metod, içine değer vermezsek listenin son indexindeki elemanı, değer verirsek verdiğimiz değere karşılık gelen indexteki elemanı LİSTEDEN ATAR VE EKRANA BASAR->liste.pop()

sort metodu #BİR LİSTE İÇİNDE STRİNG VE İNT/FLOAT DEĞERLERİ VARSA LİSTE SIRALAMAZ
sort metodu listenin elemanlarını sıralamamızı sağlar-> liste.sort()  #Küçükten büyüğe sıralar
liste.sort(reverse=True) #Büyükten küçüğe sıralar.
"""
print("***********************************")
print("LİSTE METODLARI")
print("Burada direk yapacağım kaynak kodlarda daha detaylı mevcut")
liste.append("ekledim")
print(liste)
liste.pop()
print(liste,"son elemanı yani eklediğimi attım")
print("*****************************************************************")
print("LİSTE İÇİNDE LİSTE OLUŞTURMAK")
liste
liste2=[1,2,3,4]
liste3=[5,6,7,8,9]
liste4=[liste,liste2,liste3]
print("liste=[yukarda verdik]\nliste2=[1,2,3,4]\nliste3=[5,6,7,8,9]\niçin çıktı aşağıda")
print(liste4)
#İç içe liste oluşturmak için oluşturduğun listeleri 3. bir liste içine ata.
print("********************************************************************************")
#Demetler (Tuple'lar)
#Bir program içinde demetler değiştirilemez. listelerden en temel farkı budur. değiştirilmesini istemediğimiz verileri demetler ile yazdırabiliriz.
print("DEMETLER(TUPLE'lar)")
demet=(1,2,3,4,5,5,4,2,3,1,2,3,4,5,1,2,3,4,5,2,1,2,12)
print("demet=(1,2,3,4,5,5,4,2,3,1,2,3,4,5,1,2,3,4,5,2,1,2,12) için\ntype(demet) için ->\n",type(demet))
#Demetlerde de index bulma ve parçalama yapabiliriz.
"""
DEMETLERİN METODLARI
index-> metoduyla içine verdiğimiz elemanın hangi indexte olduğunu bulabiliriz.
demet.index()

count-> metoduyla içine verdiğimiz değerin demette kaç defa geçtiğini bulabiliriz.
demet.count()
"""
print("Demetlerin 2 metodu vardır. index() ve count() metodu")
print("count metodu içinde verdiğimiz elemandan kaç adet vardır onu verir")
print("demet.count(1) ->\n",demet.count(1))
print("///////////////////")
print("index metodu içine verdiğimiz değerin kaçıncı indexte olduğunu bize verir")
print("demet.index(12) ->")
print(demet.index(12))
#index'e olmayan bir index girersen hata verir.
print("***************************")
#Sözlükler-Dictionary
print("Sözlükler-Dictionary")
"""
Sözlük oluşturmak için 2 süslü parantez içine ":" ile anahtar kelimeleri yerleştiririz.
sözlük={"bir":1,"iki":2,"üç":3} #Soldakiler anahtar kelime sağdakiler anahtar değerlerdir!
sözlük2=dict() #Boş sözlük oluşturur./ sözlük2={} buda boş sözlük oluşturur.
"""
sözlük={"bir":1,"iki":2,"üç":3}
print("sözlük={\"bir\":1,\"iki\":2,\"üç\":3}")
print("print(type(sözlük))\n->",type(sözlük))
#sözlükte istediğimiz değere ulaşmak için anahtar kelimeleri vermemiz gerek
# -> Örnek: print(sözlük["bir"])
print("print(sözlük[\"bir\"]) için\n ->",sözlük["bir"])
#Olmayan bir anahtar kelime verirsek sözlük hata döner.
# !!!SÖZLÜKLERDE İNDEX'E ERİŞEMEYİZ VE SÖZLÜKLER SIRALI OLARAK İLERLEMEZ.
#sözlüğe eleman eklemek için sözlük["beş"]=5 kod dizilimini kullanabiliriz.
print("Sözlüğe eleman eklemek için ***")
print("sözlük[\"beş\"]=5 için\n ->")
sözlük["beş"]=5
print(sözlük)
#Sözlüklerde ve listelerde iç içe olan kısımlarda ilerlemek için ÖRNEK: a["iki"][2][1] gibi bir dizilim kullanabiliriz.Bu a sözlüğünde->iki anahtar kelimesine -> ona karşılık gelen listenin 2. indexine -> ona karşılık gelen listenin içindeki indexe git demek.
#ÖRNEK
print("İç içe kullanımda nasıl verilere ulaşırız kaynak kodlarda daha detaylı <-")
sözlük_deneme={"bir":[1,2,3,4,5],"iki":["elma","armut","muz"],"üç":[[5,10],[15,20],[25]]}
print("print(sözlük_deneme={\"bir\":[1,2,3,4,5],\"iki\":[\"elma\",\"armut\",\"muz\"],\"üç\":[5,10,15,20,25]})")
print("print(sözlük_deneme[\"üç\"])")
print(sözlük_deneme["üç"])
print("print(sözlük_deneme[üç][1]")
print(sözlük_deneme["üç"][1])
print("print(sözlük_deneme[üç][1][0]")
print(sözlük_deneme["üç"][1][0])
#dictionary içindeki anahtarı mutlaka "  " içinde yaz.
#SÖZLÜKTE DEĞER DEĞİŞTİRMEK-> sözlük["bir"]=10
print("///////////")
print("SÖZLÜKTE DEĞER DEĞİŞTİRMEK")
print("önceden yukarda oluşturduğumuz sözlüğümüzü bir görelim\n ->",sözlük)
print("şimdi sözlükte istediğimiz değeri değiştirmek için gerekli kod dizilimini yazalım\n -> sözlük[\"bir\"]=19")
sözlük["bir"]=19
print(sözlük,"-> gördüğünüz gibi anahtar\"bir\"e denk gelen değer değişti.Unutma sözlüklerde veriler sıralı olarak çıktı vermez. onun için anahtar bir ortalara gitmiş olabilir ")
#Tekrar hatırlatma sözlükte anahtar kelimeyi mutlaka "  " içinde yaz!!!
#Sözlüklerde mesela bir değeri artırmak istersek: sözlük["salladım"]+=1  değeri 1 arttırır.Bunun örneğini yapmayacağım zaten basit.
#İç içe liste olduğu gibi iç içe sözlükte yapılabilir. ÖRNEK:
# -> a = {"sayılar":{"bir":1,"iki":2,"üç":3},"meyveler":{"kiraz":"yaz","portakal":"kış","erik":"yaz"}} -> yine buna da aşama aşama içine ulaşabiliriz yukardaki örneklerde olduğu gibi.
"""
Sözlüklerde temel metodlar:
# values() metodu sözlüğün değerlerini(value) bir liste olarak döner.
print(yeni_sözlük.values())
 
# keys() metodu sözlüğün anahtarlarını(key) bir liste olarak döner.
print(yeni_sözlük.keys())
 
# items() metodu sözlüğün anahtar ve değerlerini bir liste içinde demet olarak döner.
print(yeni_sözlük.items())
"""
print("////////")
print("Sözlüklerde temel metodlar")
print("elimizdeki sözlüğümüzü tekrar bir hatırlayalım\n ->",sözlük)
print(".values() metodu")
print(sözlük.values())
print(".keys() metodu")
print(sözlük.keys())
print(".items() metodu")
print(sözlük.items())
print("**********************")
#Kullanıcıdan Girdi Alma input() Fonksiyonu
print("Kullanıcıdan Girdi alma input() Fonksiyonu")
#input() içine string verebiliriz -> input("Lütfen bir sayı girin:")
#input() değerini bir değişkene atayabiliriz. a=input("bir sayı gir")
"""
a=input("Bir sayı gir")
print("girilen sayı",a)
"""
# girilen sayı str olarak döner bizim bunu int/float değerine çevirmemiz lazım ki işlem yapabilelim sayıya.
# int çevirme -> a=int(input("bir sayı girin"))
print("Üç sayının toplamlarını yazdırma(kaynak kodlarda daha detaylı <-")
a=int(input("Birinci Sayı :"))
b=int(input("İkinci Sayı :"))
c=int(input("Üçüncü Sayı :"))
print("Toplamları = ",a+b+c)
print("************")
print("TEMEL PYTHON VERİLERİ VE TEMELLERİ ÖĞRENDİK BİR SONRAKİ NOTLARDA GÖRÜŞMEK ÜZERE")
