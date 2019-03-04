#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 00:11:17 2019

@author: root
"""
# Yan tarafta verilerin olduğu dizini açtık
#Kütüphaneleri dahil ettik
import pandas as pd  #Verilere erişmek verilerle uğraşmak
import numpy as np   #Büyük sayılar hesaplamalar
import matplotlib.pyplot as plt   #Veriler için çizimde kullanılan library

# Veri yükleme
dataset=pd.read_csv("eksikveriler.csv")  #pandas read_csv fonksiyonu ile dosyaya erişim sağladık

# Veri Ön İşleme
# Kolon adına göre verileri almak
boy = dataset[["boy"]]  # hangi kolonu alacaksak atayacağımız değişken'e [[ ]] içinde kolon adını veriyoruz

boykilo= dataset[["boy","kilo"]]

# EKSİK VERİLER
from sklearn.preprocessing import Imputer  # sklearn altındaki preprocessing kütüphanesindeki Imputer fonksiyonu
imputer=Imputer(missing_values="NaN", strategy="mean", axis=0) #Sırasıyla -> nan değerleri, orta strateji, 0 bazında
yas=dataset.iloc[:,1:4].values  #iloc fonksiyonu hangi kolonları almak istediğimizi belirtir, 1'den başla 4. kolona kadar değerleri al dedik(4dahil değil)
imputer=imputer.fit(yas[:,1:4]) #.fit diyerek yukardaki stratejiyi uyguluyoruz. yas kolonunda bulunan ve sütun kısmında 1-4 arası değerleri al
yas[:,1:4]=imputer.transform(yas[:,1:4]) #yas değişkenine imputer.transform ile yeni değerleri atıyoruz. ortalaması alınıyor.

#Kategorik Veriler
#encoder: Categoric -> Numeric

ulke = dataset.iloc[:,0:1].values #sadece ülke kolonunu aldık
from sklearn.preprocessing import LabelEncoder #Her değer için sayısal değer koyan encoder
le=LabelEncoder()   #label encoder'dan bir obje oluşturduk
ulke[:,0]=le.fit_transform(ulke[:,0])  #ulke objesinin 0. kolonunu al bunu fit et ve transform et dedik(0. kolonun sebebi tek kolon olması,pythonda indexler 0 dan başlar)

from sklearn.preprocessing import OneHotEncoder #diğer encoderi dahil ettik kolon bazlı bir encoderdir
ohe=OneHotEncoder(categorical_features="all") #OneHotEncoderdan obje oluşturduk ve all diyerek bütün değerleri aldırdık
ulke=ohe.fit_transform(ulke).toarray() #ulke objesinin ohe ile fit_transform olmasını söyledik içine encode etmek istediğimiz parametreyi koyduk ve toarray diyerek işlemi bitirdik

#Veri Kümelerinin birleştirilmesi ve DataFrame / Numoy dizileri dataframe dönüşümü

sonuc=pd.DataFrame(data=ulke,index=range(22),columns=["fr","tr","us"]) #pandas DataFrame fonk kullandık.içine parametre olarak data,index,columns veriyoruz.Kolon isimleri,indexlerin numaraları 22 olma sebebi 0-21=22satır

sonuc2=pd.DataFrame(data=yas,index=range(22),columns=["boy","kilo","yas"])

cinsiyet=dataset.iloc[:,-1:].values  #cinsiyet kolonunu aldık

sonuc3=pd.DataFrame(data=cinsiyet,index=range(22),columns=["cinsiyet"])

a=pd.concat([sonuc,sonuc2],axis=1)  #pandas concat fonk ile sonuc ve sonuc2 verilerini axis=1'de birleştirdik.
a2=pd.concat([a,sonuc3],axis=1)     # sonuc3 ve a verilerini birleştirdik

#Veri Kümesinin Bölünmesi (Test-Eğitim)
from sklearn.model_selection import train_test_split  #veri kümesini bölmek için kullanacağımız kütüphaneler

x_train,x_test,y_train,y_test = train_test_split(a,sonuc3,test_size=0.33,random_state=0)
# x ve y'ler bizim belirlediğimiz değişkenler. test_size=0.33 olmasının sebebi literatürdeki teste 1/3 eğitim için 2/3 olması. random_state=0 'da verinin nasıl bölüneceği(random karıştırarak bölmesi)
 

#ÖZNİTELİK ÖLÇEKLEME / Veriler Ölçeklendi (Standartlaştırma)
from sklearn.preprocessing import StandardScaler  #kütüphaneleri import ettik. standartlaştırma olayını gerçekleştirdik
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.fit_transform(x_test)





















