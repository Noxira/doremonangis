# Inisiasi sistem Import
import sys
import os
import argparse

sys.path.insert(0, '/Functions')

# Sistem untuk import functions-functions
from Functions import hash
from Functions import csv
from Functions import register
from Functions import login
from Functions import search
from Functions import tambah
from Functions import ubahJumlah
from Functions import hapus
from Functions import pinjam
from Functions import riwayat
from Functions import kembalikan
from Functions import meminta
from Functions import help
from Functions import f12
from Functions import f13

# Variabel lokal
running = True
loggedIn = False
userIsAdmin = False


# Fungsi lokal
def loadAllFiles():  # Untuk loading file2 biar rapih aja
    global dataUser
    global dataGadget
    global dataConsumable
    global dataConsumableHistory
    global dataGadgetBorrowHistory
    global dataGadgetReturnHistory
    global dataInventory
    dataUser = csv.openFileUser(args.folderDirectory + "/user.csv")
    dataGadget = csv.openFileGadget(args.folderDirectory + "/gadget.csv")
    dataConsumable = csv.openFileConsumable(args.folderDirectory + "/consumable.csv")
    dataConsumableHistory = csv.openFileConsumableHistory(args.folderDirectory + "/consumable_history.csv")
    dataGadgetBorrowHistory = csv.openFileGadgetBorrowHistory(args.folderDirectory + "/gadget_borrow_history.csv")
    dataGadgetReturnHistory = csv.openFileGadgetReturnHistory(args.folderDirectory + "/gadget_return_history.csv")
    dataInventory = csv.openFileInventory(args.folderDirectory + "/inventory.csv")


def saveFilesTo(folderName):  # Untuk nyimpen data-data yang sekarang berupa list of array menjadi csv ke suatu folder
    if not (os.path.exists(folderName)):
        os.mkdir(folderName)
    csv.writeFileUser(folderName + "/user.csv", dataUser)
    csv.writeFileGadget(folderName + "/gadget.csv", dataGadget)
    csv.writeFileConsumable(folderName + "/consumable.csv", dataConsumable)
    csv.writeFileConsumableHistory(folderName + "/consumable_history.csv", dataConsumableHistory)
    csv.writeFileGadgetBorrowHistory(folderName + "/gadget_borrow_history.csv", dataGadgetBorrowHistory)
    csv.writeFileGadgetReturnHistory(folderName + "/gadget_return_history.csv", dataGadgetReturnHistory)
    csv.writeFileInventory(folderName + "/inventory.csv", dataInventory)


def modify_data(data, idx, col, value):  # Untuk mengubah data di suatu data
    data[idx][col] = value


# fungsi validasi, bernilai True jika terdapat ID sesuai didalam file csv
def validasi(masukan, namaFiles):
    kondisi = False
    for i in range(len(namaFiles)):
        if namaFiles[i][0] == masukan:
            kondisi = True
    return kondisi


def switchcaseInput(userinput):  # Switchcase input user ketika sudah me-load data
    global dataUser
    global running
    global userID  # Menyimpan ID User utk dipakai selanjutnya
    global userIsAdmin  # [Penting] akan menyimpan apakah user admin atau tidak (Bool)
    global loggedIn  # [Penting] akan menyimpan apakah user sudah login atau belum (Bool)

    if userinput == "register":  # F01
        if loggedIn == True:
            if userIsAdmin == True:
                print("")
                dataUser = register.addNewUser(dataUser)
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")


    elif userinput == "login":  # F02
        if loggedIn == False:
            print("")
            userTemp = input("Masukkan username: ")
            passTemp = input("Masukkan password: ")
            if login.passwordCheck(dataUser, userTemp, passTemp):
                print("\nHalo " + userTemp + "! Selamat datang di Kantong Ajaib")
                userID = login.findID(dataUser, userTemp)
                loggedIn = True
                if login.isAdmin(dataUser, userTemp):
                    userIsAdmin = True
                else:
                    userIsAdmin = False
            else:
                print("\nPassword atau Username salah!")
        else:
            print("User sudah log in!\n")

    elif userinput == "carirarity":  # F03
        if loggedIn == True:
            dicari = str(input("Masukan rarity: "))
            search.carirarity(dicari, dataGadget)
        else:
            print("User belum log in!\n")

    elif userinput == "caritahun":  # F04
        if loggedIn == True:
            dicari = int(input("Masukan tahun: "))
            kategori = str(input("Masukan kategori: "))
            search.caritahun(dicari, kategori, dataGadget)
        else:
            print("User belum log in!\n")

    elif userinput == "tambahitem":  # F05
        if loggedIn == True:
            if userIsAdmin == True:
                dicari = (input("Masukan ID: "))

                if dicari[0] == "G":
                    if validasi(dicari, dataGadget) == False:
                        tambah.tambahitem(dicari, dataGadget)
                    else:
                        print("Sudah ada gadget dengan ID tersebut!")
                elif dicari[0] == "C":
                    if validasi(dicari, dataConsumable) == False:
                        tambah.tambahitem(dicari, dataConsumable)
                    else:
                        print("Sudah ada consumable dengan ID tersebut!")
                else:
                    print("Masukan tidak valid")
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")

    elif userinput == "hapusitem":  # F06
        if loggedIn == True:
            if userIsAdmin == True:
                dicari = input("Masukkan ID: ")
                if dicari[0] == "G":
                    if validasi(dicari, dataGadget) == True:
                        hapus.hapusitem(dicari, dataGadget)
                    else:
                        print("Tidak ada ID gadget yang sesuai!")
                elif dicari[0] == "C":
                    if validasi(dicari, dataConsumable) == True:
                        hapus.hapusitem(dicari, dataConsumable)
                    else:
                        print("Tidak ada ID consumable yang sesuai!")
                else:
                    print("Masukan tidak valid")
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")

    elif userinput == "ubahjumlah":  # F07
        if loggedIn == True:
            if userIsAdmin == True:
                dicari = input("Masukkan ID: ")
                if dicari[0] == "G":
                    if validasi(dicari, dataGadget) == True:
                        jumlah = int(input("Masukkan jumlah: "))
                        ubahJumlah.ubahjumlah(dicari, jumlah, dataGadget)
                    else:
                        print("Tidak ada ID gadget yang sesuai!")
                elif dicari[0] == "C":
                    if validasi(dicari, dataConsumable) == True:
                        jumlah = int(input("Masukkan jumlah: "))
                        ubahJumlah.ubahjumlah(dicari, jumlah, dataConsumable)
                    else:
                        print("Tidak ada ID consumable yang sesuai!")
                else:
                    print("Masukan tidak valid")
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")

    elif userinput == "pinjam":  # F08
        if loggedIn == False:
            print("Harap login terlebih dahulu!\n")
        else:
            if userIsAdmin == True:
                print("Admin ngapain minjem item :)\n")
            else:
                inputGadget = input("Masukkan ID Gadget: ")
                if validasi(inputGadget, dataGadget) == True:
                    inputTanggal = input("Tanggal peminjaman: ")
                    inputJumlah = int(input("Jumlah peminjaman: "))
                    pinjam.pinjam(userID, inputGadget, inputTanggal, inputJumlah, dataGadget, dataInventory)
                    riwayat.writePinjam(userID, inputGadget, inputTanggal, inputJumlah, dataGadget,
                                        dataGadgetBorrowHistory)

                else:
                    print("Masukan tidak valid!\n")



    elif userinput == "kembalikan":  # F09
        if loggedIn == True:
            if not(userIsAdmin): 
               kembalikan.gadgetReturn(dataGadget, dataGadgetBorrowHistory, dataGadgetReturnHistory, userID)
            else: 
                print("Admin tidak diperkenankan memakai command ini!")
        else:
            print("User belum log in!\n")

    elif userinput == "minta"       :  # F10
        if loggedIn:
            if not(userIsAdmin):
                meminta.requestConsumable(dataConsumable, dataConsumableHistory, userID)
            else:
                print("Admin tidak diperkenankan memakai command ini!")
        else:
            print("User belum log in!\n")

    elif userinput == "riwayatpinjam":  # F11
        if loggedIn == True:
            if userIsAdmin == True:
                riwayat.readPinjam(dataGadgetBorrowHistory, dataGadget, dataUser)
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")


    elif userinput == "riwayatkembali":  # F12
        resultA = riwayat.riwayatGadget(dataGadgetReturnHistory, dataGadgetBorrowHistory, dataGadget, dataUser, 0)
        if loggedIn == True:
            if userIsAdmin == True:
                for i in resultA:
                    print(f"ID Pengembalian      : {i[1]}")
                    print(f"Nama Pengambil       : {i[2]}")
                    print(f"Nama Gadget          : {i[3]}")
                    print(f"Tanggal Pengembalian : {i[0]}")

                inp = input('Apakah anda ingin melihat 5 data lagi? y/n')

                if inp == 'y':
                    resultB = riwayat.riwayatGadget(dataGadgetReturnHistory, dataGadgetBorrowHistory, dataGadget, dataUser, 5)
                    for i in resultB:
                        print(f"ID Pengembalian      : {i[1]}")
                        print(f"Nama Pengambil       : {i[2]}")
                        print(f"Nama Gadget          : {i[3]}")
                        print(f"Tanggal Pengembalian : {i[0]}")
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")


    elif userinput == "riwayatambil":  # F13
        resultA = riwayat.riwayatConsumable(dataConsumableHistory, dataConsumable, dataUser, 0)
        if loggedIn == True:
            if userIsAdmin == True:
                for i in resultA:
                    print(f"ID Pengembalian      : {i[1]}")
                    print(f"Nama Pengambil       : {i[2]}")
                    print(f"Nama Consumable      : {i[3]}")
                    print(f"Tanggal Pengembalian : {i[0]}")
                    print(f"Jumlah               : {i[4]}")

                inp = input('Apakah anda ingin melihat 5 data lagi? y/n')

                if inp == 'y':
                    resultB = riwayat.riwayatConsumable(dataConsumableHistory, dataConsumable, dataUser, 5)
                    for i in resultB:
                        print(f"ID Pengembalian      : {i[1]}")
                        print(f"Nama Pengambil       : {i[2]}")
                        print(f"Nama Consumable      : {i[3]}")
                        print(f"Tanggal Pengembalian : {i[0]}")
                        print(f"Jumlah               : {i[4]}")
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")

    elif userinput == "help":  # F14
        help.help()

    elif userinput == "save":  # F15
        folderDir = input("\nMasukkan nama folder: ")
        saveFilesTo(folderDir)
        print("\nSaving..")
        print("Data telah disimpan pada folder " + folderDir)


    elif userinput == "exit":  # F17
        saveFiles = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        saveFiles = saveFiles.lower()
        if saveFiles == "y":
            saveFilesTo(args.folderDirectory)
            running = False
        elif saveFiles == "n":
            running = False
        else:
            print("\nInput tidak diterima")


# Sistem Argparse
parser = argparse.ArgumentParser()
parser.add_argument("folderDirectory", help="path folder yang akan dibuka sistem")
args = parser.parse_args()  # F14
try:

    # Kode di sini akan dijalankan bila folder dan file csv ada, alias
    # Main Program
    print('\nSelamat datang di "Kantong Ajaib"!\n')

    # kita load data-datanya terlebih dahulu
    loadAllFiles()

    while running:
        userinput = input(">> ")
        switchcaseInput(userinput)



except IOError:
    # exit case bila tdk ada folder
    print("Folder tidak ditemukan")
