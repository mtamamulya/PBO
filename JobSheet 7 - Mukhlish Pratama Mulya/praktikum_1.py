class DataStore:
    def __init__(self, nama_store="Default Store"):
        # Dictionary internal untuk menyimpan data (anggap sebagai 'protected')
        self._data = {}
        self.nama = nama_store
        print(f"DataStore '{self.nama}' dibuat.")

    def tambah_data(self, key, value):
        """Menambahkan data ke dalam store."""
        print(f"[{self.nama}] Menambahkan data: '{key}' -> {value}")
        self._data[key] = value
        print(" -> Data berhasil ditambahkan.")

    def get_data(self, key):
        """
        Mencoba mendapatkan data berdasarkan key.
        Menangani KeyError jika key tidak ada.
        """
        print(f"[{self.nama}] Mencoba mengambil data dengan key: '{key}'")
        try:
            # Baris ini berpotensi menimbulkan KeyError
            nilai = self._data[key]
            print(f" -> Data ditemukan: {nilai}")
            return nilai
        except KeyError:
            # Blok ini dijalankan jika KeyError terjadi di blok try
            print(f" -> ERROR: Key '{key}' tidak ditemukan di DataStore '{self.nama}'.")
            # Mengembalikan None atau nilai default lain sebagai indikasi gagal
            return None

# --- Kode Utama ---
if __name__ == "__main__":
    # Membuat instance DataStore
    store_produk = DataStore("Toko Produk")

    # Menambahkan beberapa data
    store_produk.tambah_data("Buku Tulis", 15000)
    store_produk.tambah_data("Pensil 2B", 2000)

    # Mengambil data yang ada (seharusnya berhasil)
    print("\nMengambil data yang ADA:")
    harga_buku = store_produk.get_data("Buku Tulis")
    if harga_buku is not None:
        print(f" Harga Buku Tulis adalah: {harga_buku}")

    # Mengambil data yang TIDAK ada (seharusnya memicu except)
    print("\nMengambil data yang TIDAK ADA:")
    harga_penggaris = store_produk.get_data("Penggaris")
    if harga_penggaris is None:
        print(" Harga Penggaris tidak ditemukan (sesuai ekspektasi).")