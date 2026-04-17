# 1. Fungsi Built-in
# Fungsi print() adalah contoh fungsi built-in untuk mencetak output
print("Ini adalah contoh fungsi built-in")

# Fungsi len() untuk menghitung panjang suatu objek
kata = "Pemrograman"
panjang_kata = len(kata)
print(f"Panjang kata '{kata}' adalah: {panjang_kata}")

# Fungsi max() untuk mencari nilai maksimum dari sebuah daftar
angka_list = [10, 5, 30, 40, 25]
nilai_max = max(angka_list)
print(f"Nilai maksimum dalam daftar {angka_list} adalah: {nilai_max}")


# 2. Fungsi User-Defined (Definisi Fungsi)

# Fungsi dengan satu parameter
def cetak_kuadrat(angka):
    # Menghitung kuadrat dari angka yang diterima
    print(f"Kuadrat dari {angka} adalah: {angka ** 2}")

# Fungsi dengan beberapa parameter
def hitung_luas_persegi_panjang(panjang, lebar):
    # Menghitung luas dan mengembalikan nilainya
    return panjang * lebar

# Fungsi dengan berbagai tipe parameter
def info_mahasiswa(nama, umur, ipk):
    # Mencetak informasi mahasiswa
    print(f"Nama: {nama}, Umur: {umur}, IPK: {ipk}")

# Fungsi tanpa return value (Non-return value)
def sapa_pengguna(nama):
    # Hanya mencetak sapaan
    print(f"Halo, {nama}! Selamat datang di dunia Python.")

# Fungsi dengan return value
def hitung_keliling_persegi(sisi):
    # Mengembalikan keliling persegi
    return 4 * sisi


# 3. Pemanggilan Fungsi

print("\n--- EKSEKUSI FUNGSI ---")

# Memanggil fungsi satu parameter
cetak_kuadrat(5)

# Memanggil fungsi beberapa parameter & menyimpan hasilnya
luas = hitung_luas_persegi_panjang(10, 5)
print(f"Luas persegi panjang: {luas}")

# Memanggil fungsi dengan berbagai tipe data
info_mahasiswa("Budi", 22, 3.8)

# Memanggil fungsi tanpa return
sapa_pengguna("Andi")

# Memanggil fungsi dengan return & mencetak langsung
keliling = hitung_keliling_persegi(5)
print(f"Keliling persegi dengan sisi 5 adalah: {keliling}")