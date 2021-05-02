def carirarity(x,datas):
    #x disini adalah rarity yang dicari
    #datas disini adalah gadget.csv

    # inisiasi count untuk mengecek apakah ada data sesuai/tidak
    count = 0
    print("Hasil Pencarian:")
    for i in range(len(datas)):

        if datas[i][4]== x:
            print("Nama             :", datas[i][1])
            print("Deskripsi        :", datas[i][2])
            print("Jumlah           :", datas[i][3])
            print("Rarity           :", datas[i][4])
            print("Tahun ditemukan  :", datas[i][5], "\n")
            count = count+1     #setidaknya ada 1 data sesuai

        print(end="")
    if count==0:
        print("tidak ada gadget ditemukan!")
def caritahun(x,y,datas):
    # x disini adalah tahun yang dicari
    #y adalah kategori (= , < , > ,>=, <=
    # datas disini adalah gadget.csv

    #inisiasi count untuk mengecek apakah ada data/tidak
    count = 0
    print("\nHasil Pencarian:")
    for i in range(len(datas)):
        if y=="=":

            if datas[i][5] == x:
                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])
                print(end="")
                count=count+1

        elif y == ">":

            if datas[i][5] > x:
                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

                print("")
                count = count + 1

        elif y == ">=":

            if datas[i][5] >= x:

                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

                print("")
                count = count + 1

        elif y == "<=":

            if datas[i][5] <= x:

                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

                print("")
                count = count + 1
        elif y == "<":

            if datas[i][5] < x:

                print("Nama             :", datas[i][1])
                print("Deskripsi        :", datas[i][2])
                print("Jumlah           :", datas[i][3])
                print("Rarity           :", datas[i][4])
                print("Tahun ditemukan  :", datas[i][5])

                print("")
                count = count + 1

    if count == 0:
        print("Tidak ditemukan data pada tahun", y, x)
