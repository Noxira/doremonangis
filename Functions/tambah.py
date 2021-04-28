def tambahitem (masukan,namaFiles):
    #namaFiles disini adalah files yang ingin ditambahkan datanya Gadget atau consumable


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