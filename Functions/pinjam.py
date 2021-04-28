def pinjam(user, gadget, tanggal, jumlah, fileGadget, fileInventory):
    # user = user yang meminjam
    # gadget = ID gadget yang dipinjam
    # tanggal = tanggal peminjaman
    # jumlah = jumlah peminjaman
    # fileGadget = file gadget.csv
    # fileInventory = file inventory.csv

    posisi = 0

    #cek posisi gadget
    for i in range(len(fileGadget)):
        if fileGadget[i][0] == gadget:
            posisi = i

    #cek apakah gadget sudah pernah dipinjam oleh user yang sama
    #cek bernilai True apabila user sudah pernah meminjam item yang sama
    cek = False
    for i in range(len(fileInventory)):
        if fileInventory[i][1]==user and fileInventory[i][2]==gadget:
            cek = True
            break

    # mencari nama gadget dari id gadget
    for i in range(len(fileGadget)):
        if fileGadget[i][0] == gadget:
            namaGadget = fileGadget[i][1]


    if cek ==False:
        if fileGadget[posisi][3] < jumlah:
            print("Jumlah peminjaman melebihi stok yang ada!")
        else:
            fileGadget[posisi][3]= fileGadget[posisi][3] - jumlah
            fileInventory.append([0,"0","0","0",0])
            fileInventory[len(fileInventory) - 1][0] = len(fileInventory)
            fileInventory[len(fileInventory) - 1][1] = user
            fileInventory[len(fileInventory) - 1][2] = gadget
            fileInventory[len(fileInventory) - 1][3] = tanggal
            fileInventory[len(fileInventory) - 1][4] = jumlah
            print("Peminjaman", namaGadget, "sebanyak", jumlah,"buah berhasil dilakukan!")

    else:
        print("User Sudah pernah meminjam Item ini!")

