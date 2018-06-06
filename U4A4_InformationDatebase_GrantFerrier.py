# -------------------------------------------------------------------------------
# Name:             U4A4_InformationDatebase_GrantFerrier.py
# Purpose:          Add a new item to the system
#                   Display all items (including all properties)
#                   Search for an item by either title or property (your choice)
#                   Sort all items by either title or property (your choice)
#                   Delete an item from the system (from a numbered list)
#
#                   **Note E is used for backing out of menu!**
#
# Author:           Ferrier.G
#
# Created:          06/05/2018
# ------------------------------------------------------------------------------


# First Name, Last Name, Age
class Player:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age


# Reads the data from the file. Has option of reading lines or objects in lines.
def file_io(ltype="lines"):
    lines = [line.rstrip('\n') for line in open('Players.txt')]
    if ltype == "line":
        for line in lines:
            person = line.split()
            return person
    elif ltype == "lines":
        return lines
    print("File IO Done")


# Save function that rights what is in memory into the file.
def save():
    print("Saving File")
    print(".")
    print("..")
    print("...")
    # Opens file in write mode and then saves all the data to it.
    with open("Players.txt", 'w') as f:
        for item in members:
            f.write(item.name + " " + item.last_name + " " + item.age + "\n")
    print("Saved")


# Display function. Rotates through the entire list and displays it to the screen.
def display():
    print("Members:")
    for item in members:
        name_index = members.index(item)
        print(str(name_index + 1) + " | " + item.name + " | " + item.last_name + " | " + item.age)


# init function. Does a fresh read of the file and loads it into the Player() class.
def init():
    print("Initialized")
    # Opens file as F
    f = file_io()
    # Takes each line and creates a class object.
    for item in f:
        attribute = item.split()
        acc = Player(attribute[0], attribute[1], attribute[2])
        members.append(acc)


# Declaring variables
members = []

# Start up
init()
# Main Loop
while 0 == 0:
    usr_input = input("CMD: ")
    if usr_input.upper() == "QUIT" or usr_input.upper() == "Q":  # Saves the program and then quits.
        save()
        while 0 == 0:  # Question Loop Asks the user if they really want to quit.
            usr_input = input("Are you sure you want to quit? {Y} {N} : ")
            if usr_input.upper() == "Y":
                quit()
            elif usr_input.upper() == "N":
                break
            else:
                print("Error!")
    elif usr_input.upper() == "SAVE" or usr_input.upper() == "S":  # Saves the program.
        save()
    elif usr_input.upper() == "INIT" or usr_input.upper() == "I":  # Reinitialize the file.
        members = []
        init()
    elif usr_input.upper() == "ADD" or usr_input.upper() == "A":  # Adds users to the database.
        while 0 == 0:  # Question Loop
            usr_input = input("Add {First Name} | {Last Name} | {Age} : ")
            if usr_input.upper() == "EXIT" or usr_input.upper() == "E":  # User can exit this level of menu
                break
            acc = usr_input.split()  # Splits the user input into three section and checks to make sure input is valid
            if len(acc) == 3:
                if acc[2].isdigit():
                    if int(acc[2]) > 0:
                        # Adds the new account with the provided values
                        new_acc = Player(acc[0], acc[1], acc[2])
                        members.append(new_acc)
                        print("Added: ")
                        name_index = members.index(new_acc)
                        # Displays the new user info.
                        print(str(
                            name_index + 1) + " | " + new_acc.name + " | " + new_acc.last_name + " | " + new_acc.age)
                    else:
                        print("Please enter an age above 0")
                else:
                    print("Incorrect Age!")
            else:
                print("Error!")

    elif usr_input.upper() == "REMOVE" or usr_input.upper() == "R":  # Removes a user from the database.
        while 0 == 0:  # Menu loop
            number_input = input("Delete Entry # ")
            if number_input.upper() == "EXIT" or number_input.upper() == "E":  # Exit this level of menu.
                break
            # Checks for valid commands
            elif number_input.isdigit() is True and int(number_input) > 0 and int(number_input) < (len(members) + 1):
                del members[int(number_input) - 1]  # Removes the user at index indicated.
                print("Here is the new list with updated indexes:")
                display()
            else:
                print("That was not a correct index!")

    elif usr_input.upper() == "DISPLAY" or usr_input.upper() == "D":  # Prints out all info in database.
        display()

    elif usr_input.upper() == "FIND" or usr_input.upper() == "F":  # Finds what the user looks for.
        while 0 == 0:  # Menu loop
            usr_input = input("Search for First Name, Last Name, or Age: ")
            if usr_input.upper() == "EXIT" or usr_input.upper() == "E":  # Exit this level of menu
                break
            if usr_input.upper() == "FIRST NAME" or usr_input.upper() == "F":  # Find First Names
                while 0 == 0:
                    usr_input = input("Enter the First Name you wish to search for: ")
                    if usr_input.upper() == "EXIT" or usr_input.upper() == "E":  # Exit this level of menu
                        break
                    found = []
                    first_names = []
                    # Checks to make sure the input is a valid search
                    for item in members:
                        first_names.append(item.name)
                    if usr_input in first_names:
                        # Searches and prints all entries that match the search terms.
                        for item in members:
                            if item.name == usr_input:
                                name_index = members.index(item)
                                print(str(
                                    name_index + 1) + " | " + item.name + " | " + item.last_name + " | " + item.age)
                        break
                    else:
                        print("That Name was Not Found!")
            elif usr_input.upper() == "LAST NAME" or usr_input.upper() == "L":  # Find Last Names
                while 0 == 0:
                    usr_input = input("Enter the Last Name you wish to search for: ")
                    if usr_input.upper() == "EXIT" or usr_input.upper() == "E":
                        break
                    found = []
                    last_names = []
                    # Checks to make sure input is a valid search
                    for item in members:
                        last_names.append(item.last_name)
                    if usr_input in last_names:
                        # Searches and prints all the entries that match the search terms.
                        for item in members:
                            if item.last_name == usr_input:
                                lastname_index = members.index(item)
                                print(str(
                                    lastname_index + 1) + " | " + item.name + " | " + item.last_name + " | " + item.age)
                        break
                    else:
                        print("That Name was Not Found!")
            elif usr_input.upper() == "AGE" or usr_input.upper() == "A":  # Find Ages
                while 0 == 0:
                    usr_input = input("Enter the Age you wish to search for: ")
                    if usr_input.upper() == "EXIT" or usr_input.upper() == "E":
                        break
                    found = []
                    ages = []
                    # Checks to make sure the input is a valid search.
                    for item in members:
                        ages.append(item.age)
                    if usr_input in ages:
                        # Searches and prints all the entries that match the search terms.
                        for item in members:
                            if item.age == usr_input:
                                member_index = members.index(item)
                                print(str(
                                    member_index + 1) + " | " + item.name + " | " + item.last_name + " | " + item.age)
                        break
                    else:
                        print("That Age was Not Found!")
            else:
                print("Error!")

    elif usr_input.upper() == "ORGANIZE" or usr_input.upper() == "O":  # Organizes the database
        while 0 == 0:  # Menu loop
            usr_input = input("What would you like to sort? {First Name} | {Last Name} | {Age} : ")
            if usr_input.upper() == "EXIT" or usr_input.upper() == "E":  # Exit this level of menu
                break
            elif usr_input.upper() == "FIRST NAME" or usr_input.upper() == "F":  # Organize by first name
                members.sort(key=lambda x: x.name, reverse=False)
                break
            elif usr_input.upper() == "LAST NAME" or usr_input.upper() == "L":  # Organize by last name
                members.sort(key=lambda x: x.last_name, reverse=False)
                break
            elif usr_input.upper() == "AGE" or usr_input.upper() == "A":  # Organize by age
                members.sort(key=lambda x: x.age, reverse=False)
                break
            else:
                print("Error!")
        print("Database Sorted!")
    else:
        print("Input Error!")
        print("Options are: | Quit | Add | Remove | Display | Find | Organize |")
