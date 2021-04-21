def passwordCheck(dataUser, username, password):
    for i in range(len(dataUser)):
        if username == dataUser[i][1]:
            if password == dataUser[i][4]:
                return True
    return False

def isAdmin(dataUser, username):
    for i in range(len(dataUser)):
        if username == dataUser[i][1]:
            if dataUser[i][5] == "admin":
                return True
            else: 
                return False