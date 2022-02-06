

def login(database, username, password):
    if (username in database) and (password == database[username]):
        print("Welcome back!", username)
        return username
    elif (username in database) and not(password == database[username]):
        print("Password incorrect, try again", username)
        return
    else:
        print("User not found. Please register")
        return


def register(database, username):
    if username in database:
        print('Username already registered')
        return ""
    else:
        print("Username", username, "registered")
        return(username)
