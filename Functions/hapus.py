def hapusitem(masukan, namaFiles):
    #masukan adalah nomor ID
    #namaFiles antara gadget atau consumables

    #inisiasi array baru

    posisi=0
        #Cek posisi item yang ingin dihapus
    for i in range(len(namaFiles)):
        if namaFiles[i][0]==masukan:
            posisi = i

    konfirmasi = input("Apakah anda yakin ingin menghapus item (y/n) ")
    if konfirmasi =="y":
        namaFiles.pop(posisi)
        print("Item telah berhasil dihapus")
        return namaFiles
    else:
        return namaFiles






