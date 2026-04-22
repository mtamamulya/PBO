# Kelas Induk
class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def mulai_mesin(self):
        print(f"Mesin kendaraan {self.merk} dinyalakan.")

# Kelas Anak (mewarisi dari Kendaraan)
class Mobil(Kendaraan):
    def __init__(self, merk, warna):
        self.merk = merk  # Mewarisi 'merk' tapi di-set ulang
        self.warna = warna  # Atribut khusus Mobil

    def info_mobil(self):
        print(f"Ini adalah mobil {self.merk} berwarna {self.warna}.")

# --- Kode Utama ---
if __name__ == "__main__":
    mobil_tesla = Mobil("Tesla Model S", "Merah")
    # Memanggil metode dari kelas anak
    mobil_tesla.info_mobil()
    # Memanggil metode yang diwarisi dari kelas induk
    mobil_tesla.mulai_mesin()
    # Mengakses atribut yang diwarisi
    print(f"Merk mobil: {mobil_tesla.merk}")