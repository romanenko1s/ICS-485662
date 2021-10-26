filePath = "studentListData.txt"

while True:

    print("0. Exit program\n1. Print the diary\n2. Add new content\n3. Print some row\n4. Search by keyword\n")

    userInput = str(input())

    if userInput == "0":
        break


    elif userInput == "1":
        
        print("How to sort it?\n1. By names\n2. By marks\n")

        userInput1 = str(input())
          
        if userInput1 == "1":
            file1 = open(filePath, "r")
            file2 = file1.readlines()

            for line in file2:
                print("#  "+line)

            print("List printed\n")

        elif userInput1 == "2":

            studentsList= {}
            file1 = open(filePath)

            for line in file1:
                key, value = line.split()
                studentsList[key] = value

            studentsListSorted = dict(sorted(studentsList.items(), key=lambda item: item[1], reverse = True))

            for student in studentsListSorted:
                print(student)

    elif userInput == "2":
        print("Enter data")

        newData = (str(input())+"\n")

        file1 = open(filePath, "a+")
        file1.write(newData)
        file1.close()

        print("Data added\n")


    elif userInput == "3":
        print("What row to print?")
        row1 = int(input())

        line = open(filePath).readlines()[row1]
        print("#  "+line)
        print("Row "+str(row1)+" printed\n")


    elif userInput == "4":
        print("Enter a key word to search for")
        searchInput = str(input())

        file1 = open(filePath, "r")
        file2 = file1.readlines()
        
        for row in file2:
            if searchInput in row:
                print(row)


    else:
        print("Input Invalida")