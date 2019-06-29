print("Bu dosya Baysan tarafından hazırlanmıştır...\nBaysan ders dosya serisinin python_ders3 dosyasının uygulamalı halidir.")


döngü=input("while döngüsünü öğrenmek için 'while'\nfor döngüsünü öğrenmek için 'for'\nin operatörü için 'in'\nrange fonksiyonu için 'range'\nbreak ifadesi için 'break'\ncontinue ifadesi için 'continue'\nwhile True için 'whiletrue'\nliste fonksiyonlarını görmek için 'liste' girin : ")

if(döngü=="while"):
	print("""while döngüleri belli bir koşul sağlandığı sürece bloğundaki işlemleri gerçekleştirmeye devam eder. 
while döngülerinin sona ermesi için koşul durumunun bir süre sonra False olması gereklidir.""")
	while_işlem=int(input("""While döngüsü ile hangi işlemi yaptırmak istediğinizi girin;
		1-)Döngüde i değerlerini ekrana yazdırma
		2-)Ekrana 40 defa "Python Öğreniyorum" yazdırma
		3-) Liste üzerinde indeks ile gezinme
		İşlem Girin :	"""))
	if(while_işlem==1):
		print("""Döngüde i değerlerini ekrana yazdırmak için:
			i=0                                -> i'ye rastgele değer verdik
			while(i<40):                       -> i 40'tan küçük olduğu sürece dedik
				print("i'nin değeri : ",i)     -> i 40'tan küçük olduğu sürece içeriyi print et dedik
				i+=1                           -> i her işlemde 1 artsın dedik                                  """)                        
		i=0
		while(i<40):
			print("i'nin değeri : ",i)
			i+=1
	elif(while_işlem==2):
		print(""" Ekrana 40 defa Python Öğreniyorum Yazdırmak için:
			i=1
			while(i<=40):
				print("Python Öğreniyorum")
				i+=1   """)
		i=0
		while(i<=40):
			print("Python Öğreniyorum")
			i+=0
	elif(while_işlem==3):
		print("""Liste üzerinde indeks ile gezinmek için:
			      liste = [1,2,3,4,5]                     -> liste oluşturuyoruz
                  a = 0                                   -> tekrar while döngüsü içine atacağımız bir değer oluşturuyoruz
                  while (a < len(liste)):                 -> a değeri listenin eleman sayısından küçük olduğu sürece dedik
                  print("Indeks:",a,"Eleman:",liste[a])   -> a değeri listenin eleman sayısından küçük olduğu sürece print et dedik
                  a +=1                                   -> a her işlemde 1 artsın dedik  """)
		liste=[1,2,3,4,5]
		a=0
		while(a<len(liste)):
			print("İndeks:",a,"Eleman:",liste[a])
			a+=1
elif(döngü=="for"):
	print("""for Döngüsü , listelerin ,demetlerin, stringlerin ve hatta sözlüklerin üzerinde dolaşmamızı sağlayan bir döngü türüdür.""")
	for_işlem=int(input("""for döngüsü ile hangi işlemi yaptırmak istersiniz;
		1-)Liste elemanlarını bastırma
		2-)Liste elemanlarını toplama
		3-)Liste elemanlarından çift olanlarını ekrana bastırma
		İşlem Seçin :                          """))
	if(for_işlem==1):
		print("""Liste elemanlarını ekrana bastırmak için :
			liste=[1,2,3,4,5,6]               -> liste oluşturduk
			for eleman in liste:              -> eleman bizim atadığımız değişken ister "x" ister "asd" ister "başkabirşey" olsun
				print("Eleman:",eleman)       -> for eleman in liste: koşulu sağlandığı sürece bunu bastır dedik                   """)
		liste=[1,2,3,4,5,6]
		for eleman in liste:
			print("Eleman :",eleman)
	elif(for_işlem==2):
		print("""Liste elemanlarını toplamak için : 
			liste=[1,2,3,4,5,6,7,8]       -> liste oluşturduk
			toplam=0                     -> toplam değişkeni oluşturduk
			for eleman in liste:         -> eleman bizim atadığımız değişken ister "x" ister "asd" ister "başkabirşey" olsun
				toplam+=eleman           -> toplam değerine sıfır verdik çünkü her seferinde 2. eleman ile kendisini toplayıp ekrana toplamı versin istiyoruz
				print("Toplam :",toplam  -> yukardaki for eleman in liste sağlandığı sürece ekrana toplamı bastır dedik                                    """)
	elif(for_işlem==3):
		print("""Liste elemanlarından çift olanlarını ekrana bastırmak için :
			liste=[1,2,3,4,5,6,100,24,16,198,20,34,56,55]    -> liste oluşturduk
			for eleman in liste:                             -> eleman bizim atadığımız değişken ister "x" ister "asd" ister "başkabirşey" olsun
				if eleman % 2 = 0:                           -> burda if ifadesini kullandık ve dedik ki eğer eleman %2=0 ise yani yüzde 2si 0a eşitse(bu çift demek)
					print("Çift olan eleman:",eleman)        -> yukardaki koşulu sağlayan durumları ekrana bastır """)
elif(döngü=="in"):
	print("""in operatörü , bir elemanın başka bir listede,demette veya stringte (karakter dizileri) bulunup bulunmadığını kontrol eder. 
             eğer listenin içinde varsa True yoksa False döner
             kullanımı oldukça basittir;
             liste=[1,2,3,4,5]
             print(4 in liste)    """)
	liste=[1,2,3,4,5]
	print(4 in liste,"\nBir de olmadığı durumları görelim,\n print(6 in liste)",6 in liste)
elif(döngü=="range"):
	print(""" Pythondaki bu hazır fonksiyon bizim verdiğimiz değerlere göre range isimli bir yapı oluşturur
     ve bu yapı listelere oldukça benzer. Bu yapı başlangıç, bitiş ve opsiyonel olarak artırma değeri alarak
     listelere benzeyen bir sayı dizisi oluşturur.
     UNUTULMAMALIDIR Kİ range FONKSİYONUNU KULLANIRKEN BAŞINA MUTLAKA '*' KONULMALIDIR!
     Kullanımlarını görmeye başlayabiliriz.
     1-) print(*range(15)) # Başlangıç değeri vermediğimiz 0'dan başlar
     2-) print(*range(5,20,2))  # 5'ten 20'ye kadar olan sayıları 2 atlayarak yazar
     3-) print(*range(20,0))    # 20'den geri gelen sayıları oluşturmaz.
     4-) print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.
     5-) liste=list(range(0,20))# list fonksiyonu ile listeye dönüştürebiliriz   
     6-) for sayı in range(1,20)# for döngüsü ve range fonksiyonunun birlikte kullanımı            """)
	range_işlem=int(input("Nasıl kullanıldığını görmek için bir işlem seçiniz : "))
	if(range_işlem==1):
		print("""print(*range(15)) # Başlangıç değeri vermediğimiz 0'dan başlar
			print(*range(15))   """)
		print(*range(15))
	elif(range_işlem==2):
		print("""print(*range(5,20,2))  # 5'ten 20'ye kadar olan sayıları 2 atlayarak yazar
			print(*range(5,20,2))   """)
		print(*range(5,20,2))
	elif(range_işlem==3):
		print("""print(*range(20,0))    # 20'den geri gelen sayıları oluşturmaz.
			print(*range(20,0))  """)
		print(*range(20,0))
	elif(range_işlem==4):
		print("""print(*range(20,0,-1)) # 20'den geri gelen sayıları oluşturur.
			print(*range(20,0,-1)) """)
		print(*range(20,0,-1))
	elif(range_işlem==5):
		print("""liste=list(range(0,20))# list fonksiyonu ile listeye dönüştürebiliriz
			liste=list(range(0,20))
			print(liste)  """)
		liste=list(range(0,20))
		print(liste)
	elif(range_işlem==6):
		print("""for sayı in range(1,20)# for döngüsü ve range fonksiyonunun birlikte kullanımı 
			for sayı in range(1,20):
			print("*"*sayı)    """)
		for sayı in range(1,20):
			print("*"*sayı)
elif(döngü=="break"):
	print("""Döngü herhangi bir yerde ve herhangi bir zamanda break ifadesiyle karşılaştığı zaman
         çalışmasını bir anda durdurur. Böylelikle döngü hiçbir koşula bağlı kalmadan
         break ifadesi sadece ve sadece içindeki bulunduğu döngüyü sonlandırır. Eğer iç içe döngüler bulunuyorsa ve
         en içteki döngüde break kullanılmışsa sadece içteki döngü sona erer.
         nasıl kullanıldığına kısaca bakalım : \n


         i=0                     -> kendimize örneğimiz için bir i değişkeni oluşturalım
         while(i<20):            -> i 20'den küçük olduğu sürece dedik
         	print(i)             -> yukardaki koşul sağlandığı süre boyunca ekrana i bas dedik
         	if(i==10):           -> eğer i 10'a eşit olursa 
         		break            -> yukardaki koşul sağlanırsa döngüyü sonlandır dedik
         	i+=1                 -> i her seferinde 1 artsın dedik                                      """)
	i=0
	while(i<20):
		print(i)
		if(i==10):
			break
		i+=1
elif(döngü=="continue"):
	print("""Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle karşılaştığı zaman geri kalan işlemlerini
             yapmadan direk bloğunun başına döner.
             Kullanımını kısaca görelim :
             liste=[1,2,3,4,5,6,7,8]   -> liste oluşturduk
             for i in liste:           -> i bizim atadığımız değişken ister "x" ister "asd" ister "başkabirşey" olsun
             	if(i==3 or i==5):      ->eğer i 3'e veya 5'e eşit olursa dedik
             		continue           -> yukardaki koşul sağlanırsa döngünün başına döner(yani koşulun sağlandığı basamağı atlar devam eder)
             	print("i:",i)          -> yukardaki koşullar sağlandığında i değerini ekrana bas             """)
	liste=[1,2,3,4,5,6,7,8]
	for i in liste:
		if(i==3 or i==5):
			continue
		print("i:",i)
elif(döngü=="whiletrue"):
	print(""" while True:  bu kod herhangi bir yerde break kullanılmamışsa sonsuza kadar çalışır.
		kısaca kullanımını görelim:
		while True:
			liste=[1,2,3,4,5]
			for i in liste:
				print(i)                """)
	while True:
			liste=[1,2,3,4,5]
			for i in liste:
				print(i,"Sonsuz döngüye girdiği bunun için for i in liste altına if(i<3): break i+=1 print(i) döngüyü sonlandırabilir ")
elif(döngü=="liste"):
	liste_işlem=int(input(""" List Comprehension
		1-) Listelerde append metodunu hatırlayalım.
		2-) Liste1'den Liste2'yi oluşturalım
		3-) [i for i in liste1]  list comprehension
		4-) [i*2 for i in liste1] list comprehension 
		5-) [i*j for (i,j) in liste1] list comprehension
		6-) [i for i in liste1 if not (i == 4 or i == 9)] list comprehension                                        

		Listelerle ilgili hangi işlemi yapmak istediğinizi seçin :"""))
	if(liste_işlem==1):
		print("""listelerde append metodunu hatırlayalım. liste2=list() veya liste1=[] ikiside liste oluşturur.
              liste1=list()       -> boş liste oluşturduk. liste1 içine değer atamadık ama liste1'in liste olduğunu belirledik.İlerde bunların içine .append metodu ile değerler atayabiliriz.
              liste2=[]           -> boş liste oluşturduk. liste2 içine değer atamadık ama liste2'nin liste olduğunu belirledik.İlerde bunların içine .append metodu ile değerler atayabiliriz.
              append metodu ile eleman eklemek için :
              liste1=[1,2,3,4,5]         -> Liste oluşturduk ve içine değerleri atadık
              liste1.append(6)           -> .append() metodu ile liste1'in içine atamak istediğimiz değeri yazdık
              print(liste1 : """)        
		liste1=[1,2,3,4,5]
		liste1.append(6)
		print(liste1)
	elif(liste_işlem==2):
		print("""liste1'den liste2'yi oluşturalım.
			liste1=[1,2,3,4,5]            -> liste oluşturduk
			liste2=list()                 -> boş liste oluşturduk içine değer atamadık liste2'nin liste olduğunu belirledik
			for i in liste1:              -> for döngüsünü liste1 için kurduk
				liste2.append(i)          -> for döngüsü yardımıyla liste2'nin içine liste1'in elemanlarını atadık
			print(liste2)                                """)
		liste1=[1,2,3,4,5]
		liste2=list()
		for i in liste1:
			liste2.append(i)
		print(liste2)

	elif(liste_işlem==3):
		print(""" [i for i in liste1] metodu
			liste1=[1,2,3,4,5]
			liste2=[i for i in liste1]
			print(liste2)""")
		liste1=[1,2,3,4,5]
		liste2=[i for i in liste1]
		print(liste2)
	elif(liste_işlem==4):
		print("""[i*2 for i in liste1] 
			liste1=[1,2,3,4,5]
			liste2=[i*2 for i in liste1]
			print(liste2)    """)
		liste1=[1,2,3,4,5]
		liste2=[i*2 for i in liste1]
		print(liste2)
	elif(liste_işlem==5):
		print(""" [i*j for (i,j) in liste1]

			liste1 = [(1,2),(3,4),(5,6)] 
			liste2 = [i*j for (i,j) in liste1]
			print(liste2)                   			""")
		liste1 = [(1,2),(3,4),(5,6)] 
		liste2 = [i*j for (i,j) in liste1]
		print(liste2)
	elif(liste_işlem==6):
		print("""[i for i in liste1 if not (i == 4 or i == 9)]


			liste1 = [1,2,3,4,5,6,7,8,9,10] 
			liste2 = [i for i in liste1 if not (i == 4 or i == 9)]
			print(liste2)                    """)
		liste1 = [1,2,3,4,5,6,7,8,9,10] 
		liste2 = [i for i in liste1 if not (i == 4 or i == 9)]
		print(liste2)                    