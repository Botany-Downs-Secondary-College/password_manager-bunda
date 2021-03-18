#password_manager
#store and display password for others

name = ""
age = ""
user = []
password_list = []

def menu(name, age):

    if age < 13:
        print("Sorry, you do not meet the age requirement for this app")
        exit()
    else:
        print("Welcome", name)
        mode = input("Choose a mode by entering the number: \n"
        "1: Add passwords 2: Veiw passwords 3: Exit \n"
        "").strip()
        return mode

print("Welocome to the password manager")
print("If you are 13 or older, you can store access details on the web or mobile apps")

name = input("What is your name?: ")

while True:
    try:
        age = float(input("How old are you?: "))

        option = menu(name, age)

        if option == "1":
            new_password = input("please enter a password: ")
            password_list.append(new_password)        
        elif option == "2":
            print("Here are your passwords")
            for password in password_list:
               print(password)
        elif option == "3":
           print("Goodbye")
           break
        else:
            print("That is not a valid number please enter a valid value")
    except ValueError:
        print("That was not a valid option, please enter a number")

print("Goodbye, thank you for using password manager")