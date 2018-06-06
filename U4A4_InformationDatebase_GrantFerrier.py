# -------------------------------------------------------------------------------
# Name:             U4A4_InformationDatebase_GrantFerrier.py
# Purpose:          Add a new item to the system
#                   Display all items (including all properties)
#                   Search for an item by either title or property (your choice)
#                   Sort all items by either title or property (your choice)
#                   Delete an item from the system (from a numbered list)
#
# Author:           Ferrier.G
#
# Created:          06/05/2018
# ------------------------------------------------------------------------------


# Name, Age, League
class Player:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age


def file_io(ltype="lines"):
    lines = [line.rstrip('\n') for line in open('Players.txt')]
    if ltype == "line":
        for line in lines:
            person = line.split()
            return person
    elif ltype == "lines":
        return lines
    print("File IO Done")


# init function
def init():
    print("INIT")
    f = file_io()
    for item in f:
        attribute = item.split()
        print(attribute)
        acc = Player(attribute[0], attribute[1], attribute[2])
        members.append(acc)
    for usr in members:
        print(usr.name)


# Declaring variables
members = []

# Start up
init()
# Main Loop
while 0 == 0:
    usr_input = input("CMD: ")
    if usr_input.upper() == "QUIT" or usr_input.upper() == "Q":
        print("Quiting")
        quit()
    elif usr_input.upper() == "ADD" or usr_input.upper() == "A":
        print("Add")
    elif usr_input.upper() == "REMOVE" or usr_input.upper() == "R":
        number_input = input("Delete Entry #")
        persons = file_io()
        print(persons)
        del persons[int(number_input)]
        print(persons)

    elif usr_input.upper() == "DISPLAY" or usr_input.upper() == "D":
        print("Display")

    elif usr_input.upper() == "SEARCH" or usr_input.upper() == "S":
        while 0 == 0:
            usr_input = input("Search for First Name, Last Name, or Age: ")
            if usr_input.upper() == "FIRST NAME" or usr_input.upper() == "F":
                print("First Name")
                found = []
                for item in members:
                    if item.name == "Grant":
                        member_index = members.index(item)
                        print(str(member_index + 1) + " " + item.name + " " + item.last_name + " " + item.age)
                break
            elif usr_input.upper() == "LAST NAME" or usr_input.upper() == "L":
                print("Last Name")
                found = []
                for item in members:
                    if item.last_name == "Ferrier":
                        member_index = members.index(item)
                        print(str(member_index + 1) + " " + item.name + " " + item.last_name + " " + item.age)
                break
            elif usr_input.upper() == "AGE" or usr_input.upper() == "A":
                print("Age")
                found = []
                for item in members:
                    if item.age == "19":
                        member_index = members.index(item)
                        print(str(member_index + 1) + " " + item.name + " " + item.last_name + " " + item.age)
                break
            else:
                print("Error!")

        print("Search")


    elif usr_input.upper() == "ORGANIZE" or usr_input.upper() == "O":
        print("Organize")
    else:
        print("Input Error!")
        print("Options are: | Quit | Add | Remove | Display | Search | Organize |")
