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
                print("Found a site with entered url")

            else:
                print("Can`t find a site with entered url (404)")

        except:
            print("Invalid input of url")

    elif userInput == "2":
        pass

    else:
        print("Invalid input")