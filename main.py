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

# Fungsi lokal
def loadAllFiles(): # Untuk loading file2 biar rapih aja
    global dataUser
    global dataGadget
    global dataConsumable
    dataUser = csv.openFileUser(args.folderDirectory + "/user.csv")
    dataGadget = csv.openFileGadget(args.folderDirectory + "/gadget.csv")
    dataConsumable = csv.openFileConsumable(args.folderDirectory + "/consumable.csv")

def saveFilesTo(folderName): # Untuk nyimpen data-data yang sekarang berupa list of array menjadi csv ke suatu folder
    if not(os.path.exists(folderName)):
        os.mkdir(folderName)
    csv.writeFileUser(folderName+"/user.csv", dataUser)
    csv.writeFileGadget(folderName+"/gadget.csv", dataGadget)
    csv.writeFileConsumable(folderName+"/consumable.csv", dataConsumable)

def modify_data(data, idx, col, value): # Untuk mengubah data di suatu data
  data[idx][col] = value

def switchcaseInput(userinput): # Switchcase input user ketika sudah me-load data
    global dataUser
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
        dicari = (input("Masukan ID: "))
        if dicari[0]=="G":
            modifikasi.tambahitem(dicari,dataGadget,userIsAdmin)
        elif dicari[0]=="C":
            modifikasi.tambahitem(dicari, dataConsumable, userIsAdmin)
        else:
            print("Masukan tidak valid")



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