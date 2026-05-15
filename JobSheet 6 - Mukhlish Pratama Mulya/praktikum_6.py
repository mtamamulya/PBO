from abc import ABC, abstractmethod

class ElemenGrafis(ABC):
    def __init__(self, id_elemen, warna):
        print(f"[ElemenGrafis __init__] Membuat elemen dengan ID: {id_elemen}")
        self._id = id_elemen
        self.warna = warna

    @property
    def id_elemen(self):
        print(f"[ElemenGrafis id_elemen getter] Mengakses ID: {self._id}")
        return self._id

    @property
    @abstractmethod
    def posisi(self):
        pass

    @posisi.setter
    @abstractmethod
    def posisi(self, koordinat_baru):
        pass

    @abstractmethod
    def gambar(self):
        pass

    def info_warna(self):
        print(f"[ElemenGrafis info_warna] Warna elemen {self.id_elemen}: {self.warna}")

class Kotak(ElemenGrafis):
    def __init__(self, id_elemen, warna, x=0, y=0, lebar=10, tinggi=10):
        super().__init__(id_elemen, warna)
        print(f"[Kotak __init__] Menginisialisasi Kotak ID: {self.id_elemen}")
        self._x = x
        self._y = y
        self.lebar = lebar
        self.tinggi = tinggi

    @property
    def posisi(self):
        print(f"[Kotak posisi getter] Mengembalikan posisi Kotak {self.id_elemen}: ({self._x}, {self._y})")
        return (self._x, self._y)

    @posisi.setter
    def posisi(self, koordinat_baru):
        print(f"[Kotak posisi setter] Mencoba set posisi Kotak {self.id_elemen} ke {koordinat_baru}")
        if isinstance(koordinat_baru, tuple) and len(koordinat_baru) == 2:
            self._x = koordinat_baru[0]
            self._y = koordinat_baru[1]
            print(f" -> Posisi Kotak {self.id_elemen} berhasil diubah ke ({self._x}, {self._y})")
        else:
            print(" -> Gagal: Posisi harus berupa tuple (x, y).")

    def gambar(self):
        print(f"[Kotak gambar] Menggambar Kotak '{self.id_elemen}' warna {self.warna} di ({self._x}, {self._y}) dengan ukuran {self.lebar}x{self.tinggi}")

if __name__ == "__main__":
    print("Membuat objek Kotak...")
    kotak1 = Kotak("KotakA", "Merah", x=5, y=10, lebar=20)
    print("-" * 30)
    
    print("Mengakses ID...")
    id_ktk = kotak1.id_elemen
    print("-" * 30)
    
    print("Mengakses Posisi Awal...")
    pos_awal = kotak1.posisi
    print("-" * 30)
    
    print("Mengubah Posisi...")
    kotak1.posisi = (50, 60)
    
    print("Mengakses Posisi Baru...")
    pos_baru = kotak1.posisi
    print("-" * 30)
    
    print("Mencoba Set Posisi Salah...")
    kotak1.posisi = [100, 200] # Bukan tuple
    print("-" * 30)
    
    print("Menggambar Kotak...")
    kotak1.gambar()
    print("-" * 30)
    
    print("Info Warna...")
    kotak1.info_warna()
    print("-" * 30)