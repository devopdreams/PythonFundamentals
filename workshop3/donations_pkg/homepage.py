def show_homepage():
    print("")
    print("          === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login       | 2.    Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate      | 4.    Show Donation  |")
    print("------------------------------------------")
    print("|                 5.  Exit                 |")
    print("------------------------------------------")


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation = username, "donated", donation_amt
    print("Thank you for your donation", username)
    return donation
