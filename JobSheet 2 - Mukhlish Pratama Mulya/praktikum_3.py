# 1. Kelas Buku untuk merepresentasikan buku di perpustakaan
class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.status = "Tersedia"  # Status default

    def tampilkan_info(self):
        print(f"Judul: {self.judul}")
        print(f"Pengarang: {self.pengarang}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Status: {self.status}")

    def pinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
            print(f"Buku '{self.judul}' telah dipinjam.")
        else:
            print(f"Buku '{self.judul}' sedang dipinjam.")

    def kembalikan(self):
        if self.status == "Dipinjam":
            self.status = "Tersedia"
            print(f"Buku '{self.judul}' telah dikembalikan.")
        else:
            print(f"Buku '{self.judul}' tidak sedang dipinjam.")

# Membuat objek dari kelas Buku
buku1 = Buku("Pemrograman Python", "John Doe", 2021)
buku2 = Buku("Data Science untuk Pemula", "Jane Smith", 2020)

# Menggunakan metode objek Buku
buku1.tampilkan_info()
buku2.pinjam()
buku2.kembalikan()
buku1.pinjam()
buku1.tampilkan_info()

print("-" * 30)

# 2. Kelas Mahasiswa untuk merepresentasikan Mahasiswa dalam kelas
class Mahasiswa:
    # Konstruktor untuk menginisialisasi atribut objek
    def __init__(self, nama, nim, umur):
        self.nama = nama 
        self.nim = nim   
        self.umur = umur 

    # Metode untuk menampilkan informasi mahasiswa
    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Umur: {self.umur} tahun")

    # Metode untuk merubah umur mahasiswa
    def ubah_umur(self, umur_baru):
        self.umur = umur_baru

# Membuat objek (instance) dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Andi", "12345", 20)
mahasiswa2 = Mahasiswa("Budi", "67890", 22)

# Menggunakan metode dari kelas Mahasiswa
mahasiswa1.tampilkan_info()
print()
mahasiswa2.tampilkan_info()

# Mengubah umur mahasiswa1
mahasiswa1.ubah_umur(21)

print("\nSetelah mengubah umur mahasiswa1:")
mahasiswa1.tampilkan_info()