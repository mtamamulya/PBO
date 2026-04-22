# Kelas Induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara generik.")

    def tampilkan_info(self):
        print(f"Ini adalah hewan bernama {self.nama}.")

# Kelas Anak
class Kucing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama) # Panggil init induk
        self.ras = ras

    # Method Overriding untuk bersuara
    def bersuara(self):
        print(f"{self.nama} (Kucing) mengeong: Meow!")

    # Method Overriding untuk tampilkan_info, memanggil versi induk
    def tampilkan_info(self):
        super().tampilkan_info() 
        print(f"Ini adalah kucing ras {self.ras}.")

# --- Kode Utama ---
if __name__ == "__main__":
    hewan_umum = Hewan("Makhluk")
    kucing_persia = Kucing("Puspus", "Persia")

    print("Info Hewan Umum:")
    hewan_umum.tampilkan_info()
    hewan_umum.bersuara()
    print("-" * 20)

    print("Info Kucing Persia:")
    kucing_persia.tampilkan_info()
    kucing_persia.bersuara()