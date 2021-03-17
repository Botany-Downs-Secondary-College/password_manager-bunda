#password_manager
#store passwords
#Kiran HArry, March 16th

name = ""
age = ""
existing_user = ["bdsc"]
login_password = ["Pass123"]
password_list = []

def menu(name):

    mode = input("Choose a mode by entering the number: \n"
    "1: Add passwords 2: Veiw passwords 3: Exit \n"
    "").strip()
    return mode
        
def login():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    while True:

        if username in existing_user and password in login_password:
            print("Welcome back,", username)
            break
        else:
            print("That is incorrect, please try again")

def sign_up(age, name):

    if age < 13:
        print("Sorry, you do not meet the age requirement for this app. You must be 13 years old and above.")
        exit()
    else:
        print("Welcome", name)

    while True:
        new_user = input("Please enter new username: ")
        if new_user in existing_user:
            print("This username has already been taken, please pick another one.")
        else:
            existing_user.append(new_user)
            break

    while True:
        print("Your password must contain atleast 8 characters, 1 digit and a capital letter")
        new_password = input("New password: ")

        if len(new_password) < 8:
            print("Your password does not have 8 characters")
        elif new_password.islower() == True:
            print("Your password does not have an uppercase")
        elif new_password.isdigit() == False:
            print("You do not have a number")
        else:
            login_password.append(new_password)
            print("account created")
            break

            
print("Welocome to the password manager")

while True:
    user_login = input("Please enter, L to login or, S to sign up: ").strip().title()
    if user_login == "L":
        login()
        break
    elif user_login == "S":
        name = input("What is your name?: ")
        age = float(input("How old are you?: "))
        sign_up(age, name)
    else:
        print("enter either L or S")

while True:
    try:
        option = menu(name)

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