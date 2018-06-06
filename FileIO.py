# Entire file method. Prints the whole file and then adds a end of file message. Option for removing end of file msg.
def entire_file(end_file=True):
    # Opens file in read mode
    inp_file = open("Names.txt", 'r')
    # Reads file and prints the entire thing
    entire_file = inp_file.read()
    print(entire_file)
    # Adds End of File and then closes the file.
    if end_file is True:
        print("-----------------End of File-----------------")
    inp_file.close()


# Prints the entire file at the start of the program.
entire_file()
# Display Welcome message
print("Welcome the \"Contact List\" Program!")

# Main loop
while 0 == 0:
    # Prompts user for input. With the option to clear the file, Quit the program, or Enter a new entry.
    usr_input = input("{\"Clear\"} {\"Quit\"} |or| {NAME} {AGE} {GENDER}:")

    if usr_input.upper() == "CLEAR" or usr_input.upper() == "C":  # Clear the file if the user types "C" or "Clear"
        # Open file in write mode which clears the file and then adds the column titles
        inp_file = open("Names.txt", 'w')
        inp_file.write("Name      | Age | Gender")
        # Closes file and outputs Cleared and then outputs the cleared file.
        inp_file.close()
        print("Cleared!")
        # Display empty list.
        entire_file()
    elif usr_input.upper() == "QUIT" or usr_input.upper() == "Q":  # Quits the program if "Q" or "Quit" is input.
        quit()
    else:  # Adds a new entry to the file.
        # Opens file in append mode. And sets up for a write on a new line.
        inp_file = open("Names.txt", 'a')
        inp_file.write("\n")
        # Takes input and splits up the input into a list.
        test_list = usr_input.split()
        # For each item in the list it appends it to the file.
        n = 0
        for i in test_list:
            inp_file.write(str(test_list[n] + " | "))
            n += 1
        # Closes the file and the prints the entire file with the new changes added.
        inp_file.close()
        entire_file()