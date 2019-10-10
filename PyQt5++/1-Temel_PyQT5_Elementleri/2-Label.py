import sys
from PyQt5.QtWidgets import *


# from PyQt5.QtWidgets import QLabel
class Wİndow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Label Widget")
        self.setGeometry(1000, 300, 300, 450)
        self.Label()

    def Label(self):
        label1 = QLabel("Hello PyQt5", self)  # self parametresini kullanmazsak pencerede gösteremeyiz
        label1.move(50,50) # x düzleminde 50 px gitsin, y düzleminde 100 px gitsin
        label2 = QLabel("PyQt5 is the very good",self)
        label2.move(50,80)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Wİndow()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
