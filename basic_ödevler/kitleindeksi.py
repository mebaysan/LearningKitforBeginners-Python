print("Kitle İndeks Programına HoşGeldiniz ...")
boy=float(input("Boy:")) #Burda neden float yazdık diye soracak olursanız boy ve kilo değerleri ondalıklı olarak yani "."lı girilebilir.Onun için float atadık inputa.
kilo=float(input("Kilo:"))
print("Kitle İndeksiniz Hesaplanıyor...\n ->",kilo/(boy**2))
