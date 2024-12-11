"""
Sean Davidson
12-10-24
To Do List
Period: 1
"""


# This is the variable that hold the items added into the list
toDoList = []
#file name
fName = "data.txt"

# Functions
def save_file():
    with open(fName, "w") as file:
        file.writelines(item + "\n" for item in toDoList)


def load_file():
    global toDoList
    with open(fName, "r") as file:
        toDoList = [line.strip() for line in file]
        print(toDoList)

def add_item(item):
    # add an item to the to do list
    toDoList.append(item)

def remove_item():
    # If there is no item to remove the code won't execute
    if len(toDoList) < 1:
        print("There is no item to remove")
        return
    # This will allow an item to be removed from the list
    for c in range(0, len(toDoList)):
        print(str(c + 1) + ". " + toDoList[c])
    choice = input("Which one do you want to remove?: ")
    if choice.isnumeric():
        choice = int(choice)
        if choice -1 >= 0 and choice - 1 < len(toDoList):
            toDoList.pop(choice - 1)
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")

def reset_list():
   # This is the command to use to clear everything in a list
    list.clear(toDoList)

def print_list():
    for c in range(0, len(toDoList)):
        print(str(c + 1) + ". " + toDoList[c])
    if len(toDoList) < 1:
        print("The list is empty")

def show_menu():
    load_file()
    while True:
        print("Press 1 to add an item to the list")
        print("Press 2 to remove an item from the list")
        print("Press 3 to see the list of items")
        print("Press 4 to reset the list")
        print("Press 5 to quit the program")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item(input("Enter item to add: "))
            print("You have successfully added the item")
        elif choice == "2":
            remove_item()

        elif choice == "3":
            print_list()
            

        elif choice == "4":
            reset_list()
            print("The list has been cleared")

        elif choice == "5":
            with open(fName, "w") as file:
                file.writelines(item + "\n" for item in toDoList)
            print("Bye!")
            break
        else:
            print("Invalid choice")

show_menu()