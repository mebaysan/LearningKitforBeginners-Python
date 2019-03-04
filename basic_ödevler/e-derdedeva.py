print("""
****************************************
e-DerdeDeva Programına Hoşgeldiniz
****************************************


# Bu program kendisini geliştirmek için 3 Ocak 2019 tarihinde BAYSAN tarafından yazılmıştır #


** e-DerdeDeva Programı 5 Hastalık üzerine temel seviyede yazılmıştır **

Hastalıklar:

Baş Ağrısı         (h1021)

Ateş               (h1022)

Mide Bulantısı     (h1023)

Soğuk Algınlığı    (h1024)
 
Grip               (h1025)
""")
çıkış="q"
hastalık=input("Hastalığınızın Kodunu Girin : ")
şifayöntemi=int(input("Şifa aracı olarak;\nDoğal Yöntemler için: 1\nİlaçlar için: 2\t tuşlayın: "))
if(hastalık=="h1021" and şifayöntemi==1):
	print("Baş Ağrısı için Doğal Yöntemler;\n1->Lavanta Yağı\n2->Nane Yağı\n3->Fesleğen Yağı\n4->Keten Tohumu\n5->Nane Limon")
elif(hastalık=="h1021" and şifayöntemi==2):
	print("Baş Ağrısı için İlaçlar;\n1->Dolorex\n2->Aspirin\n3->Apranax\n4->Advil")
elif(hastalık=="h1022" and şifayöntemi==2):
	print("Ateş için İlaçlar;\n1->Vermidon\n2->Novalgin\n3->Parol\n4->Minoset\n5->Calpol")
elif(hastalık=="h1022" and şifayöntemi==1):
	print("Ateş için Doğal Yöntemler;\n1->Ilık Suyla Duş Almak\n2->Alnınıza Islak Bez Koymak\n3->Başı ve Boynu Soğutun\n4->Kuru Üzüm Çayı")
elif(hastalık=="h1023" and şifayöntemi==1):
	print("Mide Bulantısı için Doğal Yöntemler;\n1->Bol Su İçmek\n2->Zencefil Çayı\n3->Meyve(Özellikle Muz ve Karpuz)\n4->Leblebi")
elif(hastalık=="h1023" and şifayöntemi==2):
	print("Mide Bulantısı için İlaçlar;\n1->Metpamid\n2->Postadoxine\n3->Kytril\n4->Zofran")
elif(hastalık=="h1024" and şifayöntemi==1):
	print("Soğuk Algınlığı için Doğal Yöntemler;\n1->Sarımsak Kürü\n2->Zencefil\n3->Bal\n4->Tarçın")
elif(hastalık=="h1024" and şifayöntemi==2):
	print("Soğuk Algınlığı için İlaçlar;\n1->Iburamin Zero\n2->Tylolhot Day\n3->Beniflex\n4->Tantum")
elif(hastalık=="h1025" and şifayöntemi==1):
	print("Grip için Doğal Yöntemler;\n1->Kivi\n2->Kuşburnu\n3->Bal\n4->Turunçgiller")
elif(hastalık=="h1025" and şifayöntemi==2):
	print("Grip için İlaçlar;\n1->Coldaway\n2->Panadol\n3->Katarin Plus B\n4->Ibucold")
else:
	print("Yine Bekleriz Geçmiş Olsun...")
