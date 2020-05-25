import sys
from  PyQt5 import QtWidgets

def Open():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Esnek Butonlar")
    pencere.setGeometry(1500,400,300,300)

    okay = QtWidgets.QPushButton("Onayla")
    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere.setLayout(v_box)



    pencere.show()
    sys.exit(app.exec_())

Open()