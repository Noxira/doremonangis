def findIdMax(dataUser):
    maximum = int(0)
    for i in range(len(dataUser)):
        if dataUser[i][0] > maximum:
            maximum = dataUser[i][0]
    return maximum

def uniqueUsername(dataUser, username):
    unique = True
    for i in range(len(dataUser)):
        if dataUser[i][1] == username:
            unique = False
            break
    return unique #return true jika tidak ada di csv

def addNewUser(dataUser):
    newline = [] 
    maximumId = findIdMax(dataUser)
    newline.append(int(maximumId+1))

    nama = str(input("Masukkan nama: "))

    username = str(input("Masukkan username: "))
    while not(uniqueUsername(dataUser, username)):
        print("\nusername telah digunakan, coba yang lain!")
        username = str(input("Masukkan username: "))
    newline.append(username)
    newline.append(nama)

    password = str(input("Masukkan password: "))

    alamat = str(input("Masukkan alamat: "))
    newline.append(alamat)
    newline.append(password)
    newline.append("user") # karena bila register sendiri, akan otomatis user

    dataUser.append(newline)
    print("\nUser " + username + " telah berhasil register ke dalam Kantong Ajaib.")
    return (dataUser)