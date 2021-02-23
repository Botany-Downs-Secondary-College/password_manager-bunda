#password_manager.py
#store and display passwords for users
#Jass Singh, Feb 23

name = ""
age = ""

password_list = []

user_list = []




def menu(name, age):
    
    print("Hello {}".format(name))

    if age < 13:
        print("Sorry, you are not old enough to use the Password Manager. The programme will now exit")
        exit()

    else:
        option = input("Please choose a mode by entering a number from 1 to 3: \n 1. Add a password 2. View your passwords 3. Exit \n")
        return option


print("Welcome to the password manager")


name = input("What is your name? ")
age = int(input("What is your age? "))



while True:
    chosen_option = menu(name, age)

    if chosen_option == "1":
        #call add_password function

    elif chosen_option == "2":
        #Call view_passwords function


    elif chosen_option == "3":
        #End programme

    else:
        print("That is not a valid option. Please enter a number from 1 to 3")


print("Goodbye")
