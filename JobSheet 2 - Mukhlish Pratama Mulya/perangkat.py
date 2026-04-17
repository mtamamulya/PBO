# Modul perangkat.py untuk mendefinisikan kelas HP
class Handphone:
    def __init__(self, merk, model, harga, stok):
        self.merk = merk
        self.model = model
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"[{self.merk}] {self.model}")
        print(f"Harga: Rp {self.harga:,}")
        print(f"Stok tersedia: {self.stok} unit")
        print("-" * 30)

    def kurangi_stok(self, jumlah):
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        else:
            print(f"Maaf, stok {self.model} tidak mencukupi!")
            return False

def hitung_total_bayar(harga, jumlah):
    # Fungsi sederhana untuk menghitung total belanja
    return harga * jumlah