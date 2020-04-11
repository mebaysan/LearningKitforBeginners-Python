"""
                   
Formül ->      Z = x̄ - m
              ____________
              standart_sapma
                 ______
                   √n


x̄     -> ölçülen ortalama

m     -> hedeflenen ortalama

Z (α) -> anlamlılık seviyesi

n      -> örneklem sayısı

ss      -> standart sapma (soruda verilir)


|------------------------------|
| Z (α) |  %10  | %5   | %1    |
|------------------------------|
| tek   | 1.28  | 1.64 | 2.33  |
|------------------------------|
| çift  | 1.64  | 1.96 | 2.58  |
|------------------------------|


"""
import math


x = int(input('Ölçülen oranı (x̄) girin: '))
m = int(input('Hedeflenen ortalamayı (m) girin: '))
yon = int(input('Hipotez kaç yönlü? Tek(1)    Çift(2):  '))
z = int(input('Anlamlılık seviyesini Z (α) girin(1-5-10): '))
n = int(input('Örneklem sayısını (n) girin: '))
ss = int(input('Standart sapmayı girin: '))

anlamlilik_deger = 0
if yon == 1 and z == 1:
    anlamlilik_deger = 2.33

elif yon == 1 and z == 5:
    anlamlilik_deger = 1.64

elif yon == 1 and z == 10:
    anlamlilik_deger = 1.28

elif yon == 2 and z == 1:
    anlamlilik_deger = 2.58

elif yon == 2 and z == 5:
    anlamlilik_deger = 1.96

elif yon == 2 and z == 10:
    anlamlilik_deger = 1.64

sonuc = (x - m) / (ss/math.sqrt(n))
cevap = 'H0 hipotezi yanlış'
if -anlamlilik_deger <= sonuc <= anlamlilik_deger:
    cevap = 'H0 hipotezi doğru'
print(f'Anlamlılık Seviyesi -> {z}\nAnlamlılık Değeri -> {anlamlilik_deger}\nSonuç -> {sonuc}\nCevap -> {cevap}')