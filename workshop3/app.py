from donations_pkg.homepage import *


database = {"admin": "password123"}
donations = []
authorized_user = ""

show_homepage()
if len(authorized_user) == 0:
    print("You must be logged in to donate")
else:
    print("Logged in as :", authorized_user)
