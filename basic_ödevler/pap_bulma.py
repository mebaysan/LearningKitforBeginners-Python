from time import sleep
cumle = "papatyalar çok güzeldir çünkü kızlara benzerler. Ben hep yaylaya çıktığımda papatyaları görürdüm. yaylada hep görürdüm papatyaları güneşin yansımasıyla sar sarı güzel gözükürdü. papatya sevdası böyle başladı bende"
toplam_pap_sayisi = 0 # elimizdeki toplam 'pap' sayılarını bulmak için
sayac = 0 # cumle[0:3] örneğindeki 0 yerine gelen değişken
limit = 3 # cumle[0:3] örneğindeki 3 yerine gelen değişken
uc_harf = "" # debug modunda iterate edilen her 3 harfi görmek için
             # opsiyonel değişken
while sayac <= len(cumle): # len(cumle) -> cumle değişkeninin karakter
                           # sayısını verir.
                        # sayac karakter sayısından küçük olduğu sürece
    uc_harf = cumle[sayac:limit] # debug modunda görmek için (opsiyonel)    
    if cumle[sayac:limit] == "pap": # ilk iter'de cumle[0:3]'e denk gelir
        print("'pap' bulundu")
        toplam_pap_sayisi+=1 # iterate edilen 3 karakter 'pap' ise
                            # sayıyı 1 arttır
    sayac+=1 # her iterde sayacı arttırki diğer 3 harfleri gezsin
    limit+=1 # her iterde limiti arttırki diğer 3 harfleri gezsin

print("Toplam pap sayısı = {}".format(toplam_pap_sayisi))