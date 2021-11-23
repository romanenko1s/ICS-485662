import pandas as pd
import matplotlib as ml
import matplotlib.pyplot as plt
#import tkinter as tk

excelPath = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/ЛР7/curencyData.xls"
csvPath = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/ЛР7/curencyData.csv"

dataFile1 = pd.read_excel(excelPath)
dataFile = pd.DataFrame(dataFile1, index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
for data in dataFile:
    print(data)
dataFile.plot(x = "")
plt.show()
