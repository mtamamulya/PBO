class Burung:
    def __init__(self, nama):
        self.nama = nama
    def terbang(self):
        print(f"{self.nama} terbang dengan cara umum.")
    def bersuara(self):
        print(f"{self.nama} mengeluarkan suara burung.")

class Elang(Burung):
    def __init__(self, nama, rentang_sayap):
        super().__init__(nama)
        self.rentang_sayap = rentang_sayap
    def terbang(self):
        print(f"{self.nama} terbang tinggi melayang di angkasa.")
    def bersuara(self):
        print(f"{self.nama} berteriak nyaring!")

class Pipit(Burung):
    def __init__(self, nama, warna_bulu):
        super().__init__(nama)
        self.warna_bulu = warna_bulu
    def terbang(self):
        print(f"{self.nama} terbang cepat di antara pepohonan.")
    def bersuara(self):
        print(f"{self.nama} berkicau merdu: Cit cit!")

def demonstrasi_aksi_burung(daftar_burung):
    for burung in daftar_burung:
        burung.terbang()
        burung.bersuara()

if __name__ == "__main__":
    koleksi_burung = [Elang("Elang Jawa", 1.5), Pipit("Pipit Gereja", "Coklat"), Burung("Burung Misterius")]
    demonstrasi_aksi_burung(koleksi_burung)