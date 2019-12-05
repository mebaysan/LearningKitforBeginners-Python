from math import sqrt
sayilar = list()
toplam = 0
toplam_kare_sapma = 0
for i in range(1,6):
    sayi = int(input("Sayı girin:\t"))
    toplam+=sayi
    sayilar.append(sayi)

a_o = toplam/(len(sayilar))
for sayi in sayilar:
    sapma = sayi - a_o
    kare_sapma = sapma ** 2
    toplam_kare_sapma += kare_sapma

varyans = toplam_kare_sapma / (len(sayilar))
standart_sapma = sqrt(varyans)
print("Girdiğiniz 5 sayının standart sapması = {}".format(standart_sapma))