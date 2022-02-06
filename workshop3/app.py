from donations_pkg.homepage import *
from donations_pkg.user import *


database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()
    if len(authorized_user) == 0:
        print("You must be logged in to donate")
    else:
        print("Logged in as :", authorized_user)

    choice = int(input("Choose an option: "))
    print("\n")
    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if len(authorized_user) > 0:
            database[authorized_user] = password
    elif choice == 3:
        if not len(authorized_user) > 0:
            print("You must be logged in to donate.")
        else:
            donation = donate(authorized_user)
            donations.append(donation)
    elif choice == 4:
        show_donations(donations)
    else:
        print("Leaving DonateMe")
        break
