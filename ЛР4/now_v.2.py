import pandas as pd
a1 = 103; a2 = 104; a3 = 105; a4 = 106; a5 = 109; a6 =111
A = [a1, a2, a3, a4, a5, a6]
e1 = 2003; e2 = 2004; e3 = 2005
E = [e1, e2, e3]

column = pd.MultiIndex.from_product([["Курс грн."], ["1.10", "1.11", "1.12"]])
column = column.insert(0, ("Код валюти"))
column = column.insert(4, ("Рік"))

dataFile = pd.DataFrame([
    A*3,
    E,
], column).T

print(dataFile)