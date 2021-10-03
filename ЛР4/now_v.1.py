import pandas as pd

dataFile1 = pd.read_excel(r"/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/ЛР4/curencyData.xls")
dataFile = pd.DataFrame(dataFile1, index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
print(dataFile)