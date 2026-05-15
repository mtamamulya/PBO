from abc import ABC, abstractmethod

# 1. Definisikan Kelas Abstrak
class KendaraanAbstrak(ABC):
    def __init__(self, merk):
        self.merk = merk
        print(f"Inisialisasi KendaraanAbstrak dengan merk: {self.merk}")

    # Metode konkret (tidak abstrak)
    def info_merk(self):
        print(f"Merk kendaraan ini adalah {self.merk}.")

    # 2. Definisikan Metode Abstrak
    @abstractmethod
    def start_mesin(self):
        pass

    @abstractmethod
    def stop_mesin(self):
        pass

# Contoh definisi kelas anak (konkret)
class Mobil(KendaraanAbstrak):
    # Implementasi metode abstrak start_mesin
    def start_mesin(self):
        print(f"Mesin mobil {self.merk} dinyalakan.")

    # Implementasi metode abstrak stop_mesin
    def stop_mesin(self):
        print(f"Mesin mobil {self.merk} dimatikan.")

if __name__ == "__main__":
    print("Definisi Kelas Abstrak 'KendaraanAbstrak' selesai.")
    
    # Membuat objek dari kelas anak (konkret)
    mobil_contoh = Mobil("Toyota")
    
    # Memanggil metode
    mobil_contoh.start_mesin()
    mobil_contoh.info_merk()
    mobil_contoh.stop_mesin()