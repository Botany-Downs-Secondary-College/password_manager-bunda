#password_manager
#store and display password for others
#E.Xuan, February 22

name = ""
age = ""
member_list = [["bdsc", "pass1234"]]
accounts = []
tries = 3

def menu(name):

    mode = input("Choose a mode by entering the number: \n"
    "1: Add passwords 2: Veiw passwords 3: Exit \n"
    "").strip()
    return mode
        
def login(tries):

    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        if [username, password] in member_list:
            print("Welcome back,", username)
            break
        if tries == 1:
            print("You have failed to login")
            exit()
        else:
            tries = tries - 1
            print("That is incorrect, please try again you have {} tries left".format(tries))

def sign_up(age, name):

    if age < 13:
        print("Sorry, you do not meet the age requirement for this app. You must be 13 years old and above.")
        exit()
    else:
        print("Welcome", name)

    while True:
        for user in member_list:
            new_user = input("Please enter new username: ")
            if new_user in user:
                print("This username has already been taken, please pick another one.")
            else:
                break
            break
        if new_user not in user:
            break 

    while True:
        print("Your password must contain at least 8 characters, 1 digit and a capital letter")
        new_password = input("New password: ")

        if len(new_password) < 8:
            print("Your password does not have 8 characters")
        elif any(passreqs.isupper() for passreqs in new_password) == False:
            print("Your password does not have an uppercase")
        elif any(passreqs.isdigit() for passreqs in new_password) == False:
            print("You do not have a number")
        else:
            member_list.append([new_user, new_password])
            with open("members.txt", 'a+') as output:
                for member in member_list:
                    output.write(''.join([str(a) for a in member]) + '\n')
            print("account created")
            break

print("Welcome to the password manager")

while True:
    user_login = input("Please enter, L to login or, N to sign up: ").strip().title()
    if user_login == "L":
        login(tries)
        break
    elif user_login == "N":
        name = input("What is your name?: ")
        age = float(input("How old are you?: "))
        sign_up(age, name)
    else:
        print("enter either L or N")

while True:
    try:
        option = menu(name)

        if option == "1":
            app_name = input("What app would you like to store an account in: ").strip()
            existing_user = input("please enter your username: ")
            existing_password = input("please enter a password: ")
            new_account = "Website/App: {} -- Username: {} -- Password: {}".format(app_name, existing_user, existing_password)
            accounts.append([app_name, existing_user, existing_password])
            with open("logins.txt", 'a+') as output:
                for listitem in accounts:
                    output.write(new_account)

        elif option == "2":
            print("Here are your accounts")
            for account in range(0, len(accounts)):
               print("Website/App: {} -- Username: {} -- Password: {}".format(accounts[account][0], accounts[account][1], accounts[account][2]))
        elif option == "3":
           print("Goodbye")
           break
        else:
            print("That is not a valid number please enter a valid value")
    except ValueError:
        print("Please enther numbers")

print("Thank you for using the password manager")
