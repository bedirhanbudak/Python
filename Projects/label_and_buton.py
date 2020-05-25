import sys
from PyQt5 import QtWidgets,QtGui

def Çalıştır():
    uygulama = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Başlık")
    pencere.setGeometry(1500,400,300,300)

    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Bu bir yazıdır.")
    etiket.move(95,30)

    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Bu bir butondur")
    buton.move(90,60)

    resim = QtWidgets.QLabel(pencere)
    resim.setPixmap(QtGui.QPixmap("1.gif"))
    resim.move(80,70)

    pencere.show()
    sys.exit(uygulama.exec_())

Çalıştır()
































