def gadgetReturn(arrayGadget, arrayGadgetBorrow, arrayGadgetReturn, userID):
    num = int(1)
    ownedGadgetValues = [] #[(gadgetID, gadgetName, amount, borrowID)] 
                            # num tdk perlu disimpan, cukup akses num-1

    print("")
    for i in range(len(arrayGadgetBorrow)):
        if arrayGadgetBorrow[i][1] == userID and arrayGadgetBorrow[i][5] == False:
            for j in range(len(arrayGadget)):
                if arrayGadgetBorrow[i][2] == arrayGadget[j][0]:
                    print(str(num) + ". " + arrayGadget[j][1] + " (x" + str(arrayGadgetBorrow[i][4]) +")")
                    temp = (arrayGadget[j][0], arrayGadget[j][1], int(arrayGadgetBorrow[i][4]), int(arrayGadgetBorrow[i][0]))
                    ownedGadgetValues.append(temp)
                    num += 1
    print("")

    if num != 1:
        returnNum = int(input("Masukkan nomor peminjaman: "))

        # To be added kalo mau ngerjain bonus, lg males asdge dasge
        # returnAmount = int(input("Masukkan jumlah yang dikembalikan: "))  
        # if returnAmount <= 0 or returnAmount > ownedGadgetValues[returnNum-1][]

        date = str(input("Tanggal pengembalian: "))

        print("\nItem " + str(ownedGadgetValues[returnNum-1][1]) + " (x" + str(ownedGadgetValues[returnNum-1][2]) + ") telah dikembalikan.\n")
        temp = (int(len(arrayGadgetReturn)), ownedGadgetValues[returnNum-1][3], date)
        arrayGadgetReturn.append(temp)
        arrayGadgetBorrow[(ownedGadgetValues[returnNum-1][3]) - 1][5] = True
    else:
        print("Tidak ada item yang dipinjam!\n")