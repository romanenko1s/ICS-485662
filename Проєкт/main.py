import pandas as pd
import matplotlib as ml
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

### WORKING WITH DATA BASES ###

excelPath = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/Проєкт/curencyData.xls"

dataFile1 = pd.read_excel(excelPath)
dataFile2 = pd.DataFrame(dataFile1, index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
dataFile = str(dataFile2)

### WORKING WITH THE APP ###

class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()


        self.setWindowTitle("Зараз")
        self.setGeometry(300, 250, 600, 450)

        self.title = QtWidgets.QLabel(self)
        self.title.setText("Зараз")
        self.title.move(275,50)
        self.title.adjustSize()

        self.button3 = QtWidgets.QPushButton(self)
        self.button3.move(275, 100)
        self.button3.setText("Вивести графік")
        self.button3.setFixedWidth(200)
        self.button3.clicked.connect(self.button3Action)

    def button3Action(self):
        print("hello")

### Launching App ###

def appplication():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

appplication()