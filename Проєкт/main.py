import pandas as pd
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import xlrd

### WORKING WITH DATA BASES ###

excelPath1 = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/Проєкт/curencyData.xls"
excelPath3 = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/Проєкт/curencyData3.xls"

dataExcelFile1 = pd.read_excel(excelPath1)
dataExcelFile12 = pd.DataFrame(dataExcelFile1, index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
dataFile = str(dataExcelFile12)

### MINOR WINDOWS ###



### WORKING WITH THE MAIN WINDOW ###

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 427)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 600, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setStyleSheet("background-color: rgb(245, 194, 17);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(225, 100, 150, 40))
        self.pushButton.setStyleSheet("background-color: rgb(246, 245, 244);\n""color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        #self.pushButton.clicked.connect(self.button1Action)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(225, 150, 150, 40))
        self.pushButton_2.setStyleSheet("background-color: rgb(246, 245, 244);\n""color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        #self.pushButton_2.clicked.connect(self.button2Action)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(225, 200, 150, 40))
        self.pushButton_3.setStyleSheet("background-color: rgb(246, 245, 244);\n""color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.button3Action)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(225, 250, 150, 40))
        self.pushButton_4.setStyleSheet("background-color: rgb(246, 245, 244);\n""color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        #self.pushButton_4.clicked.connect(self.button4Action)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(225, 300, 150, 40))
        self.pushButton_5.setStyleSheet("background-color: rgb(246, 245, 244);\n""color: rgb(0, 0, 0);")
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 603, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Зараз"))
        self.title.setText(_translate("MainWindow", "Зараз"))
        self.pushButton.setText(_translate("MainWindow", "Курс валют"))
        self.pushButton_2.setText(_translate("MainWindow", "Номера валют"))
        self.pushButton_3.setText(_translate("MainWindow", "Графік валют"))
        self.pushButton_4.setText(_translate("MainWindow", "Вивести в ексель"))
        self.pushButton_5.setText(_translate("MainWindow", "Вихід"))

    def button1Action(self):
        pass

    def button2Action(self):
        pass

    def button3Action(self):

        dataExcelFile3 = pd.read_excel(excelPath3)
        y1 = dataExcelFile3.iloc[0]
        plt.plot(y1)
        y2 = dataExcelFile3.iloc[1]
        plt.plot(y2)
        y3 = dataExcelFile3.iloc[2]
        plt.plot(y3)
        y4 = dataExcelFile3.iloc[3]
        plt.plot(y4)
        y5 = dataExcelFile3.iloc[4]
        plt.plot(y5)
        y6 = dataExcelFile3.iloc[5]
        plt.plot(y6)

        plt.show()
    
    def button4Action(self):
        pass

### STARTING APP ###

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  