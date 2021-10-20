filePath = "studentListData.txt"

while True:

    userInput = str(input())

    if userInput == "0":
        break

    if userInput == "1":
        file1 = open(filePath, "r")
        file2 = file1.readlines()

        for line in file2:
            print("#  "+line)

        print("List printed")

    if userInput == "2":
        print("Enter data")

        newData = (str(input())+"\n")

        file1 = open(filePath, "a+")
        file1.write(newData)
        file1.close()

        print("Data added")

    if userInput == "3":
        print("What row to print?")
        row1 = int(input())

        line = open(filePath).readlines()[row1]
        print("#  "+line)
        print("Row "+row1+" printed")

    if userInput == "4":
        searchInput = str(input())
        search_text_in_file(filePath, searchInput)