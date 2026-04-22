# Kelas Induk Level 1
class Organisme:
    def __init__(self, nama):
        self.nama = nama
        print(f"Organisme '{self.nama}' diciptakan.")

    def bernapas(self):
        print(f"{self.nama} sedang bernapas.")

# Kelas Anak Level 1
class Hewan(Organisme):
    def __init__(self, nama, jenis_makanan):
        super().__init__(nama)
        self.jenis_makanan = jenis_makanan
        print(f"Hewan '{self.nama}' adalah {self.jenis_makanan}.")

    def bergerak(self):
        print(f"{self.nama} sedang bergerak.")

# Kelas Anak Level 2
class Mamalia(Hewan):
    def __init__(self, nama, jenis_makanan, jumlah_kaki):
        super().__init__(nama, jenis_makanan)
        self.jumlah_kaki = jumlah_kaki
        print(f"Mamalia '{self.nama}' memiliki {self.jumlah_kaki} kaki.")

    def menyusui(self):
        print(f"{self.nama} sedang menyusui.")

# --- Kode Utama ---
if __name__ == "__main__":
    kucing = Mamalia("Kucing Persia", "Karnivora", 4)
    print("-" * 20)
    kucing.menyusui()
    kucing.bergerak()
    print(f"Jenis makanan: {kucing.jenis_makanan}")
    kucing.bernapas()
    print(f"Nama organisme: {kucing.nama}")