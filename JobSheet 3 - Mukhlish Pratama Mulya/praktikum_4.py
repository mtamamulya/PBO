class FileLogger:
    def __init__(self, filename):
        """
        Konstruktor: Membuka file log untuk menulis pesan.
        Parameter:
            - filename: Nama file tempat pesan log akan ditulis.
        """
        self.filename = filename
        try:
            # Membuka file dalam mode 'a' (append) agar pesan baru ditambahkan di akhir
            self.file = open(filename, "a")
            print(f"File '{filename}' berhasil dibuka untuk logging.")
        except Exception as e:
            print(f"Gagal membuka file '{filename}': {e}")

    def write_log(self, message):
        """
        Menulis pesan log ke dalam file.
        Parameter:
            - message: Pesan yang akan ditulis ke file.
        """
        self.file.write(message + "\n")
        self.file.flush()  # Memastikan pesan langsung ditulis ke disk (tidak tertahan di buffer)
        print(f"Pesan log: '{message}' telah ditulis.")

    def __del__(self):
        """
        Destruktor: Menutup file log ketika objek dihapus dari memori.
        """
        if hasattr(self, "file") and not self.file.closed:
            self.file.close()
            print(f"File '{self.filename}' telah ditutup.")

# Contoh penggunaan dalam skenario nyata aplikasi
if __name__ == "__main__":
    # Membuat objek logger untuk file "application.log"
    logger = FileLogger("application.log")

    # Menulis beberapa pesan log selama operasi aplikasi
    logger.write_log("Aplikasi dimulai.")
    logger.write_log("Melakukan operasi A...")
    logger.write_log("Operasi A selesai.")
    logger.write_log("Aplikasi akan segera selesai.")

    # Menghapus objek logger secara eksplisit untuk memicu destruktor
    del logger

    # Catatan: Jika tidak dihapus secara eksplisit, destruktor akan otomatis 
    # dipanggil oleh Garbage Collector saat program berakhir.