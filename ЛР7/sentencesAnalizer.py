import pylab

filePath = "/home/user/GitHub/romanenko1s/romanenko1s/ICS-485662/ЛР7/textForSentencesAnalizer.txt"
file1 = open(filePath, "r", encoding='UTF-8').read().lower().split()

symbols = []

for word in file1:
    for symbol in word:
        symbols.append(symbol)  

symbols.sort()

example = [".","!","?"] 
sentences =[]

for symbol1 in symbols:
    if symbol1 in example:
        sentences.append(symbol1)

frequency = {}

for item in sentences:
   if item in frequency:
        frequency[item] += 1
   else:
        frequency[item] = 1


keys, values = zip(*frequency.items())

try:
    print("Розповідні речення: ",values[1])
except:
    print("Немає розповідних речень")
try:
    print("Питальні речення: ",values[0])
except:
    print("Немає питальних речень")
try:
    print("Окличні речення: ", values[2])
except:
    print("Немає окличних речень")