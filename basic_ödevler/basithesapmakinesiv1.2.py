
#V1.2'nin tek özelliği; v1.1'deki gereksiz işlem değişkeninden kurtulmaktır...

print("""*************************
Basit Hesap Makinesi Programı v1.1 Güncellenmiş Sürüm ile Kendini Denemeye Hazır mısın? :)

İşlemler;
1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi
*************************
	""")
print("Hazırsan başlayalım. Senden birkaç şey isteyeceğim...")

birincisayi=int(input("Birinci Sayı:"))
ikincisayi=int(input("İkinci Sayı:"))
işlem=int(input("İşlemi giriniz:"))
tahmin=float(input("Şimdi Tahminleri Alma Zamanı. Tahminin Nedir : "))

if(işlem==1 and tahmin==birincisayi+ikincisayi):
	print("{} + {} = {} ".format(birincisayi,ikincisayi,birincisayi+ikincisayi),"Tebrikler Doğru Tahmin")
elif(işlem==2 and tahmin==birincisayi-ikincisayi):
	print("{} - {} = {} ".format(birincisayi,ikincisayi,birincisayi-ikincisayi),"Tebrikler Doğru Tahmin")
elif(işlem==3 and tahmin==birincisayi*ikincisayi):
	print("{} x {} = {} ".format(birincisayi,ikincisayi,birincisayi*ikincisayi),"Tebrikler Doğru Tahmin")
elif(işlem==4 and tahmin==birincisayi/ikincisayi):
	print("{} / {} = {} ".format(birincisayi,ikincisayi,birincisayi/ikincisayi),"Tebrikler Doğru Tahmin")
elif(işlem==1 and tahmin!=birincisayi+ikincisayi):
	print("{} + {} = {} ".format(birincisayi,ikincisayi,birincisayi+ikincisayi),"Üzgünüm Yanlış Tahmin")
elif(işlem==2 and tahmin!=birincisayi-ikincisayi):
	print("{} - {} = {} ".format(birincisayi,ikincisayi,birincisayi-ikincisayi),"Üzgünüm Yanlış Tahmin")
elif(işlem==3 and tahmin!=birincisayi*ikincisayi):
	print("{} x {} = {} ".format(birincisayi,ikincisayi,birincisayi*ikincisayi),"Üzgünüm Yanlış Tahmin")
elif(işlem==4 and tahmin!=birincisayi/ikincisayi):
	print("{} / {} = {} ".format(birincisayi,ikincisayi,birincisayi/ikincisayi),"Üzgünüm Yanlış Tahmin")
else:
	print("Geçersiz İşlem")
