import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton

from galleryWindow import GalleryWindow

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Image management")
        self.setFixedSize(640,480)

        layout = QGridLayout()
        self.setLayout(layout)      

        label1 = QLabel("Main Menu")
        label1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label1.setMargin(100)
        layout.addWidget(label1, 0, 0)

        button1 = QPushButton("Something")
        button1.setGeometry(200,150,100,40)
        button1.clicked.connect(self.button1_clicked)
        layout.addWidget(button1, 1, 0)

        buttonQuit = QPushButton("Quit")
        buttonQuit.setGeometry(200,150,100,40)
        buttonQuit.clicked.connect(self.buttonQuit_clicked)
        layout.addWidget(buttonQuit, 2, 0)

    def button1_clicked(self):
        print("Going to Gallery window and closing current window.")
        self.gw = GalleryWindow()
        self.gw.show()
        self.close()
    
    def buttonQuit_clicked(self):
        print("Application is closed.")
        sys.exit(0)

def wrapAyo():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())