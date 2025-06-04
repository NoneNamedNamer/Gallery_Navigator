import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton

class GalleryWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Gallery")
        self.setFixedSize(640,480)

        layout = QGridLayout()
        self.setLayout(layout)      

        label1 = QLabel("Gallery")
        label1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label1.setMargin(100)
        layout.addWidget(label1, 0, 0)

        buttonBack = QPushButton("Back")
        buttonBack.setGeometry(200,150,100,40)
        buttonBack.clicked.connect(self.buttonBack_clicked)
        layout.addWidget(buttonBack, 1, 0)

    def buttonBack_clicked(self):
        from interfaceMain import MainWindow
        print("Going back to Main Menu.")
        self.mw = MainWindow()
        self.mw.show()
        self.close()