import sys  # bunu dahil etmemizin sebebi app çalıştırmamıza yardım edecek
from PyQt5 import QtWidgets,QtGui     #pencere vs oluşturmak için QtWidgets dahil ettik, resim falan eklemek için QtGui

def Pencere():          # Burda fonksiyon ile yapıyı kurmaya başlıyoruz.
    app = QtWidgets.QApplication(sys.argv)  # mutlaka bir uygulama oluşmalıdır.
    
    pencere = QtWidgets.QWidget()   # QtWidgets içinden QWidget ile pencere objesini oluşturduk
    pencere.setWindowTitle("PyQt5 Ders 1 Pencere oluşturma")    # Pencere objesinin başlığını belirliyoruz
    
    okay = QtWidgets.QPushButton("Tamam")  # tamam ve iptal butonu oluşturduk
    cancel = QtWidgets.QPushButton("İptal")
            #QtWidgets.QWBoxLayout() yaparsak vertical box oluştururuz ve onlar yatay olarak üste yapışırlar. stretch'i önce koyarsak yukarı sonra koyarsak aşağı yapışırlar
    h_box = QtWidgets.QHBoxLayout() # horizontal box oluşturduk
    h_box.addWidget(okay) # butonlarımızı horizontal box'a ekledik
    h_box.addWidget(cancel)
    h_box.addStretch()   # butonları sol tarafa yasladık (bunu butonlardan önce koysaydık sağa yaslayacaktı butonları)
    pencere.setLayout(h_box)   # horizontal boxu pencereye ekledik
    

    buton = QtWidgets.QPushButton(pencere)  #buton objesi oluşturduk ve bunu pencereye ekledik.
    buton.setText("Burası bir butondur..")  # butona text yazdık
    

    etiket1 = QtWidgets.QLabel(pencere) # pencereye yazı ekliyoruz parametre olarak pencere objesini veriyoruz ki etiket1 pencereye yapışsın
    etiket2=QtWidgets.QLabel(pencere)
    
    etiket2.setPixmap(QtGui.QPixmap("python.png"))  #resmi dahil ettik, pencereye yapıştırdık(aynı dizinde olmalı)
    etiket1.setText("Burası Yazıdır...")    # etiket1'e yazı değeri ekledik
    
    etiket2.move(100,50)        # etiket2'yi hareket ettiriyoruz
    etiket1.move(200,10)   # etiket1 'i taşımak için move fonksiyonu kullanılır
    buton.move(175,400)     # buton hareket ettiriyoruz
    
    pencere.setGeometry(400,150,500,500) # sol 2 nereden başlayacağını gösteriyor x,y eksen / sağ 2 ne büyüklükte olacağını gösteriyor
    pencere.show()      # pencere objesini bu uygulamada gösteriyoruz
    sys.exit(app.exec_())       # uygulamayı döngüye sokuyoruz. Çarpı tuşuna basmadığımız sürece uygulamamız çalışıyor


Pencere()  # Pencere fonksiyonumuzu çalıştırdık.