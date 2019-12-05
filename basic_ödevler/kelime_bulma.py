cumle = "papatyalar çok güzeldir çünkü kızlara benzerler. Ben hep yaylaya çıktığımda papatyaları görürdüm. yaylada hep görürdüm papatyaları güneşin yansımasıyla sar sarı güzel gözükürdü. papatya sevdası böyle başladı bende"
kelimeler = cumle.split(" ")
toplam_sayi = 0
for kelam in kelimeler:
    if kelam == "çok":
        toplam_sayi +=1
print(toplam_sayi)

