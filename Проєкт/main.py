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

### CHOOSING PATH TO EXCEL FILES ###

# Those need to be changed before stating app to your actual path to 3 excel files
excelPath1 = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/Проєкт/curencyData.xls"
excelPath2 = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/Проєкт/curencyData2.xls"
excelPath3 = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/Проєкт/curencyData3.xls"

### WORKING WITH DATA BASES ###

# Here we conwert first and second excel file to string
dataExcelFile1 = pd.read_excel(excelPath1)
dataExcelFile12 = pd.DataFrame(dataExcelFile1, index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
dataFile1 = str(dataExcelFile12)

dataExcelFile2 = pd.read_excel(excelPath2)
dataExcelFile22 = pd.DataFrame(dataExcelFile2, index=[1,2,3,4,5])
dataFile2 = str(dataExcelFile22)

### STARTING APP ###

# Here we start the main menu
app = QtWidgets.QApplication(sys.argv)
nowMenu = QtWidgets.QDialog()
ui = Ui_nowMenu()
ui.setupUi(nowMenu)

nowMenu.show()

### DECLARING FUNCTIONS ###

# This function opens window with first data base
def openFirstWindow():
    global window1
    window1 = QtWidgets.QDialog()
    ui = Ui_window1()
    ui.setupUi(window1)
    nowMenu.close()
    window1.show()

    # Here we print first excel table 
    ui.label2.setText(dataFile1)

    # This function returns us to the first window
    def returnToMain1():
        window1.close()
        nowMenu.show()
    
    # Here we connect return function to the button
    ui.window1PushButton_1.clicked.connect(returnToMain1)

# This function opens window with second data base
# Code is identical to the first one
def openSecondWindow():
    global window2
    window2 = QtWidgets.QDialog()
    ui = Ui_window2()
    ui.setupUi(window2)
    nowMenu.close()
    window2.show()

    ui.label2.setText(dataFile2)

    def returnToMain2():
        window2.close()
        nowMenu.show()

    ui.window2PushButton_1.clicked.connect(returnToMain2)

# This function draws a graph out of third excel file
def drawGraph():
    # Here we open the third excel file
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
    plt.title("Курс Валют")            # Add title
    plt.ylabel("Курс відносно гривні") # Add description to Y axis
    plt.xlabel("Дата")                 # Add description to X axis
    plt.grid()                         # Add grid
    plt.legend()                       # Add legend(description of each graph)

    # Draw the graph
    plt.show()

# This function saves first excel file into your computer
def saveExcelFile():
    # Open the saving menu to create the new file
    fname = QFileDialog.getSaveFileName()[0]

    # Here we open the new file and add data from first excel file
    try:
        f = open(fname, "w")
        f.write(dataFile1)
        f.close()
    except:
        pass

# This fun
def close():
    QApplication.closeAllWindows()

### CONECTING FUNCTIONS TO APP ###

# Here we connect functions to the menu buttons
ui.menuPushButton_1.clicked.connect(openFirstWindow)
ui.menuPushButton_2.clicked.connect(openSecondWindow)
ui.menuPushButton_3.clicked.connect(drawGraph)
ui.menuPushButton_4.clicked.connect(saveExcelFile)
ui.menuPushButton_5.clicked.connect(close)

### EXIT THE APP ###

sys.exit(app.exec_())
