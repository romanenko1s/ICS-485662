import requests

print("Site analizer welcomes you ")

while True:

    print("1. Check if some site is existing\n2. Print the cite\n0. Exit")
    userInput = str(input())


    if userInput == "0":
        break


    elif userInput == "1":

        print("Enter an url")
        userInput1 = str(input())

        try:
            r = requests.get(userInput1)

            if r.ok == True:
                print("Site with entered url exists")

            else:
                print("Can`t reach a site with entered url (404)")

        except:
            print("Invalid input of url")


    elif userInput == "2":

        print("Enter an url")
        userInput2 = str(input())

        try:
            r = requests.get(userInput2)

            if r.ok == True:
                print(r.text)

            else:
                print("Can`t reach a site with entered url (404)")

        except:
            print("Invalid input of url")


    else:
        print("Invalid input")