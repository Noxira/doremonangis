#-----------------------------------------------------------
#                   BAGIAN FUNGSI GLOBAL [START]
#-----------------------------------------------------------

def convert_datas_to_string(datas, header):
  string_data = header + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ";".join(arr_data_all_string)
    string_data += "\n"
  return string_data

def convert_line_to_data(line):
  raw_array_of_data = line.split(";")
  array_of_data = [data.strip() for data in raw_array_of_data]
  return array_of_data

#-----------------------------------------------------------
#                   BAGIAN FUNGSI GLOBAL [END]
#-----------------------------------------------------------

#-----------------------------------------------------------
#                   BAGIAN USER.CSV [START]
#-----------------------------------------------------------

# Inisiasi Fungsi2
def user_convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(6):
    if(i == 0):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy

# Fungsi open file dan save file
def openFileUser(fileName):
    f = open(fileName,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    del lines[0]
    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = user_convert_array_data_to_real_values(array_of_data)
        datas.append(real_values)
    return datas

def writeFileUser(fileName, datas):
    f = open(fileName, "w")
    datas_as_string = convert_datas_to_string(datas, "id;username;nama;alamat;password;role")
    f.write(datas_as_string)
    f.close()

#-----------------------------------------------------------
#                   BAGIAN USER.CSV [END]
#-----------------------------------------------------------


#-----------------------------------------------------------
#                   BAGIAN GADGET.CSV [START]
#-----------------------------------------------------------

# Inisiasi Fungsi2
def gadget_convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(6):
    if(i == 3) or (i == 5):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy


# Fungsi open file dan save file
def openFileGadget(fileName):
    f = open(fileName,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    del lines[0]
    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = gadget_convert_array_data_to_real_values(array_of_data)
        datas.append(real_values)
    return datas

def writeFileGadget(fileName, datas):
    f = open(fileName, "w")
    datas_as_string = convert_datas_to_string(datas, "id;nama;deskripsi;jumlah;rarity;tahun_ditemukan")
    f.write(datas_as_string)
    f.close()

#-----------------------------------------------------------
#                   BAGIAN GADGET.CSV [END]
#-----------------------------------------------------------

#-----------------------------------------------------------
#                   BAGIAN CONSUMABLE.CSV [START]
#-----------------------------------------------------------

# Inisiasi Fungsi2
def consumable_convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(5):
    if(i == 3):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy


# Fungsi open file dan save file
def openFileConsumable(fileName):
    f = open(fileName,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    del lines[0]
    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = consumable_convert_array_data_to_real_values(array_of_data)
        datas.append(real_values)
    return datas

def writeFileConsumable(fileName, datas):
    f = open(fileName, "w")
    datas_as_string = convert_datas_to_string(datas, "id;nama;deskripsi;jumlah;rarity")
    f.write(datas_as_string)
    f.close()

#-----------------------------------------------------------
#                   BAGIAN CONSUMABLE.CSV [END]
#-----------------------------------------------------------

#-----------------------------------------------------------
#                   BAGIAN CONSUMABLE_HISTORY.CSV [START]
#-----------------------------------------------------------

# Inisiasi Fungsi2
def consumable_history_convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(5):
    if(i == 4 or i == 0 or i == 1 or i == 2):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy


# Fungsi open file dan save file
def openFileConsumableHistory(fileName):
    f = open(fileName,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    del lines[0]
    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = consumable_history_convert_array_data_to_real_values(array_of_data)
        datas.append(real_values)
    return datas

def writeFileConsumableHistory(fileName, datas):
    f = open(fileName, "w")
    datas_as_string = convert_datas_to_string(datas, "id;id_pengambil;id_consumable;tanggal_pengambilan;jumlah")
    f.write(datas_as_string)
    f.close()

#-----------------------------------------------------------
#                   BAGIAN CONSUMABLE_HISTORY.CSV [END]
#-----------------------------------------------------------

#-----------------------------------------------------------
#                   BAGIAN GADGET_BORROW_HISTORY.CSV [START]
#-----------------------------------------------------------

# Inisiasi Fungsi2
def gadget_borrow_history_convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(6):
    if(i == 4 or i == 0 or i == 1):
      arr_cpy[i] = int(arr_cpy[i])
    elif(i == 5):
      arr_cpy[i] = bool(True) if arr_cpy[i] == "True" else bool(False)
  return arr_cpy


# Fungsi open file dan save file
def openFileGadgetBorrowHistory(fileName):
    f = open(fileName,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    del lines[0]
    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = gadget_borrow_history_convert_array_data_to_real_values(array_of_data)
        datas.append(real_values)
    return datas

def writeFileGadgetBorrowHistory(fileName, datas):
    f = open(fileName, "w")
    datas_as_string = convert_datas_to_string(datas, "id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah;is_returned")
    f.write(datas_as_string)
    f.close()

#-----------------------------------------------------------
#                   BAGIAN GADGET_BORROW_HISTORY.CSV [END]
#-----------------------------------------------------------

#-----------------------------------------------------------
#                   BAGIAN GADGET_RETURN_HISTORY.CSV [START]
#-----------------------------------------------------------

# Inisiasi Fungsi2
def gadget_return_history_convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(4):
    if(i == 0 or i == 1 or i==3):
      arr_cpy[i] = int(arr_cpy[i])
  return arr_cpy


# Fungsi open file dan save file
def openFileGadgetReturnHistory(fileName):
    f = open(fileName,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    del lines[0]
    datas = []
    for line in lines:
        array_of_data = convert_line_to_data(line)
        real_values = gadget_return_history_convert_array_data_to_real_values(array_of_data)
        datas.append(real_values)
    return datas

def writeFileGadgetReturnHistory(fileName, datas):
    f = open(fileName, "w")
    datas_as_string = convert_datas_to_string(datas, "id;id_peminjaman;tanggal_pengembalian;jumlah")
    f.write(datas_as_string)
    f.close()

#-----------------------------------------------------------
#                   BAGIAN GADGET_RETURN_HISTORY.CSV [END]
#-----------------------------------------------------------