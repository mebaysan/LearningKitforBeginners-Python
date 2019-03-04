#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 02:12:06 2019

@author: root
"""

import pandas as pd  #Verilere erişmek verilerle uğraşmak
import numpy as np   #Büyük sayılar hesaplamalar
import matplotlib.pyplot as plt   #Veriler için çizimde kullanılan library

# Veri yükleme
dataset=pd.read_csv("satislar.csv")  #pandas read_csv fonksiyonu ile dosyaya erişim sağladık

aylar=dataset.iloc[:,0:1].values  #verileri parçaladık
satislar=dataset.iloc[:,1:2].values #bütün satırları al, 1 ile 2. kolonları al




from sklearn.model_selection import train_test_split #verileri test ve eğitim için böldük
x_train,x_test,y_train,y_test=train_test_split(aylar,satislar,test_size=0.33,random_state=0)


from sklearn.preprocessing import StandardScaler  # Scaler import ettik
sc=StandardScaler()
X_train=sc.fit_transform(x_train)  #Standartlaştırma işlemi uyguladık
X_test=sc.fit_transform(x_test)
Y_train = sc.fit_transform(y_train)
Y_test = sc.fit_transform(y_test)

# model inşası (linear regression)
from sklearn.linear_model import LinearRegression #Doğrusal model oluşturacağımız için burayı import ediyoruz
lr=LinearRegression()
lr.fit(x_train,y_train)

tahmin = lr.predict(x_test)






















