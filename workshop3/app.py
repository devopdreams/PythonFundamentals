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
    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        print("Write register functionality")
    elif choice == 3:
        print("TODO: Write donate functionality")
    elif choice == 4:
        print("TODO: Write show donations functionality")
    else:
        print("Leaving DonateMe")
        break
