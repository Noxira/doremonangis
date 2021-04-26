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
from Functions import kembalikan

# Variabel lokal
running = True
loggedIn = False
userIsAdmin = False

# Fungsi lokal
def loadAllFiles(): # Untuk loading file2 biar rapih aja
    global dataUser
    global dataGadget
    global dataConsumable
    global dataConsumableHistory
    global dataGadgetBorrowHistory
    global dataGadgetReturnHistory
    dataUser = csv.openFileUser(args.folderDirectory + "/user.csv")
    dataGadget = csv.openFileGadget(args.folderDirectory + "/gadget.csv")
    dataConsumable = csv.openFileConsumable(args.folderDirectory + "/consumable.csv")
    dataConsumableHistory = csv.openFileConsumableHistory(args.folderDirectory + "/consumable_history.csv")
    dataGadgetBorrowHistory = csv.openFileGadgetBorrowHistory(args.folderDirectory + "/gadget_borrow_history.csv")
    dataGadgetReturnHistory = csv.openFileGadgetReturnHistory(args.folderDirectory + "/gadget_return_history.csv")

def saveFilesTo(folderName): # Untuk nyimpen data-data yang sekarang berupa list of array menjadi csv ke suatu folder
    if not(os.path.exists(folderName)):
        os.mkdir(folderName)
    csv.writeFileUser(folderName+"/user.csv", dataUser)
    csv.writeFileGadget(folderName+"/gadget.csv", dataGadget)
    csv.writeFileConsumable(folderName+"/consumable.csv", dataConsumable)
    csv.writeFileConsumableHistory(folderName+"/consumable_history.csv", dataConsumableHistory)
    csv.writeFileGadgetBorrowHistory(folderName+"/gadget_borrow_history.csv", dataGadgetBorrowHistory)
    csv.writeFileGadgetReturnHistory(folderName+"/gadget_return_history.csv", dataGadgetReturnHistory)

def modify_data(data, idx, col, value): # Untuk mengubah data di suatu data
  data[idx][col] = value

def switchcaseInput(userinput): # Switchcase input user ketika sudah me-load data
    global dataUser
    global running
    global userID       # Menyimpan ID User utk dipakai selanjutnya
    global userIsAdmin  # [Penting] akan menyimpan apakah user admin atau tidak (Bool)
    global loggedIn     # [Penting] akan menyimpan apakah user sudah login atau belum (Bool)
    
    if userinput == "register":
        if loggedIn == True:                                                            # F01
            if userIsAdmin == True:
                print("")
                dataUser = register.addNewUser(dataUser)
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")

    elif userinput == "login":                                                          # F02
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
    
    elif userinput =="carirarity":                                                      # F03
        if loggedIn == True:
            dicari = str(input("Masukan rarity: "))
            search.carirarity(dicari, dataGadget)
        else:
            print("User belum log in!")

    elif userinput =="caritahun":                                                       # F04
        if loggedIn == True: 
            dicari = int(input("Masukan tahun: "))
            kategori = str(input("Masukan kategori: "))
            search.caritahun(dicari, kategori, dataGadget)
        else: 
            print("User belum log in!\n")

    elif userinput=="tambahitem":                                                       # F05
        if loggedIn == True:
            if userIsAdmin == True:
                dicari = (input("Masukan ID: "))
                if dicari[0]=="G":
                    modifikasi.tambahitem(dicari,dataGadget,userIsAdmin)
                elif dicari[0]=="C":
                    modifikasi.tambahitem(dicari, dataConsumable, userIsAdmin)
                else:
                    print("Masukan tidak valid")
            else:
                print("User bukan admin!\n")
        else:
            print("User belum log in!\n")

    elif userinput == "kembalikan":
        if loggedIn == True:
            kembalikan.gadgetReturn(dataGadget, dataGadgetBorrowHistory, dataGadgetReturnHistory, userID)
        else:
            print("User belum log in!\n")

    elif userinput == "save":                                                           # F15
        folderDir = input("\nMasukkan nama folder: ")
        saveFilesTo(folderDir)

        print("\nSaving..")
        print("Data telah disimpan pada folder "+ folderDir)

    elif userinput == "exit":                                                           # F17
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
args = parser.parse_args()                                                              # F14
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