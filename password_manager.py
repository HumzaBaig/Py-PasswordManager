# Imports
import os


# Retrieve password for password manager
def get_master_password():
    return input("What is the master password? ")


# Display list of current passwords
def view_passwords():
    if os.path.exists("passwords.txt"):
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                try:
                    data = line.rstrip()

                    user, password = data.split("|")

                    print("User:", user, "Password:", password)
                except ValueError:
                    print("Error: Corrupted line found in passwords file.")
    else:
        print("No passwords saved yet.")


# Request and add new password to list
def add_passwords():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + password + "\n")


# Main function
def main():
    master_pwd = get_master_password()

    while True:
        mode = input("Would you like to add a new password, view existing ones, or quit? (view/add/q) ").lower()
        
        if mode == "q":
            break

        if mode == "view":
            view_passwords()
        elif mode == "add":
            add_passwords()
        else:
            print("Invalid mode, please try again.")


# Run password manager
if __name__ == "__main__":
    main()