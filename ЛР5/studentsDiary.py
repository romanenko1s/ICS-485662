while True:

    userInput = str(input())

    if userInput == "0":
        break

    if userInput == "1":
        file1 = open("studentListData.txt", "r")
        file2 = file1.readlines()

        for line in file2:
            print("#  "+line)

        print("List printed")

    if userInput == "2":
        print("Enter data")

        newData = (str(input())+"\n")

        file1 = open("studentListData.txt", "a+")
        file1.write(newData)
        file1.close()

        print("Data added")

    if userInput == "3":
        print("What row to print?")
        row1 = int(input())

        line = open("studentListData.txt").readlines()[row1]
        print("#  "+line)