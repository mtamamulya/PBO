
class InventarisBarang:
    def __init__(self):
        # Menginisialisasi atribut protected berupa dictionary kosong
        self._items = {}
        print("Sistem Inventaris Barang siap digunakan.\n")

    def tambah_barang(self, kode, jumlah):
        # tambah_barang
        try:
            jumlah_int = int(jumlah)
            if jumlah_int <= 0:
                raise ValueError("Jumlah harus berupa integer positif.")
        except ValueError as e:
            # Menangkap ValueError jika input bukan angka atau <= 0
            print(f"[Error Input Tambah] {e}")
            return

        if kode in self._items:
            # Bangkitkan KeyError jika barang sudah ada
            raise KeyError(f"Error: Kode barang '{kode}' sudah ada.")

        # Jika valid dan belum ada, tambahkan ke dictionary
        self._items[kode] = jumlah_int
        print(f"Sukses: Barang '{kode}' ditambahkan dengan stok {jumlah_int}.")

    def ambil_barang(self, kode, jumlah):
        # ambil_barang
        try:
            jumlah_int = int(jumlah)
            if jumlah_int <= 0:
                raise ValueError("Jumlah harus berupa integer positif.")
        except ValueError as e:
            # Menangkap ValueError untuk jumlah
            print(f"[Error Input Ambil] {e}")
            return

        try:
            stok_sekarang = self._items[kode]
        except KeyError:
            # Menangkap KeyError jika kode tidak ditemukan
            print(f"Error: Kode barang '{kode}' tidak ditemukan di inventaris.")
            return

        # Periksa apakah stok mencukupi
        if jumlah_int > stok_sekarang:
            # Bangkitkan ValueError jika stok kurang
            raise ValueError(f"Error: Stok barang '{kode}' tidak mencukupi (tersedia: {stok_sekarang}, diminta: {jumlah_int}).")

        # Jika lolos semua validasi, kurangi stok
        self._items[kode] -= jumlah_int
        print(f"Sukses: {jumlah_int} unit '{kode}' berhasil diambil. Sisa stok: {self._items[kode]}.")

    def cek_stok(self, kode):
        # cek_stok dengan try...except...else...finally
        print(f"--- Memeriksa stok untuk '{kode}' ---")
        try:
            stok = self._items[kode]
        except KeyError:
            print("Hasil: Barang tidak ditemukan di inventaris.")
        else:
            print(f"Hasil: Stok barang '{kode}' adalah {stok} unit.")
        finally:
            print(f"Pengecekan stok untuk kode '{kode}' telah selesai dilakukan.\n")


# Kode Utama
if __name__ == "__main__":
    inventaris = InventarisBarang()

    print("=== UJI COBA: TAMBAH BARANG ===")
    inventaris.tambah_barang("Kamera", 5)
    inventaris.tambah_barang("Printer", 6)
    inventaris.tambah_barang("Scanner", -4)     # Memicu except ValueError internal
    inventaris.tambah_barang("Mesin Fotokopi", "lima")  # Memicu except ValueError internal

    try:
        # Memicu KeyError karena Kamera sudah ada
        inventaris.tambah_barang("Kamera", 2)
    except KeyError as e:
        print(f"Main Error Catcher (KeyError): {e}")

    print("\n=== UJI COBA: AMBIL BARANG ===")
    inventaris.ambil_barang("Penggaris", 5)        # Memicu except KeyError internal (kode tidak ada)
    inventaris.ambil_barang("Kamera", "dua")    # Memicu except ValueError internal (jumlah invalid)
    inventaris.ambil_barang("Kamera", 3)       # Pengambilan sukses

    try:
        # Memicu ValueError yang di-raise karena stok tidak cukup
        inventaris.ambil_barang("Printer", 10)
    except ValueError as e:
        print(f"Main Error Catcher (ValueError): {e}")

    print("\n=== UJI COBA: CEK STOK ===")
    inventaris.cek_stok("Kamera") # Kode ada (memicu blok try -> else -> finally)
    inventaris.cek_stok("Joran") # Kode tidak ada (memicu blok try -> except -> finally)