class Book():

    def __init__(self, name, author, genre, publicationYear):
        self.name = name
        self.author = author
        self.genre = genre
        self.publicationYear = publicationYear

    def getBook(self, name):
        book = open(name+"txt", "r")

### DATA ###

book1 = Book("The Machinery of Freedom", "David Friedman", "Science", "1973")
book2 = Book("Das Capital", "Karl MArx", "Fiction", "1867")
book3 = Book()
#### ---- ###

print("The Home Library welcomes you")

while True:

    print("0. Exit\n1. Print the home library\n2. Search for book\n")
    userInput = str(input())
    

    if userInput == "0":
        break


    elif userInput == "1":
        print()


    elif userInput == "2":

        print("How to search a book?\n1. By name\n2. By author\n3. By genre\n4. By year of publication\n0. Cancel curent action")
        userInput1 = str(input())

        if userInput1 == "0":
            print("Action cancaled\n")

        elif userInput1 == "1":
            print("Enter keyword to search\n")

        elif userInput1 == "2":
            print("Enter keyword to search\n")

        elif userInput1 == "3":
            print("Enter keyword to search\n")

        elif userInput1 == "4":
            print("Enter keyword to search\n")
        
        else:
            print("Invalid Input1\n")


    else:
        print("Invalid Input\n")