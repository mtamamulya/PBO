# 1. Definisikan Custom Exception (mewarisi dari Exception)
class KonfigurasiError(Exception):
    """Exception khusus untuk menandakan error terkait konfigurasi aplikasi."""
    def __init__(self, message, penyebab_asli=None):
        super().__init__(message)
        self.penyebab_asli = penyebab_asli # Menyimpan error asli jika ada

    def __str__(self):
        if self.penyebab_asli:
            return f"{super().__str__()} (Disebabkan oleh: {type(self.penyebab_asli).__name__})"
        return super().__str__()

# Kelas yang menggunakan exception handling gabungan
class PengelolaSetting:
    def __init__(self, file_config):
        self._config = {}
        self.file_config = file_config
        # Panggil metode internal yang berpotensi raise KonfigurasiError
        try:
            self.load_config()
            print(f"-> PengelolaSetting berhasil dibuat untuk '{self.file_config}'.")
        except KonfigurasiError as e:
            print(f"-> GAGAL membuat PengelolaSetting: {e}")
            # Bisa jadi kita ingin raise lagi agar pembuat objek tahu ada masalah serius
            # raise e

            # Atau set state default
            self._config = {}
            print("     -> Menggunakan konfigurasi default/kosong.")

    def load_config(self):
        """Metode internal untuk load config. Bisa raise KonfigurasiError."""
        print(f"\n [{self.file_config}] Mencoba load konfigurasi...")
        try:
            # --- Potensi FileNotFoundError ---
            print(f"     Membuka file '{self.file_config}' ...")
            # Simulasi: anggap hanya file 'config.txt' yang valid untuk dibaca
            if self.file_config != 'config.txt':
                # Jika file tidak ada, kita raise FileNotFoundError secara manual
                # (dalam aplikasi nyata, ini akan otomatis dari open())
                raise FileNotFoundError(f"File '{self.file_config}' tidak ada.")

            # --- Potensi Error Isi File (KeyError, ValueError) ---
            print(f"     Membaca dan validasi isi '{self.file_config}'...")

            # Simulasi data raw (bisa dari json.load(f), dll)
            # data_raw = {"host": "192.168.1.1", "port": "8080"} # Port benar
            data_raw = {"host": "192.168.1.1", "port": "xyz"}  # Port salah tipe
            # data_raw = {"host": "192.168.1.1"}               # Key 'port' hilang

            # Cek key 'port'
            port_str = data_raw['port'] # Bisa raise KeyError

            # Cek tipe 'port'
            port_int = int(port_str)    # Bisa raise ValueError

            # Jika lolos, simpan
            self._config['port'] = port_int
            self._config['host'] = data_raw.get('host', 'localhost')
            print("  -> Konfigurasi berhasil di-load dan divalidasi.")

        # --- Blok Except ---
        except FileNotFoundError as e_fnf:
            print(f"    ERROR Bawaan: File tidak ditemukan.")
            # Re-raise sebagai KonfigurasiError
            raise KonfigurasiError(f"File konfigurasi penting '{self.file_config}' hilang.", penyebab_asli=e_fnf) from e_fnf

        except KeyError as e_key:
            print(f"    ERROR Bawaan: Kunci konfigurasi hilang.")
            # Re-raise sebagai KonfigurasiError
            raise KonfigurasiError(f"Kunci '{e_key}' wajib ada dalam file konfigurasi.", penyebab_asli=e_key) from e_key

        except ValueError as e_val:
            print(f"    ERROR Bawaan: Nilai konfigurasi tidak valid.")
            # Re-raise sebagai KonfigurasiError
            raise KonfigurasiError(f"Nilai untuk 'port' ('{port_str}') harus integer.", penyebab_asli=e_val) from e_val

        except Exception as e_lain:
            print(f"    ERROR Bawaan Tak Terduga: {type(e_lain).__name__}")
            # Re-raise sebagai KonfigurasiError umum
            raise KonfigurasiError(f"Terjadi error tak terduga saat konfigurasi.", penyebab_asli=e_lain) from e_lain

    def get_setting(self, key, default=None):
        """Mendapatkan nilai setting."""
        # print(f"Mendapatkan setting '{key}'...")
        return self._config.get(key, default)

# --- Kode Utama ---
if __name__ == "__main__":
    # Skenario 1: File tidak ada -> Menghasilkan KonfigurasiError
    print("\n--- Skenario 1: File Salah ---")
    # Error sudah ditangani di dalam __init__ berdasarkan contoh ini
    settings1 = PengelolaSetting("setting.cfg")
    # Jika error di-raise ulang oleh init, kode di bawah tidak jalan
    print(f"Port dari settings1: {settings1.get_setting('port', 'Belum terload')}")

    # Skenario 2: File ada, tapi data port salah -> Menghasilkan KonfigurasiError
    print("\n--- Skenario 2: Data Port Salah ---")
    # (Anggap 'config.txt' ada tapi isinya menyebabkan ValueError di load_config)
    settings2 = PengelolaSetting("config.txt")
    print(f"Port dari settings2: {settings2.get_setting('port', 'Belum terload')}")

    # Skenario 3: (Jika simulasi di load_config diubah jadi benar)
    print("\n--- Skenario 3: Sukses ---")
    # Catatan: Untuk skenario 3 berhasil sepenuhnya, kamu harus meng-uncomment
    # baris 45 (data_raw port benar) dan me-comment baris 46 di dalam method load_config
    settings3 = PengelolaSetting("config.txt")
    print(f"Port dari settings3: {settings3.get_setting('port')}")
    print(f"Host dari settings3: {settings3.get_setting('host')}")