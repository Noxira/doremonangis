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

def riwayatConsumable(consumable_history, consumable, user,value_pos):                              
    ret = []
    for i in range(len(consumable_history)-value_pos,len(consumable_history)-5-value_pos if len(consumable_history) >= 5+value_pos else 0,-1):
        id_pengambil = int(consumable_history[i-1][1])
        id_ambil = consumable_history[i-1][0]
        id_consumable = consumable_history[i-1][2]
        tanggal_kembali = consumable_history[i-1][3]
        jumlah = consumable_history[i-1][4]
        nama_consumable = ""
        nama_pengambil = ""

        for consum in consumable:
            if consum[0]==id_consumable:
                nama_consumable = consum[1]
                break

        for orang in user:
            if orang[0]==id_pengambil:
                nama_pengambil = orang[2]
                break


        ret.append([tanggal_kembali,id_ambil,nama_pengambil,nama_consumable,jumlah])
        break
    # print(f"ID Pengembalian      : {id_ambil}")
    # print(f"Nama Pengambil       : {nama_pengambil}")
    # print(f"Nama Consumable      : {nama_consumable}")
    # print(f"Tanggal Pengembalian : {tanggal_kembali}")
    # print(f"Jumlah               : {jumlah}")

    # print()
    return ret

def riwayatGadget(gadget_return_history, gadget_borrow_history, gadget, user, value_pos):                              
 
    ret = []
 
    for i in range(len(gadget_return_history)-value_pos,len(gadget_return_history)-5-value_pos if len(gadget_return_history) >= 5+value_pos else 0,-1):
        id_pinjam = gadget_return_history[i-1][1]
        id_kembali = gadget_return_history[i-1][0]
        tanggal_kembali = gadget_return_history[i-1][2]
 
        for pinjam in gadget_borrow_history:
            if pinjam[0]==id_pinjam:
                id_peminjam = int(pinjam[1])
                id_gadget = pinjam[2]
                nama_gadget = ""
                nama_peminjam = ""
 
                for gad in gadget:
                    if gad[0] == id_gadget:
                        nama_gadget = gad[1]
                        break
 
                for nama in user:
                    if nama[0]==id_peminjam:
                        nama_peminjam = str(nama[2])
                        break
 
                # print(f"ID Pengembalian      : {id_kembali}")
                # print(f"Nama Pengambil       : {nama_peminjam}")
                # print(f"Nama Gadget          : {nama_gadget}")
                # print(f"Tanggal Pengembalian : {tanggal_kembali}")
		ret.append([tanggal_kembali,id_kembali,nama_peminjam,nama_gadget])		
                break
        # print()
 
    ret.sort(key=lambda date[0]: datetime.strptime(date[0],"%d/%m/%y"))
 
	return ret