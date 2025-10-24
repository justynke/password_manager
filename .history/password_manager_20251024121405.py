pwd = input("What is the master password?\n")

def view():
    with open('db.txt', 'r') as f:
        print("\n")
        for line in f.readlines():
            data = line.rstrip()
            account, user, password = data.split("|")
            print("Account name:", account)
            print("Username:", user, "\nPassword:", password, "\n\n")
        

        

def add():
    name = input("What's the account for? (for example address of the website or name of the program)\n")
    username = input("What's the username?\n")
    password = input("What's the password?\n")

    with open('db.txt', 'a') as f:
        f.write(name + "|" + username + "|" + password + "\n")

def delete():
    account = input("What is the password for? (application / website name etc., not the username)")
    with open('db.txt', 'r') as db:
        lines = db.readlines()

    with open('db.txt', 'w') as f:
        found = False
        for line in lines:
            if line.startswith(account):
                answer = input("Are you sure, you want to delete the data for", account, "? (Y/N)\n")
                if answer.lower() == "y":
                    lines.remove(line)
                    found = True
                elif answer.lower() == "n":
                    break
                else:
                    print("Wrong input")
                    break

        f.writelines(lines)
        if found == False:
            print("Account not found. Please try again!\n")
            break




    


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