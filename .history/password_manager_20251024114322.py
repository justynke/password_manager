pwd = input("What is the master password?\n")

def view():
    with open('db.txt', 'r') as f:
        for line in f.readlines():
            print line

        

def add():
    name = input("What's the account for? (for example address of the website or name of the program)\n")
    username = input("What's the username?\n")
    password = input("What's the password?\n")

    with open('db.txt', 'a') as f:
        f.write(name + " | " + username + " | " + password + "\n")

def delete():

    pass


while True:
    mode = input(
        "Would you like to:\n1. View existing passwords\n2. Add a new password\n3. Delete a password from the database\n4. Quit the program\n(1/2/3/4)\n"
    )

    if mode == "1":                             # VIEW
        view()
    elif mode == "2":                           # ADD
        add()
    elif mode == "3":                           # DELETE
        delete()
    elif mode == "4":                           # QUIT
        print("Thank you for using our password manager! Have a good day!")
        quit()   
    else:
        print("Invalid command.")
        continue