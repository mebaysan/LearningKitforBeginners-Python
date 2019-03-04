print(""" Bu ders dosyası Baysan tarafından hazırlanmıştır...
*************************************************************************	""")
print("""					Dosya Açma ve Yazma İşlemleri

Dosya Açmak

Bir dosyayı açmak için open() fonksiyonunu kullanıyoruz. Yapısı şu şekildedir;

open(dosya_adı,dosya_erişme_kipi)

“w” dosya kipi

Dosyalarımızı açmak ve dosyalarımıza yazmak için “write” anlamına gelen “w” kipini kullanıyoruz. “w” kipi eğer oluşturmak istediğimiz dizinde öyle bir dosya yoksa dosyayı oluşturuyor , 
eğer öyle bir dosya varsa dosyayı silip tekrar oluşturuyor. 
Yani, eğer açmak istediğimiz dosyadan zaten varsa ve dosyanın içi doluysa “w” kipi dosyadaki bilgileri silip tekrar oluşturacaktır. (Biraz Tehlikeli)

open("deneme.txt","w")         -> bulunduğumuz dizinde txt dosyası açtı
file=open("deneme.txt","w")    -> oluşturduğumuz dosyaya değişken atadık. Bu değişkeni kullanarak istediğimiz dosya işlemini yapabiliriz.
file.close()                   -> dosyayı kapatmak için dosyaya atadığımız değişken.close() fonksiyonunu kullanmamız gerek. Aksi halde dosya kapanmaz hep açık kalır.


Eğer bir dosyayı bulunduğumuz dizinde değil de başka bir dizinde açmak istersek, dizinin yolunu özellikle belirtmeliyiz.
file = open("C:/Users/user/Desktop/bilgiler.txt","w")    # çalıştırdığımızda masaüstünde bilgiler.txt oluşacaktır.
file.close()                    ->->->->->->             # Unutmayalım.

“w” Kipiyle Dosyalara Yazmak

İlk olarak dosyayı “w” kipiyle açıyoruz.

file = open("bilgiler.txt","w",encoding="utf-8")   # Türkçe karakter kullanacaksak encoding="utf-8" parametresini veriyoruz.
file.write("Muhammed Enes Baysan")                 # write fonksiyonu ile dosyamıza yazıyoruz. 20 bytelık yani 20 karakter yazıldı. 
file.close()
********************************************************************
“a” Kipiyle Dosyalara Yazmak

“append” (ekleme) kelimesinin kısaltması olan “a” kipiyle bir dosyayı açtığımızda , dosya eğer yoksa oluşturulur. 
Eğer öyle bir dosya mevcut ise, dosya tekrar oluşturulmaz ve dosya imleci dosyanın sonuna giderek dosyaya ekleme yapmamızı sağlar.

file = open("bilgiler.txt","a",encoding="utf-8")    -> a kipiyle dosyamızı açtık
file.write("Muhammed Enes Baysan") 					-> Muhammed Enes Baysan'ı içine yazdık
file.close()										-> Dosyayı kapattık

Dosyayı tekrar açalım...
file = open("bilgiler.txt","a",encoding="utf-8")    # açacağımız dosya üzerinde rahat işlem yapmak için 'dosya' değişkenine atadık.
file.write("Yusuf Baysan") 							# Dosyanın sonuna ekleme yaptık.
file.close()

***************************************************************************************************************
Dosya Okuma İşlemleri

Dosyaları okumak ve verileri almak için “r” kipiyle açmamız gerekiyor. 
“r” kipiyle açtığımız dosya eğer bulunmuyorsa “FileNotFoundError” hatası dönecektir.

file = open("bilgiler.txt","r", encoding="utf-8")
file.close()

Dosya işlemlerini daha güvenli yazmak try,except bloklarını kullanabilirsiniz.


try:
    file = open("bilgiler2.txt","r",encoding= "utf-8")
except FileNotFoundError:                               -> Eğer dizinde dosya yoksa alttaki mesajı döndürür.
    print("Dosya Bulunamadı....")
 

Peki bir dosyanın içinden bilgileri nasıl okuyacağız ?


For döngüsü ile okuma

file = open("bilgiler.txt","r",encoding= "utf-8")    # Dosyayı okuma kipiyle(yani üstüne birşey yazmayacağız) açıyoruz. Türkçe karaktere dikkat.
 
for i in file:                                       # Tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    print(i)                                         # Her bir satırı ekrana basıyoruz.
file.close()

Burada her bir satırımız boşluklu yazıldı. Bunun nedeni, hem her satır sonunda “\\n” karakterinin olması hem de print fonksiyonun bir alt satıra geçmek için boşluk bırakmasıdır. 
Bunu önlemek için varsayılan değer olarak “\\n” karakteri alan end parametresine kendimiz değer verebiliriz.

file = open("bilgiler.txt","r",encoding= "utf-8") # Dosyayı okuma kipiyle açıyoruz. Türkçe karaktere dikkat.
 
for i in file:                   # Tıpkı listeler gibi dosyanın her bir satırı üzerinde geziniyoruz.
    print(i,end = "")            # Her bir satırı ekrana basıyoruz. end parametresi \\n yerine boşluk alacak.
file.close()



read() fonksiyonu

read() fonksiyonu eğer içine hiçbir değer vermezsek bütün dosyamızı okuyacaktır.

file = open("bilgiler.txt","r",encoding="utf-8")
 
icerik = file.read() 
 
print("Dosya İçeriği:\\n",icerik,sep ="")
 
file.close()
read() fonksiyonuyla bir dosyayı okuduğumuzda dosya imlecimiz dosyanın en sonuna gider ve read() fonksiyonu 2. okuma da artık boş string döner.



readline() fonksiyonu

readline() fonksiyonu her çağrıldığında dosyanın sadece bir satırını okur. Her seferinde dosya imlecimiz (file) bir satır atlayarak devam eder.

file = open("bilgiler.txt","r",encoding="utf-8")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline()) # Okuyacak herhangi bir şey kalmayınca readline fonksiyonu boş string döner.
file.close()

readlines() fonksiyonu

readlines() fonksiyonu dosyanın bütün satırları bir liste şeklinde döner.

file = open("bilgiler.txt","r",encoding="utf-8")
 
file.readlines()
 
file.close()
***********************************************************************************************************

Dosyalarda Kullanılan Fonksiyonlar

osyaları Otomatik Kapatma

Dosyalarda işlemlerimiz bittiği zaman dosyamızı kapatmamız gerektiğini biliyoruz. Ancak programlamacılık doğası gereği çoğu zaman dosyaları kapatmayı unutabiliriz. Bunun için Pythonda dosyalarda işimiz bitince otomatik kapatma özelliği bulunuyor.

with open(dosya_adı,dosya_kipi) as file:
     Dosya işlemleri
ÖRNEK:
with open("bilgiler.txt","r",encoding = "utf-8") as file:
    for i in file:
        print(i)

Eğer dosya işlemlerini bu blok içinde yaparsak işlemimiz bittiği zaman dosyamız otomatik olarak kapanacaktır.
******************************************************************************************

Dosyaları İleri Geri Sarmak

dosya imlecimiz okuma işleminin sonunda , dosyanın en sonuna gidiyordu. Ancak biz çoğu zaman dosya imlecini (file) dosyanın herhangi bir yerine götürmek isteyebiliriz. 
Bunun için Pythondaki seek() fonksiyonunu kullanacağız. 
Ancak ondan önce dosya imlecinin hangi byteda olduğunu söyleyen tell() fonksiyonuna bakalım.

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    print(file.tell())     -> Bize imlecin hangi byte de olduğunu söyler.


Şu anda hiçbir işlem yapmadığımız için tell() fonksiyonu dosyanın en başında (0. byteda) olduğumuzu söyledi. Peki bir dosya imlecini dosyanın 20.byte’ına götürmek için ne yapacağız ? 
Bunun için de seek() fonksiyonunu kullanacağız.

with open("bilgiler.txt","r",encoding = "utf-8") as file:
    file.seek(20) # 20.byte götürdük.
    print(file.tell()) 


Peki biz bir dosyanın belirli bir byte’ına(karakter) gidip sadece belli sayıda karakteri nasıl okuyacağız ? Eğer biz read() fonksiyonuna bir sayı değeri verirsek sadece o sayı değeri kadar alanı okuyacaktır.
with open("bilgiler.txt","r",encoding = "utf-8") as file:
    file.seek(5) # 5.byte gidiyoruz.
    icerik = file.read(10)  # 10 karakteri okuyoruz.
    print(icerik)
    print(file.tell())



r+ Kipi -> hem okuma hem de yazma işlemimizi yapmamızı sağlar





Dosyalarda Değişiklik Yapmak
seek() ve write()

Eğer biz bir dosyanın belli bir yerine seek() fonksiyonu ile gidip, write() fonksiyonunu kullanırsak, yazdığımız değerler öncesinde bulunan değerlerin üzerine yazılacaktır. 
Bunun için hem okuma hem de yazma işlemimizi yapmamızı sağlayan “r+” kipini kullanacağız. 
İlk önce dosyamızda bilgileri görelim.

with open("bilgiler.txt","r+",encoding = "utf-8") as file: 
    file.seek(10)                   # 10. byte üzerine gider ve üzerine yazar
    file.write("Deneme")


Dosyanın Sonunda Değişiklik Yapmak

Bu işlemlerin en kolayıyla başlayalım. Dosyaların sonunda değişiklik yapmak için, dosyamızı “a” kipiyle açalım ve sadece dosyanın sonuna write() ile ekleme yapalım.

with open("bilgiler.txt","a",encoding = "utf-8") as file:
    file.write("Mert Erarslan\\n")                          # "append" metoduyla açılan bir dosyanın imleci direk dosyanın sonunda olduğu için sadece write


Dosyanın Başında Değişiklik Yapmak

“bilgiler.txt” dosyamızın başına bir tane satır eklemek için ne yapabiliriz ? Bunun için dosyamızı bütünüyle string halinde alıp daha sonra satırımızı string’in başına eklememiz gerekiyor. Daha sonra dosyanın en başına seek() fonksiyonuyla giderek ,direk write() fonksiyonunu kullanabiliriz. Hemen yapalım.
with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    
    icerik = "Dosyanın Başına Eklemek\\n" + icerik
    file.seek(0)
    file.write(icerik)





	""")
