import requests

while True:

    print("Enter an url")
    userInput = str(input())

    try:
        r = requests.get(userInput)

        if r.ok == True:
            print("Found a site with entered url")

        else:
            print("Can`t find a site with entered url (404)")

    except:
        print("Invalid Input")