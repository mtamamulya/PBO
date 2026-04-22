import locale

# Set locale ke Indonesia (jika tersedia)
try:
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
except locale.Error:
    print("Locale id_ID.UTF-8 tidak tersedia.")

def format_rupiah(angka):
    return locale.currency(angka, grouping=True, symbol='Rp ')

class Pegawai:
    def __init__(self, nama, id_pegawai, gaji_pokok):
        self.nama = nama
        self.id_pegawai = id_pegawai
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

    def tampilkan_info(self):
        print(f"ID: {self.id_pegawai}, Nama: {self.nama}")
        print(f"Gaji Pokok: {format_rupiah(self.gaji_pokok)}")

class Manager(Pegawai):
    def __init__(self, nama, id_pegawai, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, id_pegawai, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan

    def hitung_gaji(self):
        return super().hitung_gaji() + self.tunjangan_jabatan

    def tampilkan_info(self):
        print("--- Info Manager ---")
        super().tampilkan_info()
        print(f"Tunjangan Jabatan: {format_rupiah(self.tunjangan_jabatan)}")
        print(f"Total Gaji: {format_rupiah(self.hitung_gaji())}")

class StafTeknis(Pegawai):
    def __init__(self, nama, id_pegawai, gaji_pokok, keahlian, bonus_keahlian):
        super().__init__(nama, id_pegawai, gaji_pokok)
        self.keahlian = keahlian
        self.bonus_keahlian = bonus_keahlian

    def hitung_gaji(self):
        return super().hitung_gaji() + self.bonus_keahlian

    def tampilkan_info(self):
        print("--- Info Staf Teknis ---")
        super().tampilkan_info()
        print(f"Keahlian: {self.keahlian}")
        print(f"Bonus Keahlian: {format_rupiah(self.bonus_keahlian)}")
        print(f"Total Gaji: {format_rupiah(self.hitung_gaji())}")

# --- Kode Utama ---
if __name__ == "__main__":
    manager1 = Manager("Budi Santoso", "M001", 10000000, 5000000)
    staf1 = StafTeknis("Citra Lestari", "S001", 7000000, "Python Programming", 1500000)
    
    manager1.tampilkan_info()
    print("-" * 30)
    staf1.tampilkan_info()