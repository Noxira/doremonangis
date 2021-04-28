def writePinjam(user,gadget,tanggal,jumlah,fileGadget,fileRiwayat):
    #user = user yang meminjam
    #gadget = ID gadget yang dipinjam
    #tanggal = tanggal peminjaman
    #jumlah = jumlah peminjaman
    #fileGadget = file gadget.csv
    #fileRiwayat = file gadget_borrow_history

    #mencari nama gadget dari id gadget
    for i in range(len(fileGadget)):
        if fileGadget[i][0]== gadget:
            namaGadget = fileGadget[i][1]

    fileRiwayat.append([0,"0","0","0",0,False])

    fileRiwayat[len(fileRiwayat) - 1][0] = len(fileRiwayat)
    fileRiwayat[len(fileRiwayat) - 1][1] = user
    fileRiwayat[len(fileRiwayat) - 1][2] = gadget
    fileRiwayat[len(fileRiwayat) - 1][3] = tanggal
    fileRiwayat[len(fileRiwayat) - 1][4] = jumlah
    return fileRiwayat

def readPinjam(fileRiwayat,fileGadget):
    #fileRiwayat = file gadget_borrow_history


    #array untuk menampung nama gadget
    namaGadget = ["" for i in range (len(fileRiwayat))]

    # mencari nama gadget dari id gadget
    for i in range(len(fileRiwayat)):
        for j in range(len(fileGadget)):
            if fileGadget[j][0] == fileRiwayat[i][2]:
                namaGadget[i] = fileGadget[i][1]

    for i in range(len(fileRiwayat)):
        print("ID Peminjaman      :  ",fileRiwayat[i][0])
        print("Nama Pengambil     :  ",fileRiwayat[i][1])
        print("Nama Gadget        :  ",namaGadget[i])
        print("Tanggal Peminjaman :  ",fileRiwayat[i][3])
        print("Jumlah             :  ",fileRiwayat[i][4])
        print(" ")