import sys
from PyQt5.QtWidgets import *

class Window(QWidget): # QWidget class'ından inherit edilmeli
    def __init__(self):
        super().__init__()
        self.setGeometry(1000,300,300,450) # pencerenin yerini ve boyutunu ayarlar. 1. parametre -> x düzleminde yeri, 2. parametre -> y düzleminde yeri, 3. parametre genişlik, 4. parametre yükseklik
        self.setWindowTitle("Burası pencere başlığıdır") # pencere başlığını belirler
        self.show() #pencereyi görünür yapar
    

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
