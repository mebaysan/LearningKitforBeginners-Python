print("""Bu ders dosyası Baysan tarafından Hazırlanmıştır...	""")
print("""
                       NESNE TABANLI PROGRAMLAMA MANTIĞI

Nesne Yönelimli Programlama veya ingilizce ismiyle Object Oriented Programming en basit anlamıyla gerçek hayatı programlamaya uyarlamak olarak düşünülebilir. 
Örneğin bir tane öğrenci otomasyon sistemi yazmak istiyoruz. 
Bunun için öğretmenleri , öğrencileri ve kursları aslında birer nesne olarak oluşturmamız gerekiyor. 
Böyle bir sistemi programlamayla gerçekleştirmek için aslında her bir nesnenin yapısını tanımlayıp, daha sonra bu yapılardan nesneler üretmemiz gerekiyor. 
İşte Nesne Yönelimli Programlama en basit anlamıyla bu şekilde """)

print("""**************************************************************************************************************************
OBJE NEDİR ?
Etrafımıza baktığımızda aslında her bir eşyanın bir obje olduğunu görüyoruz. 
Örneğin bir tane televizyon kumandasını düşünelim. 
Bu kumandanın kendi içinde değişik özellikleri (attribute) ve fonksiyonları(metod) bulunuyor. 
Örneğin, kumandanın markası, tuşları aslında bu kumandanın özellikleridir(attribute). 
Kumandanın kırmızı tuşuna bastığımızda televizyonun kapanması ve sesi kapatma tuşuna bastığımızda televizyonun sesinin kapanması bu kumandanın metodlarıdır. 
Bunun gibi Pythondaki aslında her şey bir objedir. 
Örneğin, listelere bakacak olursak bu liste objelerinin aslında birçok metodu ve özelliği bulunur.

liste, dictionary, function, tuple; hepsi birer objedir. """)
print("""**************************************************************************************
Sınıflar
Kendi veri tiplerimizi oluşturmak ve bu veri tiplerinden objeler üretmemiz için öncelikle objeleri üreteceğimiz yapıyı tanımlamamız gerekiyor. 
Bunu tasarladığımız yapıya da sınıf veya ingilizce ismiyle class diyoruz.

Class Anahtar Kelimesi
Sınıflar veya Classlar objelerimizi oluştururken objelerin özelliklerini ve metodlarını tanımladığımız bir yapıdır ve biz herbir objeyi bu yapıya göre üretiriz. 
İsterseniz bir Araba classı tanımlayarak yapımızı kurmaya başlayalım.


#  Yeni bir Araba veri tipi oluşturuyoruz.
class Araba():
    model =  "Renault Megane"
    renk = "Gümüş"            # Sınıfımızın özellikleri (attributes)
    beygir_gücü = 110
    silindir = 4
	""")

#  Yeni bir Araba veri tipi oluşturuyoruz.
class Araba():
    model =  "Renault Megane"
    renk = "Gümüş"            # Sınıfımızın özellikleri (attributes)
    beygir_gücü = 110
    silindir = 4

print("""Sınıfımızı Pythonda tanımladık. Peki bu sınıftan obje nasıl oluşturacağız ?

	
objeismi = Sınıfİsmi(parametreler(opsiyonel))

	
araba1 =  Araba() # Araba veri tipinden bir "araba1" isminde bir obje oluşturduk.
 
print(araba1) # Objemizin veri tipi Araba
ÇIKTISI:	""")
araba1 =  Araba() # Araba veri tipinden bir "araba1" isminde bir obje oluşturduk.
 
print(araba1) # Objemizin veri tipi Araba
print("""
print(type(araba1))

ÇIKTISI:
	""")
print(type(araba1))
print("""
araba1 objesi artık sınıfta tanımladığımız bütün özelliklere (attributes) sahip olmuş oldu. 
İşte sınıf ve obje üretmek bu şekilde olmaktadır. 
Peki bu araba objesinin özelliklerinin nasıl görebiliriz ?

objeismi.özellikismi


print(araba1.model)
print(araba1.renk)
print(araba1.beygir_gücü)
print(araba1.silindir)

ÇIKTISI:
	""")
print(araba1.model)
print(araba1.renk)
print(araba1.beygir_gücü)
print(araba1.silindir)
print("""***********************
Şimdi de başka bir Araba objesi oluşturalım.
araba2 =  Araba()
 
print(araba2.model)
print(araba2.renk)
print(araba2.beygir_gücü)
print(araba2.silindir)


ÇIKTISI:
	""")
araba2 =  Araba()
 
print(araba2.model)
print(araba2.renk)
print(araba2.beygir_gücü)
print(araba2.silindir)
print("""
urda gördüğümüz gibi oluşturduğumuz objelerin buradaki model,renk vs. gibi özelliklerinin değeri aynıdır. 
Çünkü aslında burada tanımladığımız özellikler birer sınıf özelliğidir. 
Yani biz bir obje oluşturduğumuzda bu özelliklerin değerleri varsayılan olarak gelir. 
Bu özelliklerin değerlerine , herhangi bir obje oluşturmadan da erişebiliriz. 
Bunu da şu şekilde yapabiliriz:

print(Araba.renk) # Class_İsmi.özellik_ismi
print(Araba.beygir_gücü)

ÇIKTISI:

	""")
print(Araba.renk) # Class_İsmi.özellik_ismi
print(Araba.beygir_gücü)

print("""
Bizim her bir objeyi başlangıçta farklı değerlerle oluşturmamız için her bir objeyi oluştururken objelerin değerlerini göndermemiz gerekiyor. 
Bunun için de özel bir metodu kullanmamız gerekmektedir.

__init__()


Peki bu metod ne anlama geliyor ? İsterseniz ilk olarak dir() fonksiyonu yardımıyla araba1 objemizde neler var bakalım.

print(dir(araba1))
ÇIKTISI:
	""")
print(dir(araba1))
print("""
Burada objemizin tüm özelliklerini ve metodlarını görüyoruz. Ancak biz herhangi bir metod tanımlamamıştır. 
Buradaki metodlar Python tarafından bir obje oluşturulduğunda özel olarak tanımlanan metodlardır ve biz eğer özel olarak bunları tanımlamazsak Python kendisi bunları varsayılan tanımlıyor. 
Burada aynı zamanda init metodunu da görüyoruz. 
Eğer biz bu metodu kendimiz tanımlarsak objelerimizi farklı değerlerle başlatabiliriz.

Aslında init metodu Pythonda yapıcı(constructor ) fonksiyon olarak tanımlanmaktadır.
 Bu metod objelerimiz oluşturulurken otomatik olarak ilk çağrılan fonksiyondur. 
 Bu metodu özel olarak tanımlayarak objelerimizi farklı değerlerle oluşturabiliriz.

Peki bu metodu nasıl tanımlayacağız ? Direk örnek üzerinden görmeye çalışalım.


# Araba Veri tipi 
 
class Araba():
    # Şimdilik Class özelliklerine ihtiyacımız yok.
    
    def __init__(self):
        print("init fonksiyonu çağrıldı.")
 
araba1 = Araba() # araba1 objesi oluşurken otomatik olarak __init__ metodumuz çağrılıyor.


ÇIKTISI:
	""")
# Araba Veri tipi 
 
class Araba():
    # Şimdilik Class özelliklerine ihtiyacımız yok.
    
    def __init__(self):
        print("init fonksiyonu çağrıldı.")
 
araba1 = Araba() # araba1 objesi oluşurken otomatik olarak __init__ metodumuz çağrılıyor.

print("""
Peki burada self ne anlama geliyor ? 
self anahtar kelimesi objeyi oluşturduğumuz zaman o objeyi gösteren bir referanstır ve metodlarımızda en başta bulunması gereken bir parametredir. 
Yani biz bir objenin bütün özelliklerini ve metodlarını bu referans üzerinden kullanabiliriz.

Objeler oluşturulurken, Python bu referansı metodlara otomatik olarak kendisi gönderir. Özel olarak self referansını göndermemize gerek yoktur.

init metodunu ve self’i iyi anlamak için objelerimize özellikler ekleyelim


class Motor():
    
    def __init__(self,model,renk,beygir_gücü,silindir): # Parametrelerimizin değerlerini objelerimizi oluştururken göndereceğiz.
        self.model =  model # self.özellik_ismi = parametre değeri şeklinde objemizin model özelliğine değeri atıyoruz.
        self.renk = renk # self.özellik_ismi = parametre değeri şeklinde objemizin renk özelliğine değeri atıyoruz.
        self.beygir_gücü = beygir_gücü # self.özellik_ismi = parametre değeri şeklinde objemizin beygir_gücü özelliğine değeri atıyoruz.
        self.silindir = silindir # self.özellik_ismi = parametre değeri şeklinde objemizin silndir özelliğine değeri atıyoruz.
 
# motor1 objesini oluşturalım.
# Artık değerlerimizi göndererek objelerimizin özelliklerini istediğimiz değerle başlatabiliriz.
motor1 = Motor("Yamaha 301","Beyaz",90,4) 
 
# araba2 objesini oluşturalım.
motor2 = Motor("Scooter Megane","Gümüş",110,4)
 
print(motor1.model)
print(motor1.renk)
print(motor2.model)
print(motor2.renk)


ÇIKTISI:
	""")
class Motor():
    
    def __init__(self,model,renk,beygir_gücü,silindir): # Parametrelerimizin değerlerini objelerimizi oluştururken göndereceğiz.
        self.model =  model # self.özellik_ismi = parametre değeri şeklinde objemizin model özelliğine değeri atıyoruz.
        self.renk = renk # self.özellik_ismi = parametre değeri şeklinde objemizin renk özelliğine değeri atıyoruz.
        self.beygir_gücü = beygir_gücü # self.özellik_ismi = parametre değeri şeklinde objemizin beygir_gücü özelliğine değeri atıyoruz.
        self.silindir = silindir # self.özellik_ismi = parametre değeri şeklinde objemizin silndir özelliğine değeri atıyoruz.
 
# motor1 objesini oluşturalım.
# Artık değerlerimizi göndererek objelerimizin özelliklerini istediğimiz değerle başlatabiliriz.
motor1 = Motor("Yamaha 301","Beyaz",90,4) 
 
# araba2 objesini oluşturalım.
motor2 = Motor("Scooter Megane","Gümüş",110,4)
 
print(motor1.model)
print(motor1.renk)
print(motor2.model)
print(motor2.renk)

print("""
İstersek init metodunu varsayılan değerlerle de yazabiliriz.


class Bisiklet():
    
    def __init__(self , model = "Bilgi Yok",renk = "Bilgi Yok",beygir_gücü = 75 ,silindir = 4): 
        self.model =  model 
        self.renk = renk 
        self.beygir_gücü = beygir_gücü 
        self.silindir = silindir
 
bisiklet1 = Bisiklet(beygir_gücü = 85, renk = "Siyah")
print(bisiklet1.renk)
print(bisiklet1.model)


ÇIKTISI:
	""")
class Bisiklet():
    
    def __init__(self , model = "Bilgi Yok",renk = "Bilgi Yok",beygir_gücü = 75 ,silindir = 4): 
        self.model =  model 
        self.renk = renk 
        self.beygir_gücü = beygir_gücü 
        self.silindir = silindir
 
bisiklet1 = Bisiklet(beygir_gücü = 85, renk = "Siyah")
print(bisiklet1.renk)
print(bisiklet1.model)

print("""
İşte burada gördüğümüz gibi bir objeyi init metodunu kendimiz yazarak farklı değerlerle oluşturabiliyoruz.
************************************************************************************************************************************************
	""")


print("""
***********************************************

                      NESNE TABANLI PROGRAMLAMA METODLARI

Bu yazıda bir sınıf içinde metodlarımızı nasıl tanımlayacağımızı öğrenmeye çalışacağız. Bunun için ilk olarak bir Yazılımcı sınıfı tanımlayalım.

class Yazılımcı():
	def __init__(self,isim,soyisim,numara,maaş,diller):
		self.isim=isim
		self.soyisim=soyisim
		self.numara=numara            #Yazılımcı objelerinin özellikleri
		self.maaş=maaş
		self.diller=diller

#yazılımcı objesi
yazılımcı1= Yazılımcı("Enes","Baysan",12345,3000,["Python","Java","C"])
yazılımcı2= Yazılımcı("Yusuf","Baysan",23455,3020,["Python","Arapça","NodeJs"])

print(yazılımcı1.diller)
print(yazılımcı2.soyisim)


ÇIKTISI:

	""")
class Yazılımcı():
	def __init__(self,isim,soyisim,numara,maaş,diller):
		self.isim=isim
		self.soyisim=soyisim
		self.numara=numara            #Yazılımcı objelerinin özellikleri
		self.maaş=maaş
		self.diller=diller

#yazılımcı objesi
yazılımcı1= Yazılımcı("Enes","Baysan",12345,3000,["Python","Java","C"])
yazılımcı2= Yazılımcı("Yusuf","Baysan",23455,3020,["Python","Arapça","NodeJs"])

print(yazılımcı1.diller)
print(yazılımcı2.soyisim)
print("""
*******************************************************************
 Peki bu class’a metodlarımızı nasıl tanımlayabiliriz ? 
 Aynı init metodunu tanımladığımız gibi bir class’a da istediğimiz kadar metod tanımlayabiliriz. 
 Örneğin ,Yazılımcı classına bilgilerigöster isimli bir metod tanımlayalım.

class Yazılımc():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print(\"""
        Çalışan Bilgisi:
        
        İsim :  {\\}
        
        Soyisim : {\\}
        
        Şirket Numarası: {\\}
        
        Maaş :  {\\}
        
        Diller: {\\}
        "\\"".format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
 
yazılımc1 =  Yazılımc("Enes","Baysan",12345,3000,["Python","C","Java"])
 
yazılımc1.bilgilerigöster()


ÇIKTISI:
	""")
class Yazılımc():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim :  {}
        
        Soyisim : {}
        
        Şirket Numarası: {}
        
        Maaş :  {}
        
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
 
yazılımc1 =  Yazılımc("Enes","Baysan",12345,3000,["Python","C","Java"])
 
yazılımc1.bilgilerigöster()
print("""
Burada bilgilerigöster isimli metod tanımlayarak her bir özelliğimizin değeri ekrana derli toplu bir şekilde yazdırmış olduk. 
Metodlarımızı yazarken dikkat etmemiz gerek nokta, her metodun birinci parametresinin self referansı olması gerektiğidir. 
Ayrıca objelerimizin özelliklerine mutlaka self referansıyla erişmemiz gerekiyor.İsterseniz bu classa 2 tane daha metod yazalım.


class Yazılımcıx():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print(\"""
        Çalışan Bilgisi:
        
        İsim :  {\\}
        
        Soyisim : {\\}
        
        Şirket Numarası: {\\}
        
        Maaş :  {\\}
        
        Diller: {\\}
        ""\\".format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.")
        self.diller.append(yeni_dil)
    def maas_yukselt(self,zam_miktarı):
        print("Maaş yükseliyor...")
        
        self.maaş += 250
 
yazılımcıx1 =  Yazılımcıx("Mustafa Murat","Coşkun",12345,3000,["Python","C","Java"])
yazılımcıx1.bilgilerigöster()
yazılımcıx1.maas_yukselt(500)
 
yazılımcıx1.bilgilerigöster()
yazılımcıx1.dil_ekle("Javascript")
 
yazılımcıx1.bilgilerigöster()
ÇIKTISI:
	""")
class Yazılımcıı():
    
    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara    # Yazılımcı objelerinin özellikleri 
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim :  {}
        
        Soyisim : {}
        
        Şirket Numarası: {}
        
        Maaş :  {}
        
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.")
        self.diller.append(yeni_dil)
    def maas_yukselt(self,zam_miktarı):
        print("Maaş yükseliyor...")
        
        self.maaş += 250
 
yazılımcıı1 =  Yazılımcıı("Baysan","Baysan",12345,3000,["Python","C","Java"])
yazılımcıı1.bilgilerigöster()
yazılımcıı1.maas_yukselt(500)
yazılımcıı1.bilgilerigöster()
yazılımcıı1.dil_ekle("Javascript")
yazılımcıı1.bilgilerigöster()
print("""
**********************************************************************************************
                               Python – Kalıtım (Inheritance)


Nesne Yönelimli Programlamadaki inheritance(kalıtım veya miras alma) konseptini öğrenmeye çalışacağız. 
Inheritance veya kalıtım bir sınıfın başka bir sınıftan özelliklerini(attribute ) ve metodlarını miras almasıdır.
Bu konsepti aslında bizim kendi anne babamızdan değişik özellikleri ve davranışları miras almamıza benzetebiliriz.

Peki inheritance nerede işimize yarar ? Örneğin, bir şirketin çalışanlarını tasarlamak için sınıflar oluşturuyoruz. 
Bunun için Yönetici, Proje Direktörü, İşçi gibi sınıflar oluşturmamız gerekiyor. 
Aslında baktığımız zaman bu sınıfların hepsinin belli ortak metodları ve özellikleri bulunuyor. 
O zaman bu ortak özellikleri ve metodları tekrar tekrar bu sınıfların içinde tanımlamak yerine, bir tane ana class tanımlayıp bu classların bu classın özelliklerini ve metodlarını almalarını sağlayabiliriz. 
Inheritance’ın veya Kalıtım’ın temel mantığı budur.

İsterseniz inheritance yapısını kurmak için öncelikle bir tane çalışan sınıfı oluşturalım.


class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {\\} \\nMaaş: {\\} \\nDepartman: {\\}\\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
ÇIKTISI:
	""")
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
print("""
Çalışan sınıfını oluşturduk şimdi de Yönetici sınıfını bu Çalışan sınıfından türetmeye çalışalım.

class Yönetici(Çalışan):    # Çalışan sınıfından miras alıyoruz.
    pass                    # Pass Deyimi bir bloğu sonradan tanımlamak istediğimizde kullanılan bir deyimdir.


Burada, yönetici sınıfında herhangi bir şey tanımlamadık ancak Çalışan sınıfından bütün özellikleri ve metodları miras aldık. Bakalım burada Çalışan sınıfının metodlarını kullanabilecek miyiz ?
ÇIKTISI:
	""")
class Yönetici(Çalışan): # Çalışan sınıfından miras alıyoruz.
    pass # Pass Deyimi bir bloğu sonradan tanımlamak istediğimizde kullanılan bir deyimdir.

print("""yönetici1 = Yönetici("Enes Baysan",3000,"İnsan Kaynakları") # yönetici objesi
yönetici1.bilgilerigoster()

ÇIKTISI:
    	""")
yönetici1=Yönetici("Enes Baysan",3000,"İnsan Kaynakları")
yönetici1.bilgilerigoster()

print("""
yönetici1.departman_degistir("Halkla İlişkiler")
yönetici1.bilgilerigoster()
ÇIKTISI:
    """)
yönetici1.departman_degistir("Halkla İlişkiler")
yönetici1.bilgilerigoster()
print("""
Peki biz Yönetici sınıfına ekstra fonksiyonlar ve özellikler ekleyebiliyor muyuz ? 
Örnek olması açısından zam_yap isimli bir metod ekleyelim.

class Yönetici(Çalışan):
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı  


yönetici2=Yönetici("Yusuf Baysan",3000,"Bilişim")
yönetici2.zam_yap(500)
yönetici2.bilgilerigoster()


İşte biz bir sınıftan miras alarak oluşturduğumuz sınıflara ekstra metodlar ve özellikler de ekleyebiliyoruz.

ÇIKTISI:
    """)
class Yönetici(Çalışan):
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı  


yönetici2=Yönetici("Yusuf Baysan",3000,"Bilişim")
yönetici2.zam_yap(500)
yönetici2.bilgilerigoster()
print("""
*****************************************************************************************************

Overriding (İptal Etme)
Eğer biz miras aldığımız metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak , artık metodu çağırdığımız zaman miras aldığımız değil kendi metodumuz çalışacaktır. 
Buna Nesne Tabanlı Programlamada bir metodu override etmek denmektedir.

Örneğin artık Çalışan sınıfının init metodunu kullanmak yerine Yönetici sınıfında init metodunu override edebiliriz. 
Böylelikle Yönetici sınıfına ekstra özellikler(attribute) ekleyebiliriz.

class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {\\} \\nMaaş: {\\} \\nDepartman: {\\}\\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
 
class Yönetici(Çalışan):
    
    def __init__(self,isim,maaş,departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı # Yeni eklenen özellik
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {\\} \\nMaaş: {\\} \\nDepartman: {\\}\\nSorumlu Olduğu Kişi Sayısı:{\\}".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))

Python

a = Yönetici("Yavuz Baysan",3000,"Bilişim",10) # Yönetici sınıfının init fonksiyonu. Override edildi.
a.bilgilerigöster()


ÇIKTISI:
    """)
class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
 
class Yönetici(Çalışan):
    
    def __init__(self,isim,maaş,departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişi_sayısı = kişi_sayısı # Yeni eklenen özellik
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu Olduğu Kişi Sayısı:{}".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
a=Yönetici("Yavuz Baysan",3000,"Bilişim",10)
a.bilgilerigoster()
print("""
***************************************************************************************************
super Anahtar Kelimesi
super anahtar kelimesi özellikle override ettiğimiz bir metodun içinde aynı zamanda miras aldığımız bir metodu kullanmak istersek kullanılabilir. 
Yani super en genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan kullanmamızı sağlar.


*******************************************************************************************************************
    """)
print("""
Nesne Yönelimli Programlama – Özel Metodlar
zel metodlar, daha önceden de bahsettiğimiz gibi bizim özel olarak çağırmadığımız ancak her classa ait metodlardır. 
Bunların çoğu biz tanımlamasak bile Python tarafından varsayılan olarak tanımlanır. 
Ancak bu metodların bazılarını da özel olarak bizim tanımlamamız gerekmektedir. 
Daha önceden gördüğümüz init metodu bu metodlara bir örnektir.
********************************************************************************************************************************************
init METODU:
init metodunu kendimiz tanımlarsak artık kendi init fonksiyonumuz çalışacaktır.

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")             -> Örnek Olması İçin bildiğimiz __init__ fonksiyonu,içine atadığımız değerler ile çalışır.
        self.isim = isim 
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")


*************************************************************************************************************************
str METODU:
Normalde print(kitap1) ifadesi ekrana şöyle bir yazı yazdırıyor.


<__main__.Kitap object at 0x000000CEE886EAC8>

Ancak;eğer str metodunu kendimiz tanımlarsak artık ekrana kitap1 in içeriğini daha anlaşılır yazabileceğiz;


class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {\\}\\nYazar: {\\}\\nSayfa Sayısı: {\\}\\nTür: {\\}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)


*************************************************************************************************************************************************
len METODU
len metodu normalde özel olarak biz tanımlamazsak tanımlanan bir metod değil. Onun için bu metodu kendimiz tanımlamamız gereklidir.

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {\\}\\nYazar: {\\}\\nSayfa Sayısı: {\\}\\nTür: {\\}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
 
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(len(kitap1)) # KEndi __len__ metodumuz çağrıldı.

*******************************************************************************************************************************************************************

del METODU
del metodu Pythonda bir objeyi del anahtar kelimesiyle sildiğimiz zaman çalıştırılan metoddur. Bu metodu kendimiz tanımlayarak ekstra özellikler ekleyebiliriz.

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür): 
        print("Kitap Objesi oluşuyor....")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim: {\\}\\nYazar: {\\}\\nSayfa Sayısı: {\\}\\nTür: {\\}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self):
        return self.sayfa_sayısı
    def __del__(self):
        print("Kitap objesi siliniyor.......")
 
kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
 
del kitap1

ÇIKTISI:
Kitap Objesi oluşuyor....
Kitap objesi siliniyor.......
    """)