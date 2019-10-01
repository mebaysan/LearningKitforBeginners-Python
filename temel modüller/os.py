import os

result = dir(os)  # os modülü içerisindeki her şey

result = os.name  # işletim sistemini verir
result = os.getcwd()  # dosyanın çalıştığı dizini verir
os.mkdir("yeni_dizi")  # dosyanın çalıştığı dizine klasör açar
os.makedirs("newdirectory/yeni_klasör")  # iç içe klasörler oluşturur
os.rename("newdirectory", "yeniklasor")  # isim değişikliği yapabiliriz. ilk parametre değişecek klasor adı
os.rmdir("newdirectory")  # klasör siler
os.removedirs("newdirectory/yeniklasor")  # alt dizinler dahil hepsini siler klasör boş olmalıdır
os.chdir('C:\\');  # dosyanın dizinini değiştirir
os.chdir('..')  # üst klasöre çıkar
os.listdir()  # etkin olduğu klasör içerisindeki dosyalar listelenir istersek path verebiliriz
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)  # sonu .py ile biten dosyaları yazar

result = os.stat("imdb.py")  # içine verdiğin dosyanın bilgilerini verir

os.system("notepad.exe")  # sistem üzerinde komut çalıştırabiliriz

result = os.path.abspath("os.py")  # içine verdiğimiz dosyanın tam konumunu verir bize
result = os.path.dirname("C:/Desktop/modules/deneme.py")  # konumu verilen dosyanın dizin adını alır
result = os.path.dirname(os.path.abspath("os.py"))  # dosyamızın tam yolunu veriyor ve dizin adını verir. adını bildiğimiz fakat yolunu bilmediğimiz dosyalar için
result = os.path.exists("os.py")  # içine verdiğimiz dosyanın veya klasörün varlığını kontrol eder
result = os.path.isdir("temel_moduller") # yolunu verdiğimiz parametre bir klasör mü
result = os.path.isfile("os.py") # verdiğimiz yol bir dosya mı değil mi
result = os.path.join("C:\\","deneme") # iki dizini birleştirmeye yarar. 3 parametre de verebiliriz
result = os.path.split("C:\\deneme") # bu şekildede tam yolu verilen bir parametreyi parçalayabiliriz
result = os.path.splitext("os.py") # dosyanın ismi ve uzanyısını ayırır
