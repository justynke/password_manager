pwd = input("What is the master password?\n")


while True:
    mode = input(
        "Would you like to:\n1. View existing passwords\n2. Add a new password\n3. Delete a password from the database\n4. Quit the program\n(1/2/3/4)"
    )

    if mode == "1":                             # VIEW
        pass
    elif mode == "2":                           # ADD
        pass
    elif mode == "3":                           # DELETE
        pass

    else:
        print("Invalid command.")
        continue