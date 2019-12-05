aranan_harf = input("Harf girin:")
toplam_aranan_harf = 0   

cumle = input("Cümle girin:")

for harf in cumle:
    if harf == aranan_harf:
        toplam_aranan_harf+=1
    
print("Aradığınız {} harfi cümle içerisinde {} kere geçmektedir.".format(aranan_harf,toplam_aranan_harf))