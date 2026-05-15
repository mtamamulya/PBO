from abc import ABC, abstractmethod
import random

class AlatPembayaranAbstrak(ABC):
    def __init__(self, nama_metode):
        self.nama_metode = nama_metode
        print(f"Inisialisasi alat pembayaran: {self.nama_metode}")

    def info(self):
        print(f"Metode Pembayaran: {self.nama_metode}")

    @abstractmethod
    def proses_pembayaran(self, jumlah):
        pass

class KartuKredit(AlatPembayaranAbstrak):
    def __init__(self, nomor_kartu, nama_pemilik):
        super().__init__("Kartu Kredit")
        self.nomor_kartu = nomor_kartu[-4:]
        self.nama_pemilik = nama_pemilik
        print(f" -> Kartu Kredit ************{self.nomor_kartu} ({self.nama_pemilik}) siap.")

    def proses_pembayaran(self, jumlah):
        print(f" Memproses pembayaran Rp{jumlah} via Kartu ************{self.nomor_kartu}...")
        berhasil = random.choice([True, False])
        if berhasil:
            print(" Pembayaran Kartu Kredit Berhasil.")
            return True
        else:
            print(" Pembayaran Kartu Kredit Gagal (Limit tidak cukup/Error).")
            return False

class DompetDigital(AlatPembayaranAbstrak):
    def __init__(self, nomor_telepon, nama_provider):
        super().__init__(f"Dompet Digital ({nama_provider})")
        self.nomor_telepon = nomor_telepon
        self._saldo = random.randint(50000, 500000)
        print(f" -> Dompet Digital {self.nomor_telepon} siap (Saldo: Rp{self._saldo}).")

    def proses_pembayaran(self, jumlah):
        print(f" Memproses pembayaran Rp{jumlah} via Dompet Digital {self.nomor_telepon}...")
        if jumlah <= self._saldo:
            self._saldo -= jumlah
            print(" Pembayaran Dompet Digital Berhasil.")
            print(f" Saldo tersisa: Rp{self._saldo}")
            return True
        else:
            print(" Pembayaran Dompet Digital Gagal (Saldo tidak mencukupi).")
            return False

if __name__ == "__main__":
    kartu_bca = KartuKredit("1234-5678-9012-3456", "Budi Cahyono")
    gopay = DompetDigital("08123456789", "GoPay")
    
    kartu_bca.info()
    kartu_bca.proses_pembayaran(150000)
    
    gopay.info()
    gopay.proses_pembayaran(75000)