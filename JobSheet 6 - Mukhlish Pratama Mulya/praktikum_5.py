from abc import ABC, abstractmethod
import math

class BangunDatarAbstrak(ABC):
    def __init__(self, nama):
        self._nama = nama
        print(f"Inisialisasi BangunDatarAbstrak: {self._nama}")

    @property
    def nama(self):
        return self._nama

    def info_lengkap(self):
        print(f"\n--- Info Lengkap: {self.nama} ---")
        try:
            luas = self.hitung_luas()
            print(f" Luas     : {luas:.2f}")
        except Exception as e:
            print(f" Luas     : Error ({e})")
            
        try:
            keliling = self.hitung_keliling()
            print(f" Keliling : {keliling:.2f}")
        except Exception as e:
            print(f" Keliling : Error ({e})")
        print("-" * (len(self.nama) + 18))

    @abstractmethod
    def hitung_luas(self):
        pass

    @abstractmethod
    def hitung_keliling(self):
        pass

class Lingkaran(BangunDatarAbstrak):
    def __init__(self, radius):
        super().__init__("Lingkaran")
        if radius < 0:
            raise ValueError("Radius tidak boleh negatif")
        self.radius = radius
        print(f" -> Lingkaran dibuat (Radius: {self.radius})")

    def hitung_luas(self):
        return math.pi * (self.radius ** 2)

    def hitung_keliling(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    lingkaran_A = Lingkaran(10)
    print(f"\nNama bangun (via property): {lingkaran_A.nama}")
    lingkaran_A.info_lengkap()