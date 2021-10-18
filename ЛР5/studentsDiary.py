import os

file0 = "studentListData.txt"

while True:

    userInput = str(input())

    if userInput == "0":
        break

    if userInput == "1":
        file1 = open(file0, "r")
        file2 = file1.readlines()

        for line in file2:
            print("#  "+line)

        print("List printed")

    if userInput == "2":
        print("Enter data")

        newData = (str(input())+"\n")

        file1 = open(file0, "a+")
        file1.write(newData)
        file1.close()

        print("Data added")

    if userInput == "3":
        print("What row to print?")
        row1 = int(input())

        line = open(file0).readlines()[row1]
        print("#  "+line)

    if userInput == "4":
        for file0 in os.listdir(""):
            print(file0)