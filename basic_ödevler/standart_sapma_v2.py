from math import sqrt
def standart_sapma_bul(sayilar):
    toplam = 0
    toplam_kare_sapma = 0
    for i in sayilar:
        sayi = i
        toplam+=sayi
        i+=1

    a_o = toplam/(len(sayilar))
    for sayi in sayilar:
        sapma = sayi - a_o
        kare_sapma = sapma ** 2
        toplam_kare_sapma += kare_sapma

    varyans = toplam_kare_sapma / (len(sayilar))
    standart_sapma = sqrt(varyans)
    print("Girdiğiniz {} sayının standart sapması = {}".format(len(sayilar),standart_sapma))

standart_sapma_bul([2,4,6,8,10,12])