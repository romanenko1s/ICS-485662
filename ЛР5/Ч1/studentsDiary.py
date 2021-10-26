filePath = "studentListData.txt"

while True:

    print("0. Exit program\n1. Print the diary\n2. Add new content\n3. Print some row\n4. Search by keyword\n")

    userInput = str(input())

    if userInput == "0":
        break


    if userInput == "1":
        
        print("How to sort it?\n1. By names\n2. By marks\n")

        userInput1 = str(input())
          
        if userInput1 == "1":
            file1 = open(filePath, "r")
            file2 = file1.readlines()

            for line in file2:
                print("#  "+line)

            print("List printed\n")

        elif userInput1 == "2":
            file1 = open(filePath, "r")
            file2 = file1.readlines()
            
            #students = {}
            #for row in file2:
            #    students.append(row)

            #print(students)

            a_dictionary = {}
            a_file = open(filePath)
            for line in a_file:
                key, value = line.split()
                a_dictionary[key] = value

            print(a_dictionary)


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


    if userInput == "4":
        print("Enter a key word to search for")
        searchInput = str(input())

        file1 = open(filePath, "r")
        file2 = file1.readlines()
        
        for row in file2:
            if searchInput in row:
                print(row)


    else:
        print("Input Invalida")