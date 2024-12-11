def show_menu():
    while True:
        print("Pick 1 to have fun")
        print("Pick 2 to do work")
        print("Pick 3 to quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("fun")
        elif choice == "2":
            #do something
            pass
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice")

# How to make a list of items in your list
def remove_something():
    for c in range(0, len(myList)):
        print(str(c + 1) + ". " + myList[c])
    choice = input("Which one do you want to remove?: ")
    if choice.isnumeric():
        choice = int(choice)
        if choice -1 >= 0 and choice - 1 < len(myList):
            myList.pop(choice - 1)
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")


# This is how you make a list

myList = ["thing 1", "thing 2", "thing 3", "thing 4"]
print(myList[3])

# This is how you add to the list
myList.append("thing 5")

# This is how you print the entire list
print(myList)


# This is how you remove items using the index
myList.pop(2)
print(myList)

show_menu()