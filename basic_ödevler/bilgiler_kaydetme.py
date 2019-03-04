print("Bilgilerinizi Kaydettiriniz Lütfen...")

ad=input("Adınızı Giriniz:")
soyad=input("Soyadınızı Giriniz:")
numara=input("Telefon Numaranızı Giriniz:") #Burada neden int kullanmadık diye soracak olursanız buradan gelen değer ile matematiksel işlem yaptırmayacağız,onun için int/float kullanmadık.
bilgi=[ad,soyad,numara]
print("Bilgileriniz aşağıdaki gibidir\nAdınız:{}\nSoyadınız:{}\nNumaranız:{}\n".format(ad,soyad,numara))