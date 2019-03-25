buku = []

#fungsi untuk menampilkan semua data
def show_data():
  if len(buku) <= 0:
    print("belum ada data buku")
  else:
    for indeks in range(len(buku)):
      print "[%d] %s" % (indeks, buku[indeks])
    
#fungsi untuk memasukkan data
def insert_data():
  buku_baru = raw_input("judul buku :")
  buku.append(buku_baru)
  
#fungsi untuk mengedit data
def edit_data():
  show_data()
  indeks = input("masukkan id buku :")
  if (indeks > len(buku)):
    print("id buku salah")
  else:
    judul_baru = raw_input("masukkan judul buku baru")
    buku[indeks] = judul_baru

#fungsi untuk menghapus data
def delete_data():
  show_data()
  indeks = input("masukkan id buku :")
  if (indeks > len(buku)):
    print("id buku salah")
  else:
    buku.remove(buku[indeks])
  
#fungsi untuk memunculkan menu
def show_menu():
  print "\n"
  print "----------- MENU ----------"
  print "[1] Show Data"
  print "[2] Insert Data"
  print "[3] Edit Data"
  print "[4] Delete Data"
  print "[5] Exit"

  menu = input("pilih menu :")
  print "\n"

  #logika untuk proses
  if menu == 1:
    show_data()
  elif menu == 2:
    insert_data()
  elif menu == 3:
    edit_data()
  elif menu ==4:
    delete_data()
  elif menu == 5:
    exit()
  else:
    print("salah pilihan") 


if __name__ == "__main__":
  while(True):
    show_menu()