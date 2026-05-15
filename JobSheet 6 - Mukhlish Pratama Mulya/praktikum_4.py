from abc import ABC, abstractmethod
import time

class DokumenAbstrak(ABC):
    def __init__(self, nama_file):
        self.nama_file = nama_file
        print(f"Inisialisasi Dokumen: {self.nama_file}")
    
    def info_file(self):
        print(f"Nama File: {self.nama_file}")

    @abstractmethod
    def cetak(self):
        pass

    @abstractmethod
    def simpan(self):
        pass

class DokumenTeks(DokumenAbstrak):
    def __init__(self, nama_file, isi_teks):
        super().__init__(nama_file)
        self.isi_teks = isi_teks
        print(" -> Tipe: Dokumen Teks")

    def cetak(self):
        print(f"Mencetak Dokumen Teks '{self.nama_file}':")
        print("="*15)
        print(self.isi_teks)
        print("="*15)

    def simpan(self):
        print(f"Menyimpan Dokumen Teks '{self.nama_file}' ke disk...")
        time.sleep(0.2)
        print(" -> Berhasil disimpan.")

class Spreadsheet(DokumenAbstrak):
    def __init__(self, nama_file, baris, kolom):
        super().__init__(nama_file)
        self.baris = baris
        self.kolom = kolom
        print(" -> Tipe: Spreadsheet")

    def cetak(self):
        print(f"Mencetak Spreadsheet '{self.nama_file}' ({self.baris} baris x {self.kolom} kolom)...")

    def simpan(self):
        print(f"Menyimpan Spreadsheet '{self.nama_file}' ke format .xlsx...")
        time.sleep(0.3)
        print(" -> Berhasil disimpan.")

def proses_dokumen(daftar_dokumen):
    print("\n======= MEMPROSES SEMUA DOKUMEN =======")
    for doc in daftar_dokumen:
        print(f"\n--- Memproses {type(doc).__name__}: {doc.nama_file} ---")
        doc.cetak()
        doc.simpan()

if __name__ == "__main__":
    dok1 = DokumenTeks("laporan.txt", "Ini adalah isi laporan singkat.")
    dok2 = Spreadsheet("data_penjualan.xlsx", 200, 15)
    dok3 = DokumenTeks("catatan_rapat.txt", "Poin penting:\n- Bahas budget\n- Tentukan timeline")
    
    koleksi_dokumen = [dok1, dok2, dok3]
    proses_dokumen(koleksi_dokumen)