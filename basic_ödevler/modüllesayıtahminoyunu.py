import time
import random


print("""******************************

Sayı Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin edin.

Toplam Deneme Hakkınız 7'dir.
*************************************""")
rastgelesayı=random.randint(1,40)                       #Random modülü içindeki randit fonksiyonu -> bu fonksiyon bize içine verdiğimiz değerler arasında random bir sayı üretir
tahminhakkı= 7

while True:
    tahmin=int(input("Tahmininiz:"))

    if(tahmin<rastgelesayı):
        print("Bilgiler Sorgulanıyor...")
 
        time.sleep(1)                                   #time modülü içindeki sleep fonksiyonu-> içinde verdiğimiz değer kadar saniye bekler

        print("Daha yüksek bir sayı söyleyin")

        tahminhakkı-=1                                  #tahmin her yanlış olduğunda tahmin hakkı 1 azalacak
        print("Kalan tahmin hakkınız:",tahminhakkı)

    elif(tahmin>rastgelesayı):
        print("Bilgiler Sorgulanıyor...")

        time.sleep(1)

        print("Daha küçük bir sayı söyleyin")

        tahminhakkı-=1
        print("Kalan tahmin hakkınız:",tahminhakkı)

    else:
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler Doğru Sayınız:",rastgelesayı)
        break
    if(tahminhakkı==0):
        print("Tahmin Hakkınız Bitti...")
        print("Doğru Sayı:",rastgelesayı)
        break
        
