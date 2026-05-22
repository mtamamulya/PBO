import os  # Diperlukan untuk menghapus file dummy nanti

class FileProcessor:
    def __init__(self, nama_file):
        self.nama_file = nama_file
        self.file_handle = None  # Untuk menyimpan objek file saat dibuka
        print(f"\n-> FileProcessor dibuat untuk file: '{self.nama_file}'")

    def baca_dan_proses(self):
        """Membuka, membaca, dan 'memproses' file, dengan cleanup di finally."""
        print(f"[{self.nama_file}] Mencoba memproses...")
        try:
            # 1. Mencoba membuka file untuk dibaca
            print(f"  [{self.nama_file}] Membuka file...")
            self.file_handle = open(self.nama_file, 'r', encoding='utf-8')  # Mode 'r' untuk baca

            # 2. Jika buka berhasil, coba baca isinya
            print(f"  [{self.nama_file}] Membaca isi file...")
            isi = self.file_handle.read()
            print("  -> File berhasil dibaca.")

            # 3. Simulasi pemrosesan isi
            print(f"  [{self.nama_file}] Memproses isi...")
            panjang_isi = len(isi)
            print(f"  -> Panjang isi: {panjang_isi} karakter.")
            # Simulasi: Anggap pemrosesan selalu berhasil jika baca berhasil

        except FileNotFoundError:
            # 4a. Blok ini jalan jika open() gagal karena file tidak ada
            print(f"  -> ERROR: File '{self.nama_file}' tidak ditemukan.")
        except UnicodeDecodeError:
            # 4b. Contoh error lain saat membaca file non-teks
            print(f"  -> ERROR: Gagal membaca '{self.nama_file}' sebagai teks (mungkin file biner?).")
        except Exception as e:
            # 4c. Menangkap error tak terduga lainnya saat try
            print(f"  -> ERROR Lainnya saat memproses file: {type(e).__name__} - {e}")
        else:
            # 5. Blok ini jalan HANYA JIKA try selesai tanpa exception
            print(f"  -> PEMROSESAN BERHASIL: Tidak ada error terjadi pada '{self.nama_file}'.")
        finally:
            # 6. Blok ini SELALU jalan setelah try/except/else selesai
            print(f"  [{self.nama_file}] Blok Finally: Melakukan cleanup...")
            if self.file_handle and not self.file_handle.closed:
                print(f"    Menutup file '{self.nama_file}'...")
                self.file_handle.close()
                print("    -> File berhasil ditutup.")
            else:
                # Ini akan terjadi jika file gagal dibuka (FileNotFoundError)
                # atau jika sudah ditutup karena error lain di try
                print("    -> File tidak perlu ditutup (belum dibuka atau sudah ditutup).")

        print(f"[{self.nama_file}] Selesai mencoba proses.")
        print("-" * 30)


# --- Kode Utama ---
if __name__ == "__main__":
    NAMA_FILE_SUKSES = "data_penting.txt"
    NAMA_FILE_GAGAL = "file_yang_tidak_ada.log"

    # Membuat file dummy untuk skenario sukses
    try:
        with open(NAMA_FILE_SUKSES, "w", encoding='utf-8') as f:
            f.write("Ini adalah baris pertama.\n")
            f.write("Baris kedua berisi data penting.\n")
        print(f"File dummy '{NAMA_FILE_SUKSES}' berhasil dibuat.")
    except IOError as e:
        print(f"Gagal membuat file dummy '{NAMA_FILE_SUKSES}': {e}")

    # Skenario 1: File ada dan proses berhasil
    print("\n--- Skenario 1: Proses Sukses ---")
    processor1 = FileProcessor(NAMA_FILE_SUKSES)
    processor1.baca_dan_proses()

    # Skenario 2: File tidak ada
    print("\n--- Skenario 2: File Tidak Ditemukan ---")
    processor2 = FileProcessor(NAMA_FILE_GAGAL)
    processor2.baca_dan_proses()

    # Cleanup file dummy
    try:
        if os.path.exists(NAMA_FILE_SUKSES):
            os.remove(NAMA_FILE_SUKSES)
            print(f"\nFile dummy '{NAMA_FILE_SUKSES}' dihapus.")
    except OSError as e:
        print(f"\nGagal menghapus file dummy '{NAMA_FILE_SUKSES}': {e}")