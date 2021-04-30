def riwayatGadget(gadget_return_history, gadget_borrow_history, gadget, user): #gadget = dataGadget, user = dataUser?
    for i in range(len(gadget_return_history),len(gadget_return_history)-5 if len(gadget_return_history) >= 5 else 0,-1):
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

                print(f"ID Pengembalian      : {id_kembali}")
                print(f"Nama Pengambil       : {nama_peminjam}")
                print(f"Nama Gadget          : {nama_gadget}")
                print(f"Tanggal Pengembalian : {tanggal_kembali}")

                break
        print()





