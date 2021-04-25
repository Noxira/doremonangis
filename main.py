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
from Functions import modifikasi
from Functions import user
from Functions import riwayat


# Fungsi lokal
def loadAllFiles(): # Untuk loading file2 biar rapih aja
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
    dataInventory = csv.openFileInventory(args.folderDirectory +"/inventory.csv")

def saveFilesTo(folderName): # Untuk nyimpen data-data yang sekarang berupa list of array menjadi csv ke suatu folder
    if not(os.path.exists(folderName)):
        os.mkdir(folderName)
    csv.writeFileUser(folderName+"/user.csv", dataUser)
    csv.writeFileGadget(folderName+"/gadget.csv", dataGadget)
    csv.writeFileConsumable(folderName+"/consumable.csv", dataConsumable)
    csv.writeFileConsumableHistory(folderName+"/consumable_history.csv", dataConsumableHistory)
    csv.writeFileGadgetBorrowHistory(folderName+"/gadget_borrow_history.csv", dataGadgetBorrowHistory)
    csv.writeFileGadgetReturnHistory(folderName+"/gadget_return_history.csv", dataGadgetReturnHistory)
    csv.writeFileInventory(folderName +"/inventory.csv", dataInventory)


def modify_data(data, idx, col, value): # Untuk mengubah data di suatu data
  data[idx][col] = value

#fungsi validasi, bernilai True jika terdapat ID sesuai didalam file csv
def validasi(masukan,namaFiles):
    kondisi = False
    for i in range (len(namaFiles)):
        if namaFiles[i][0]==masukan:
            kondisi=True
    return kondisi


def switchcaseInput(userinput): # Switchcase input user ketika sudah me-load data
    global dataUser
    global namaUser     # Menyimpan nama user yang sedang login
    global userIsAdmin  # [Penting] akan menyimpan apakah user admin atau tidak (Bool)
    global running
    global loggedIn     # [Penting] akan menyimpan apakah user sudah login atau belum (Bool)
    if userinput == "register":
        print("")
        dataUser = register.addNewUser(dataUser)
    elif userinput == "login":
        print("")
        userTemp = input("Masukkan username: ")
        passTemp = input("Masukkan password: ")
        if login.passwordCheck(dataUser, userTemp, passTemp):
            print("\nHalo " + userTemp + "! Selamat datang di Kantong Ajaib")
            loggedIn = True
            if login.isAdmin(dataUser, userTemp):
                userIsAdmin = True
            else:
                userIsAdmin = False
                namaUser = userTemp
        else:
            print("\nPassword atau Username salah!")

    elif userinput == "save":
        folderDir = input("\nMasukkan nama folder:")
        saveFilesTo(folderDir)

        print("\nSaving..")
        print("Data telah disimpan pada folder "+ folderDir)

    elif userinput == "exit":
        saveFiles = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        saveFiles = saveFiles.lower()
        if saveFiles == "y":
            saveFilesTo(args.folderDirectory)
            running = False
        elif saveFiles == "n":
            running = False
        else:
            print("\nInput tidak diterima")

    elif userinput =="carirarity":
        dicari = str(input("Masukan rarity: "))
        search.carirarity(dicari, dataGadget)

    elif userinput =="caritahun":
        dicari = int(input("Masukan tahun: "))
        kategori = str(input("Masukan kategori: "))
        search.caritahun(dicari, kategori, dataGadget)

    elif userinput=="tambahitem":
        if loggedIn==False:
            print("Harap login terlebih dahulu!")
        else:
            if userIsAdmin == False:
                print("Hanya Admin yang dapat menambahkan item")
            else:
                dicari = (input("Masukan ID: "))
                if dicari[0]=="G":
                    if validasi(dicari,dataGadget)==False:
                        modifikasi.tambahitem(dicari,dataGadget)
                    else:
                        print("Sudah ada gadget dengan ID tersebut!")
                elif dicari[0]=="C":
                    if validasi(dicari,dataConsumable)==False:
                        modifikasi.tambahitem(dicari, dataConsumable)
                    else:
                        print("Sudah ada consumable item dengan ID tersebut!")
                else:
                    print("Masukan tidak valid")

    elif userinput =="hapusitem":
        if loggedIn == False:
            print("Harap login terlebih dahulu!")
        else:
            if userIsAdmin == False:
                print("Hanya Admin yang dapat menambahkan item")
            else:
                dicari = input("Masukkan ID item yang ingin dihapus")
                if dicari[0] == "G":
                    if validasi(dicari, dataGadget) == True:
                        modifikasi.hapusitem(dicari, dataGadget)
                    else:
                        print("Tidak ada ID gadget yang sesuai!")
                elif dicari[0] == "C":
                    if validasi(dicari, dataConsumable) == True:
                        modifikasi.hapusitem(dicari, dataConsumable)
                    else:
                        print("Tidak ada ID consumable yang sesuai!")
                else:
                    print("Masukan tidak valid")

    elif userinput == "ubahjumlah":
        if loggedIn == False:
            print("Harap login terlebih dahulu!")
        else:
            if userIsAdmin == False:
                print("Hanya Admin yang dapat mengubah stok item")
            else:
                dicari = input("Masukkan ID: ")
                jumlah = int(input("Masukkan jumlah: "))
                if dicari[0] == "G":
                    if validasi(dicari, dataGadget) == True:
                        modifikasi.ubahjumlah(dicari,jumlah, dataGadget)
                    else:
                        print("Tidak ada ID gadget yang sesuai!")
                elif dicari[0] == "C":
                    if validasi(dicari, dataConsumable) == True:
                        modifikasi.ubahjumlah(dicari,jumlah, dataConsumable)
                    else:
                        print("Tidak ada ID consumable yang sesuai!")
                else:
                    print("Masukan Tidak Valid!")


    elif userinput =="pinjam":
        if loggedIn == False:
            print("Harap login terlebih dahulu!")
        else:
            if userIsAdmin == True:
                print("Admin ngapain minjem item :)")
            else:
                inputGadget     = input("Masukkan ID Gadget: ")
                if validasi(inputGadget, dataGadget) == True:
                    inputTanggal    = input("Tanggal peminjaman: ")
                    inputJumlah     = int(input("Jumlah peminjaman: "))
                    user.pinjam(namaUser,inputGadget, inputTanggal, inputJumlah, dataGadget, dataInventory)
                    riwayat.riwayatpinjam(namaUser,inputGadget, inputTanggal, inputJumlah, dataGadget, dataGadgetBorrowHistory)





# Variabel lokal
running = True
loggedIn = False

# Sistem Argparse
parser = argparse.ArgumentParser()
parser.add_argument("folderDirectory", help="path folder yang akan dibuka sistem")
args = parser.parse_args()
try:
    # Kode di sini akan dijalankan bila folder ada, alias
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
