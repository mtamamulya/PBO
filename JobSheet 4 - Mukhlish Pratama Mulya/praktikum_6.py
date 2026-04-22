class BentukGeometri:
    def __init__(self, nama_bentuk):
        self.nama = nama_bentuk
    def tampilkan_nama(self):
        print(f"Ini adalah bentuk: {self.nama}")
    def hitung_luas(self):
        print(f"Luas {self.nama} tidak dapat dihitung (generik).")

class PersegiPanjang(BentukGeometri):
    def __init__(self, panjang, lebar):
        super().__init__("Persegi Panjang")
        self.panjang = panjang
        self.lebar = lebar
    def hitung_luas(self):
        print(f"Luas {self.nama}: {self.panjang * self.lebar}")

class Segitiga(BentukGeometri):
    def __init__(self, alas, tinggi):
        super().__init__("Segitiga")
        self.alas = alas
        self.tinggi = tinggi
    def hitung_luas(self):
        print(f"Luas {self.nama}: {0.5 * self.alas * self.tinggi}")

def proses_bentuk(bentuk):
    print(f"\nMemproses objek: {type(bentuk)}")
    if isinstance(bentuk, BentukGeometri):
        bentuk.tampilkan_nama()
        print("Objek ini adalah instance dari BentukGeometri.")
    
    if isinstance(bentuk, PersegiPanjang):
        print("-> Objek ini juga instance dari PersegiPanjang.")
    elif isinstance(bentuk, Segitiga):
        print("-> Objek ini juga instance dari Segitiga.")
    else:
        print("Objek ini BUKAN instance dari PersegiPanjang atau Segitiga.")

# --- Kode Utama ---
if __name__ == "__main__":
    pp = PersegiPanjang(4, 3)
    seg = Segitiga(5, 2)
    bg = BentukGeometri("Lingkaran")
    
    daftar_objek = [pp, seg, bg]
    for obj in daftar_objek:
        proses_bentuk(obj)