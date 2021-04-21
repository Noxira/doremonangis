#make polynomial rolling hash function
# https://www.geeksforgeeks.org/string-hashing-using-polynomial-rolling-hash-function/

# unhashed = str(input("Masukkan string: "))  # input user untuk dihash
# hashed = int(0)                             # hasil hash
# k = int(31)                                 # suatu konstanta pengali
# top = int(1e9 + 9)                               # batas atas

# for i in range(len(unhashed)):
#     hashed = (hashed + (ord(unhashed[i]) * (k**i))) % top

# print(hashed)

def RollingHash(unhashed):
    hashed = int(0)                             # hasil hash
    k = int(31)                                 # suatu konstanta pengali
    top = int(1e9 + 9)                          # batas atas
    for i in range(len(unhashed)):
        hashed = (hashed + (ord(unhashed[i]) * (k**i))) % top
    return(hashed)