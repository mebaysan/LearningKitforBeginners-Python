print("Kök Bulma Programına HoşGeldiniz...")

"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)

"""
a = int(input("Denklemin a değeri:"))

b = int(input("Denklemin b değeri:"))

c = int(input("Denklemin c değeri:"))


delta  = b ** 2 - 4  * a * c

x1  =  (-b - delta ** 0.5)/ (2 * a)

x2 = (-b + delta ** 0.5) / (2 * a)


print("Birinci Kök : {}\nİkinci Kök : {}".format(x1,x2))


