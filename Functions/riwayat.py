def riwayatpinjam(user,gadget,tanggal,jumlah,fileGadget,fileRiwayat):
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
    fileRiwayat[len(fileRiwayat) - 1][2] = namaGadget
    fileRiwayat[len(fileRiwayat) - 1][3] = tanggal
    fileRiwayat[len(fileRiwayat) - 1][4] = jumlah
    return fileRiwayat