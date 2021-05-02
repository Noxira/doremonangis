def ubahjumlah(masukan,jumlah,namaFiles):
    #Masukan adalah nomor ID
    #jumlah adalah jumlah yang ingin diubah, positif artinya menambahkan, negatif kurang

    #inisiasi posisi = 0
    posisi =0

    # Cek posisi item yang ingin diubah jumlah nya
    for i in range(len(namaFiles)):
        if namaFiles[i][0] == masukan:
            posisi = i

    if namaFiles[posisi][3]+jumlah<0:
        print(jumlah,namaFiles[posisi][1], "gagal dibuang karena stok kurang! stok sekarang", namaFiles[posisi][3],)
    else:
        namaFiles[posisi][3] = namaFiles[posisi][3]+jumlah
        if jumlah>0:
            print(jumlah, namaFiles[posisi][1], "berhasil ditambahkan! Stok sekarang", namaFiles[posisi][3])
        else:
            print(abs(jumlah), namaFiles[posisi][1], "berhasil dihapus! Stok sekarang", namaFiles[posisi][3])
