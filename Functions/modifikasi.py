def tambahitem (masukan,namaFiles):
    #namaFiles disini adalah files yang ingin ditambahkan datanya Gadget atau consumable


    #variabel lokal
    kondisi = True

    #cek apakah ID sudah ada
    for i in range(len(namaFiles)):
        if namaFiles[i][0] == masukan:
            kondisi= False
            print("Gagal menambahkan item karena ID sudah ada")

    if kondisi == True:     #Kondisi True apabila belum ada ID tersebut dalam data
        if masukan[0] == "G":
            namaFiles.append(["0","0","0",0,"0",0])
        else:
            namaFiles.append(["0", "0", "0", 0, "0"])
        namaFiles[len(namaFiles)-1][0] = masukan
        namaFiles[len(namaFiles)-1][1] = str(input("Masukkan Nama: "))
        namaFiles[len(namaFiles)-1][2] = str(input("Masukkan Deskripsi: "))
        namaFiles[len(namaFiles)-1][3] = int(input("Masukkan Jumlah: "))

        RarityItem  = namaFiles[len(namaFiles)-1][4] = str(input("Masukkan Rarity: "))
        if RarityItem != ("S" or "A" or "B" or "C"):
            print("Input rarity tidak valid!")
            namaFiles.pop(-1)
            return namaFiles
        else:
            if masukan[0]=="G":
                namaFiles[len(namaFiles)-1][5] = int(input("Masukkan Tahun: "))

            print("Item telah berhasil ditambahkan")

def hapusitem(masukan, namaFiles):
    #masukan adalah nomor ID
    #namaFiles antara gadget atau consumables

    #inisiasi array baru

    posisi=0

    #Inisiasi kondisi, True apabila ID berada pada data, False jika ID tidak ada di database
    kondisi = True
    for i in range(len(namaFiles)):
        if namaFiles[i][0]==masukan:
            kondisi =True
            break

    if kondisi==False:
        print("Tidak ada item dengan ID tersebut!")
    else: #Kondisi True, terdapat ID tersebut
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

def ubahjumlah(masukan,jumlah,namaFiles):
    #Masukan adalah nomor ID
    #jumlah adalah jumlah yang ingin diubah, positif artinya menambahkan, negatif kurang

    #inisiasi posisi = 0
    posisi =0
    # Inisiasi kondisi, True apabila ID berada pada data, False jika ID tidak ada di database
    kondisi = True
    for i in range(len(namaFiles)):
        if namaFiles[i][0] == masukan:
            kondisi = True
            break

    if kondisi == False:
        print("Tidak ada item dengan ID tersebut!")
    else:  # Kondisi True, terdapat ID tersebut
        # Cek posisi item yang ingin diubah jumlah nya
        for i in range(len(namaFiles)):
            if namaFiles[i][0] == masukan:
                posisi = i

        if namaFiles[posisi][3]+jumlah<0:
            print(jumlah,namaFiles[posisi][1], "gagal dibuang karena stok kurang", namaFiles[posisi][3])
        else:
            namaFiles[posisi][3] = namaFiles[posisi][3]+jumlah
            print(jumlah, namaFiles[posisi][1], "berhasil ditambahkan! Stok sekarang", namaFiles[posisi][3])




