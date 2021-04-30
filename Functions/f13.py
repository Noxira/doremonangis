def riwayatConsumable(consumable_history, consumable, user):
    for i in range(len(consumable_history),len(consumable_history)-5 if len(consumable_history) >= 5 else 0,-1):
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
                

        print(f"ID Pengembalian      : {id_ambil}")
        print(f"Nama Pengambil       : {nama_pengambil}")
        print(f"Nama Consumable      : {nama_consumable}")
        print(f"Tanggal Pengembalian : {tanggal_kembali}")
        print(f"Jumlah               : {jumlah}")

        print()