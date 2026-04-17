# Kelas untuk menjelaskan atribut dan metode dalam kelas
class Mobil:
    def __init__(self, merk, warna, tahun, harga):
        # Atribut: Data yang dimiliki oleh objek Mobil
        self.merk = merk
        self.warna = warna
        self.tahun = tahun
        self.harga = harga 

    # Metode 1: Tanpa return value (hanya mencetak informasi)
    def tampilkan_info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}, tahun {self.tahun}, harga: Rp {self.harga}")

    # Metode 2: Dengan satu parameter (input diskon)
    def diskon(self, persen_diskon):
        diskon_harga = self.harga * (persen_diskon / 100)
        harga_setelah_diskon = self.harga - diskon_harga
        print(f"Harga setelah diskon {persen_diskon}%: Rp {harga_setelah_diskon}")

    # Metode 3: Dengan return value (mengembalikan hasil hitungan)
    def hitung_usia(self, tahun_sekarang):
        usia = tahun_sekarang - self.tahun
        return usia

    # Metode 4: Dengan beberapa parameter (update data)
    def perbarui_harga(self, harga_baru, tahun_baru): 
        self.harga = harga_baru
        self.tahun = tahun_baru
        print(f"Harga dan tahun mobil {self.merk} diperbarui menjadi Rp {self.harga} dan tahun {self.tahun}")

# --- Eksekusi Program ---

# Membuat objek mobil
mobil1 = Mobil("Toyota", "Hitam", 2015, 300000000)
mobil2 = Mobil("Honda", "Merah", 2018, 250000000)

# Menggunakan metode-metode objek
mobil1.tampilkan_info()
mobil1.diskon(10)

# Mengambil nilai dari return value
usia_mobil1 = mobil1.hitung_usia(2026)
print(f"Usia mobil1 pada tahun 2026: {usia_mobil1} tahun")

# Memperbarui data objek
mobil1.perbarui_harga(280000000, 2022)