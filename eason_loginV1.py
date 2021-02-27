#password_manager
#store and display password for others
#E.Xuan, February 22

name = ""
age = ""
login_user = ["bdsc"]
login_password = ["pass1234"]
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
def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        if username in login_user and password in login_password:
            print("Welcome back,", username)
        else:
            print("do it again")
            

print("Welocome to the password manager")
while True:
    user_login = input("Please enter, L to login or, N to sign up: ").strip().title()
    if user_login == "L":
        login()
        break
    elif user_login == "N":
        print("make account")
        break
    else:
        print("enter either L or N")



print("If you are over the age of 12, you are able to store your passwords on this app")

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
        print("Please enther numbers")

print("Thank you for using the password manager")