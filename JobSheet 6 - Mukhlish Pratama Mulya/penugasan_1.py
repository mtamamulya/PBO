from abc import ABC, abstractmethod # [cite: 842]

# 1. Definisikan Kelas Abstrak (Senjata) [cite: 841]
class Senjata(ABC): # [cite: 843]
    def __init__(self, nama): # [cite: 844]
        self.nama = nama
        print(f"Inisialisasi Senjata: {self.nama}")

    # Metode Abstrak [cite: 845]
    @abstractmethod
    def serang(self): # [cite: 846]
        """Logika serangan spesifik untuk tiap jenis senjata."""
        pass

    # Properti Abstrak [cite: 847]
    @property
    @abstractmethod
    def kapasitas(self): # [cite: 848]
        """Getter abstrak untuk daya tahan atau amunisi."""
        pass

    # Metode Konkret (Opsional) [cite: 849]
    def info_nama(self):
        print(f"Nama Senjata: {self.nama}")

# 2. Kelas Anak Konkret 1 (Pedang) [cite: 850]
class Pedang(Senjata): # [cite: 851]
    def __init__(self, nama, panjang_bilah): # [cite: 853]
        super().__init__(nama) # [cite: 854]
        self.panjang_bilah = panjang_bilah # [cite: 852]
        self._daya_tahan = 100 # Atribut internal

    # Implementasi metode abstrak serang [cite: 855]
    def serang(self):
        print(f"Pedang {self.nama} menebas dengan bilah sepanjang {self.panjang_bilah} cm!")

    # Implementasi properti abstrak (daya_tahan) [cite: 857]
    @property
    def kapasitas(self):
        return self._daya_tahan

# 3. Kelas Anak Konkret 2 (Panah) [cite: 859]
class Panah(Senjata): # [cite: 860]
    def __init__(self, nama, jumlah_anak_panah): # [cite: 862]
        super().__init__(nama) # [cite: 863]
        self._jumlah_anak_panah = jumlah_anak_panah # [cite: 861]

    # Implementasi metode abstrak serang [cite: 864]
    def serang(self):
        if self._jumlah_anak_panah > 0: # [cite: 865]
            self._jumlah_anak_panah -= 1
            print(f"Panah {self.nama} melesat! Sisa anak panah: {self._jumlah_anak_panah}.") # [cite: 866]
        else:
            print(f"Amunisi Panah {self.nama} habis!") # [cite: 866]

    # Implementasi properti abstrak (ammo) [cite: 867]
    @property
    def kapasitas(self):
        return self._jumlah_anak_panah
    
    @kapasitas.setter # [cite: 868]
    def kapasitas(self, nilai_baru):
        self._jumlah_anak_panah = nilai_baru
        print(f"Amunisi {self.nama} diisi ulang menjadi: {self._jumlah_anak_panah}")

# 4. Kode Utama [cite: 869]
if __name__ == "__main__":
    # Mencoba instansiasi kelas abstrak (Opsional) [cite: 875]
    try:
        print("--- Mencoba membuat objek dari kelas abstrak Senjata ---")
        senjata_error = Senjata("Excalibur")
    except TypeError as e:
        print(f"GAGAL: {e}\n") # [cite: 876]

    # Buat objek dari kelas Pedang dan Panah [cite: 870]
    pedang_saya = Pedang("Katana", 75)
    panah_saya = Panah("Longbow", 2)
    print("-" * 40)

    # Panggil metode serang() pada objek Pedang [cite: 872]
    pedang_saya.serang()
    print(f"Daya tahan {pedang_saya.nama}: {pedang_saya.kapasitas}") # [cite: 873, 874]
    print("-" * 40)

    # Panggil metode serang() pada objek Panah beberapa kali [cite: 871]
    panah_saya.serang()
    panah_saya.serang()
    panah_saya.serang() # Mencoba menyerang saat amunisi habis
    
    # Akses properti amunisi [cite: 873, 874]
    print(f"Sisa amunisi {panah_saya.nama}: {panah_saya.kapasitas}")
    
    # Menggunakan setter untuk isi ulang
    panah_saya.kapasitas = 5
    print("-" * 40)