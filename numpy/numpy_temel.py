#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:13:11 2019

@author: root
"""

import numpy as np   # numpy kütüphanesini dahil ettik ve np kısaltmasına atadık

a = np.arange(1,15)  # arange -> içine verilen parametreler arası değerleri basar, (15 dahil değil)

b = np.arange(1,15).reshape(2,7)  # .reshape(x,y) -> x kadar satır y kadar sütun

c = np.array([1,3,5,7,8,13,15])  # np.array -> içine verilen liste değerini alır

d = np.linspace(1,10,5)            # np.linspace(x,y,z) -> x ile y arasında rasgele sayılar üretir, z kadar artan sayılar (z parametresi olmak zorunda değil)

 # TEMEL OPERASYONLARI ÖĞRENMEK 
 
x = np.array([20,30,40,50])
 
y = np.arange(4)

y_1 = y**2  # y değerlerinin karesini alır

z = x@y  # x ve y matris çarpımı yaptı
"""
np.ones((x,y)) -> x kadar satır y kadar sütun içinde 1 basar
np.zeros((x,y)) -> x kadar satır y kadar sütun içinde 0 basar
np.random.random((x,y)) -> x kadar satır y kadar sütun içinde 0 ile 1 arasında sayı basar
np.sum(b)    -> içine verilen değerlerin toplamını alır (b değişkeni yukardaki değişken olduğunu varsayarsak sonuç 6 çıkacaktır 0+1+2+3)
np.min(b)    -> verilen parametredeki en küçük değeri al
np.max(b)    -> verilen parametredeki en büyük değeri al
np.sqrt(b)   -> verilen parametrenin karekökünü al
"""
"""
# Dizi birleştirme: stacking
np.vstack((a,b))  -> içine verilen değerleri birleştirir sütun sayısını değiştirmek istemediğimizde
np.hstack((a,b))  -> içine verilen değerleri birleştirir satır sayısını değiştirmek istemediğimizde 
"""
