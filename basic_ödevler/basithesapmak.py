print("""*************************
Basit Hesap Makinesi Programı

İşlemler;
1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi
*************************
	""")

a=int(input("Birinci Sayı:"))
b=int(input("İkinci Sayı:"))
işlem=input("İşlemi giriniz:")
if (işlem=="1"):
	print("{} ile {} toplamı = {}".format(a,b,a+b))
	pass
elif(işlem=="2"):
	print("{} ile {} farkı = {}".format(a,b,a-b))
elif(işlem=="3"):
    print("{} ile {} çarpımı = {}".format(a,b,a*b))
elif(işlem=="4"):
	print("{} ile {} bölümü = {}".format(a,b,a/b))
else:
	print("Geçersiz İşlem")
