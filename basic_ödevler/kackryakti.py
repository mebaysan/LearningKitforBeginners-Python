#Bir aracın kilometrede ne kadar yaktığını ve kaç kilometre yol yaptığını alıp kaç kuruş yaktığını bulacağız.
print("Kaç Kuruş Programına HoşGeldiniz...")

yakan_miktar = float(input("Kilometrede yakan miktar:"))

kilometre = float(input("Kaç km yol yaptınız:"))  # Burda da aynı şekilde float kullandık çünkü tam sayı ile kilometre yapamayız her zaman :D ve ayrıca yaktığı miktarda küsüratsız olmaz.

print("Tutar: {} tl".format(yakan_miktar * kilometre))
