class Komputer:
    def __init__(self, merk, processor, ram_gb):
        self.merk = merk
        self.processor = processor
        self.ram_gb = ram_gb

    def info_spesifikasi(self):
        print(f"Merk: {self.merk}")
        print(f"Processor: {self.processor}")
        print(f"RAM: {self.ram_gb} GB")

    def jalankan_aplikasi(self, nama_aplikasi):
        print(f"{self.merk} menjalankan aplikasi: {nama_aplikasi}...")

    # Simulasi Overloading (Opsi A: Default Argument)
    def upgrade_ram(self, tambahan_gb, tipe_ram="DDR4"):
        self.ram_gb += tambahan_gb
        print(f"RAM {self.merk} diupgrade sebesar {tambahan_gb} GB (Tipe: {tipe_ram}). Total RAM sekarang: {self.ram_gb} GB.")

class Laptop(Komputer):
    def __init__(self, merk, processor, ram_gb, ukuran_layar, berat):
        super().__init__(merk, processor, ram_gb)
        self.ukuran_layar = ukuran_layar
        self.berat = berat

    def info_spesifikasi(self):
        super().info_spesifikasi()
        print(f"Ukuran Layar: {self.ukuran_layar} inch")
        print(f"Berat: {self.berat} Kg")

class Desktop(Komputer):
    def __init__(self, merk, processor, ram_gb, jenis_casing, monitor_external):
        super().__init__(merk, processor, ram_gb)
        self.jenis_casing = jenis_casing
        self.monitor_external = monitor_external

    def info_spesifikasi(self):
        super().info_spesifikasi()
        print(f"Jenis Casing: {self.jenis_casing}")
        print(f"Monitor External: {'Ya' if self.monitor_external else 'Tidak'}")

# Fungsi Polimorfisme
def cetak_semua_spesifikasi(daftar_komputer):
    for kompi in daftar_komputer:
        print("-" * 20)
        kompi.info_spesifikasi()

# Main Program
if __name__ == "__main__":
    pc1 = Laptop("Asus", "Intel i5", 16, 14.0, 1.5)
    pc2 = Desktop("Lenovo", "AMD Ryzen 7", 32, "Tower", True)

    daftar = [pc1, pc2]
    
    cetak_semua_spesifikasi(daftar)
    
    # Demonstrasi Overloading (Default Argumen)
    print("\n--- Simulasi Upgrade RAM ---")
    pc1.upgrade_ram(8)           # Menggunakan tipe_ram default
    pc1.upgrade_ram(8, "DDR5")   # Menggunakan argumen eksplisit