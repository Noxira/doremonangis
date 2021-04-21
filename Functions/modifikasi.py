def tambahitem (masukan,namaFiles, validasi):
    #namaFiles disini adalah files yang ingin ditambahkan datanya Gadget atau consumable
    #validasi disini untuk memvalidasi jika function dijalankan oleh admin

    #variabel lokal
    kondisi = True
    #cek apakah admin/user
    if validasi == False:
        kondisi= False

    else:
        #cek apakah ID sudah ada
        for i in range(len(namaFiles)):
            if namaFiles[i][0] == masukan:
                kondisi= False
                print("Gagal menambahkan item karena ID sudah ada")

        if kondisi == True:
            if masukan[0] == "G":
                namaFiles.append(["0","0","0","0","0","0"])
            else:
                namaFiles.append(["0", "0", "0", "0", "0"])
            namaFiles[len(namaFiles)-1][0] = masukan
            namaFiles[len(namaFiles)-1][1] = str(input("Masukkan Nama: "))
            namaFiles[len(namaFiles)-1][2] = str(input("Masukkan Deskripsi: "))
            namaFiles[len(namaFiles)-1][3] = int(input("Masukkan Jumlah: "))
            namaFiles[len(namaFiles)-1][4] = str(input("Masukkan Rarity: "))
            if masukan[0]=="G":
                namaFiles[len(namaFiles)-1][5] = int(input("Masukkan Tahun: "))

            print("Item telah berhasil ditambahkan")
