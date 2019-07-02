import os
import glob
from xml.etree import ElementTree as et


os.getcwd() # program çalışan dizinde çalıştırdık


liste = list()

for file in glob.glob("*.xml"): # uzantısı .xml olan tüm dosyaları alır
    liste.append(file) # yakaladığımız dosyaları oluşturduğumuz listeye ekliyoruz

liste_eleman = len(liste) # döngüde lazım olacak
dosya_icerigi = str()
flag = 0
iter = 0
file2 = open("yeniExcel.xml", "w", encoding="UTF-8") # yeni bir dosya okuyoruz
mevcut_dizin = os.getcwd() # şuanki bulunduğumuz dizini alıyoruz
for i in liste:
    print(mevcut_dizin+"\\"+i) # dizin sonuna dosya adını ekliyoruz
    with open(i, "r", encoding="UTF-8") as file: # listeden gelen dosyayı açıyoruz
        for j in file: # dosya içindeki satırları okuyoruz
            if iter!=liste_eleman:
                j=j[:-660] # son 660'ı alma dedik (bu program yazdıldığındaki gereksinimlerden dolayı yazılmış bir kod)
            if flag==0:
                file2.write(j+"\n")
                flag=1
            else:
                file2.write(j[6131:]) # ilk 6131. satırı al diyoruz (bu program yazdıldığındaki gereksinimlerden dolayı yazılmış bir kod)
            iter= iter+1

            #print(j+"\n")


