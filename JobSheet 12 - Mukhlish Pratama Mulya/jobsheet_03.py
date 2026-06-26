from abc import ABC, abstractmethod

class Lokasi(ABC):
    def __init__(self, nama: str, latitude: float, longitude: float):
        self.nama = str(nama) if nama else "Tanpa Nama"
        try:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
        except (ValueError, TypeError):
            print(f"  -> Peringatan: Koordinat tidak valid untuk '{self.nama}'. Set ke (0.0, 0.0).")
            self.latitude = 0.0
            self.longitude = 0.0

    def get_koordinat(self) -> tuple:
        return (self.latitude, self.longitude)

    @abstractmethod
    def get_info_popup(self) -> str:
        pass

    def __repr__(self) -> str:
        return (f"{type(self).__name__}(nama='{self.nama}', "
                f"lat={self.latitude:.4f}, lon={self.longitude:.4f})")

    def __str__(self) -> str:
        return f"{self.nama} [{type(self).__name__}]"
    
class TempatWisata(Lokasi):

    def __init__(self, nama: str, latitude: float, longitude: float,
                 jenis: str, deskripsi: str):
        
        super().__init__(nama, latitude, longitude)
        self.jenis_wisata = str(jenis) if jenis else "Umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Tidak ada deskripsi."

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>{self.jenis_wisata}</i><br><br>"
                f"{self.deskripsi}<br><br>"
                f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})")

class Kuliner(Lokasi):

    def __init__(self, nama: str, latitude: float, longitude: float,
                 menu_andalan: str):
        
        super().__init__(nama, latitude, longitude)
        self.menu_andalan = str(menu_andalan) if menu_andalan else "Tidak diketahui"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>Kuliner</i><br><br>"
                f"Menu Andalan: {self.menu_andalan}<br><br>"
                f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})")

class TempatIbadah(Lokasi):

    def __init__(self, nama: str, latitude: float, longitude: float,
                 agama: str = "Umum", deskripsi: str = ""):
        
        super().__init__(nama, latitude, longitude)
        self.agama = str(agama) if agama else "Umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Tempat Ibadah"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>Tempat Ibadah ({self.agama})</i><br><br>"
                f"{self.deskripsi}<br><br>"
                f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})")

if __name__ == "__main__":
    print("--- Memulai Praktikum 3: Mendesain Kelas OOP ---")

    print("\n1. Membuat objek TempatWisata:")
    wisata1 = TempatWisata(
        "Lawang Sewu", -6.9840, 110.4105,
        "Wisata Sejarah",
        "Bangunan bersejarah peninggalan Belanda dengan banyak pintu."
    )
    print(f"   repr: {repr(wisata1)}")
    print(f"   str : {str(wisata1)}")
    print(f"   Koordinat: {wisata1.get_koordinat()}")
    print(f"   Popup HTML:\n   {wisata1.get_info_popup()}")

    print("\n2. Membuat objek Kuliner:")
    kuliner1 = Kuliner(
        "Toko Oen", -6.9715, 110.4235,
        "Restoran dan toko es krim legendaris sejak zaman kolonial."
    )
    print(f"   repr: {repr(kuliner1)}")
    print(f"   str : {str(kuliner1)}")
    print(f"   Popup HTML:\n   {kuliner1.get_info_popup()}")

    print("\n3. Membuat objek TempatIbadah:")
    ibadah1 = TempatIbadah(
        "Masjid Agung Jawa Tengah", -6.9892, 110.4452,
        "Islam",
        "Masjid besar dengan arsitektur megah dan menara pandang Asmaul Husna."
    )
    print(f"   repr: {repr(ibadah1)}")
    print(f"   str : {str(ibadah1)}")
    print(f"   Popup HTML:\n   {ibadah1.get_info_popup()}")

    print("\n4. Demonstrasi Polimorfisme:")
    daftar_lokasi = [wisata1, kuliner1, ibadah1]
    for lok in daftar_lokasi:
        print(f"   - {str(lok)} | Koordinat: {lok.get_koordinat()}")

    print("\n5. Mencoba membuat objek Lokasi (abstrak):")
    try:
        lok_abstrak = Lokasi("Test", 0.0, 0.0)
    except TypeError as e:
        print(f"   -> Berhasil dicegah! Error: {e}")

    print("\n--- Praktikum 3 Selesai ---")
