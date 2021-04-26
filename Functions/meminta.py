def requestConsumable(arrayConsumable, arrayconsumableHistory, userID):
    itemPosition = int(0)


    itemID = str(input("Masukkan ID Item: "))
    found = False
    for i in range(len(arrayConsumable)):
        if itemID == arrayConsumable[i][0]:
            itemPosition = i
            found = True
    if found == True:     
        amount = int(input("Jumlah Item: "))
        if amount <= arrayConsumable[itemPosition][3] and amount != 0:
            date = str(input("Tanggal permintaan: "))

            print("\nItem " + str(arrayConsumable[itemPosition][1]) + " (x" + str(amount) + ") telah berhasil diambil!")

            temp = (len(arrayconsumableHistory)+1, int(userID), itemID, date, int(amount))
            arrayconsumableHistory.append(temp)
            arrayConsumable[itemPosition][3] -= amount
        else:
            print("\nTerdapat kesalahan pada Jumlah yang diminta!\n")
    else:
        print("\nTerdapat kesalahan pada ID Item!\n")


