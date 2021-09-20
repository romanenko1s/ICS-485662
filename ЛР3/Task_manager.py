# This program invented to organize your tasks

# Here goes the help info about code

help1 = 'Hello, this is an interactive task manager.\nYou can add, view and delete your tasks, so you can use it as your daily list.\nYou can get help and additional info, by typing "help".'
help2 = 'Here is a command list:\n1."Add task" - adds task to your task list\n2."My tasks" - prints all your tasks into the command line\n3."Clear list" - deletes all your tasks\n4."Help" - get a help menu and all additional info\n5."Commands" - gets only list of commands'
help3 = 'Commands are not case sensetive, you can use capitalised and normal size letters.\nAll changes are automaticaly saved.'

def dec1():
    print("-------------------")

print(help1)
dec1()

while True:
    # Here code takes an raw input as a string, and converts it in lowercase

    userinputraw = str(input())

    def lowercase (input1):
        return input1.lower()
        
    userinput = lowercase(userinputraw)
    
    if userinput == "exit":
        break
    
    # From here we startinvg to work with data file

    try:    
        # Here we add new tasks to data file

        if userinput == "add task":
            dec1()
            print("What task is it?")
            
            newtaskinput = (str(input())+"\n")
            
            file_tasklist = open("tasklistdata", "a+")
            file_tasklist.write(newtaskinput)
            file_tasklist.close()

            print("Task added")
            dec1()

        # Here we print tasks 

        if userinput == "my tasks":
            try:
                dec1()
                file_tasklist = open("tasklistdata", "r")
                file_tasklistreadmode = file_tasklist.readlines()

                line_count = 0
                for line in file_tasklistreadmode:
                    if line != "\n":
                        line_count += 1
                
                if line_count == 1:
                    print("Printing your tasks...\n")

                    for line in file_tasklistreadmode:
                        print("#  "+line.capitalize())
                        
                else:
                    print("You have no task")

                file_tasklist.close()
                    
            except:
                print("Error ocured during printing from data file\nOr maybe, you just have no tasks")

            finally:
                dec1()

        #Here we clear the data file

        if userinput == "clear list":
            print("You want to clear your task, confirm your action?")
            clearlistinput = lowercase(str(input("y/n")))

            if clearlistinput == "y":
                try:
                    file_tasklist = open("tasklistdata", "w")
                    file_tasklist.close()
                    print("Data has been deleted")

                except:
                    print("Error ocured during data earising")
            
            else:
                print("Action canceled")

            dec1()
            print("")
            dec1()

        if userinput == "help":
            print(help1+"\n\n"+help2+"\n\n"+help3)
            dec1()

        if userinput == "commands":
            print(help2)
            dec1()

    except:
        print("Error ocured during opening a data file")
        file_tasklist.close()