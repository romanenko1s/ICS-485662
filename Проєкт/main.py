import pandas as pd
from matplotlib import *
import matplotlib.pyplot as plt
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import xlrd
from menu import Ui_nowMenu
from window1 import Ui_window1
from window2 import Ui_window2

### WORKING WITH DATA BASES ###

excelPath1 = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/Проєкт/curencyData.xls"
excelPath3 = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/Проєкт/curencyData3.xls"

dataExcelFile1 = pd.read_excel(excelPath1)
dataExcelFile12 = pd.DataFrame(dataExcelFile1, index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
dataFile = str(dataExcelFile12)

### STARTING APP ###

app = QtWidgets.QApplication(sys.argv)
nowMenu = QtWidgets.QDialog()
ui = Ui_nowMenu()
ui.setupUi(nowMenu)

nowMenu.show()

### DECLARING FUNCTIONS ###

def openFirstWindow():
    global window1
    window1 = QtWidgets.QDialog()
    ui = Ui_window1()
    ui.setupUi(window1)
    nowMenu.close()
    window1.show()

    def returnToMain1():
        window1.close()
        nowMenu.show()

    ui.window1PushButton_1.clicked.connect(returnToMain1)

def openSecondWindow():
    global window2
    window2 = QtWidgets.QDialog()
    ui = Ui_window2()
    ui.setupUi(window2)
    nowMenu.close()
    window2.show()

    def returnToMain2():
        window2.close()
        nowMenu.show()

    ui.window2PushButton_1.clicked.connect(returnToMain2)


def drawGraph():
    dataExcelFile3 = pd.read_excel(excelPath3)

    # Here we read each row in the excel sheet
    y1 = dataExcelFile3.iloc[0]
    y2 = dataExcelFile3.iloc[1]
    y3 = dataExcelFile3.iloc[2]
    y4 = dataExcelFile3.iloc[3]
    y5 = dataExcelFile3.iloc[4]
    y6 = dataExcelFile3.iloc[5]

    # Here we add each row to graph
    plt.plot(y1, label = u'103')
    plt.plot(y2, label = u'104')
    plt.plot(y3, label = u'105')
    plt.plot(y4, label = u'106')
    plt.plot(y5, label = u'109')
    plt.plot(y6, label = u'111')
    
    # The decoration section
    plt.title("Курс Валют")
    plt.ylabel("Курс відносно гривні")
    plt.xlabel("Дата")
    plt.grid()
    plt.legend()

    plt.show()

def saveExcelFile():
    fname = QFileDialog.getSaveFileName()[0]
    try:
        f = open(fname, "w")
        f.write(dataFile)
        f.close()
    except:
        pass

def close():
    QApplication.closeAllWindows()

### CONECTING FUNCTIONS TO APP ###

ui.menuPushButton_1.clicked.connect(openFirstWindow)
ui.menuPushButton_2.clicked.connect(openSecondWindow)
ui.menuPushButton_3.clicked.connect(drawGraph)
ui.menuPushButton_5.clicked.connect(close)

### EXIT THE APP ###

sys.exit(app.exec_())
