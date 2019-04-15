class karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama=nama
        self.gaji=gaji
        karyawan.jumlah_karyawan+=1

    def tampilkan_jumlah(self):
        print ("jumlah karyawan :",karyawan.jumlah_karyawan)

    def tampilkan_profile(self):
        print ("nama karyawan :",self.nama)
        print ("gaji karyawan :",self.gaji)
        print()

 
# Membuat objek pertama dari kelas Karyawan
karyawan1 = karyawan("andre putra", 7000000)
# Membuat objek kedua dari kelas Karyawan
karyawan2 = karyawan("naya safitri", 7000000)

karyawan1.tampilkan_profile()
karyawan2.tampilkan_profile()
print("Total karyawan :", karyawan.jumlah_karyawan)       
                
        