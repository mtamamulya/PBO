# konfigurasi.py
import os

# Menentukan direktori utama proyek
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NAMA_DB = 'pengeluaran_harian.db'
DB_PATH = os.path.join(BASE_DIR, NAMA_DB)

# Daftar kategori pengeluaran
KATEGORI_PENGELUARAN = ["Makanan", "Transportasi", "Hiburan", "Tagihan", "Belanja", "Kesehatan", "Pendidikan", "Lainnya"]
KATEGORI_DEFAULT = "Lainnya"