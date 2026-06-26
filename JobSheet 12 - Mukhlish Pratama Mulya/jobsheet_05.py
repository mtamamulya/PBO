import pandas as pd
import folium
from abc import ABC, abstractmethod

class Lokasi(ABC):
    def __init__(self, nama: str, latitude: float, longitude: float):
        self.nama = str(nama) if nama else "Tanpa Nama"
        try:
            self.latitude, self.longitude = float(latitude), float(longitude)
        except ValueError:
            self.latitude, self.longitude = 0.0, 0.0

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
    def __init__(self, nama, latitude, longitude, jenis, deskripsi):
        super().__init__(nama, latitude, longitude)
        self.jenis_wisata = str(jenis) if jenis else "Umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Tidak ada deskripsi."

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>{self.jenis_wisata}</i><br><br>"
                f"{self.deskripsi}<br><br>"
                f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})")


class Kuliner(Lokasi):
    def __init__(self, nama, latitude, longitude, menu_andalan):
        super().__init__(nama, latitude, longitude)
        self.menu_andalan = str(menu_andalan) if menu_andalan else "Tidak diketahui"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>Kuliner</i><br><br>"
                f"Menu Andalan: {self.menu_andalan}<br><br>"
                f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})")


class TempatIbadah(Lokasi):
    def __init__(self, nama, latitude, longitude, agama="Umum", deskripsi=""):
        super().__init__(nama, latitude, longitude)
        self.agama = str(agama) if agama else "Umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Tempat Ibadah"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>Tempat Ibadah ({self.agama})</i><br><br>"
                f"{self.deskripsi}<br><br>"
                f"Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})")

def baca_data_lokasi(nama_file: str):
    try:
        dataframe = pd.read_csv(nama_file)
        return dataframe
    except FileNotFoundError:
        print(f"ERROR: File '{nama_file}' tidak ditemukan!")
        return None
    except Exception as e:
        print(f"ERROR saat membaca file CSV: {type(e).__name__} - {e}")
        return None


def buat_objek_lokasi_dari_df(dataframe: pd.DataFrame) -> list:
    list_objek_lokasi = []
    if dataframe is None or dataframe.empty:
        return list_objek_lokasi

    for index, row in dataframe.iterrows():
        nama = row.get('Nama', None)
        lat = row.get('Latitude', None)
        lon = row.get('Longitude', None)
        tipe = row.get('Tipe', 'Lainnya')
        deskripsi = row.get('Deskripsi', '')
        objek = None

        if nama is None or lat is None or lon is None:
            continue

        try:
            if 'Wisata' in str(tipe) or tipe == 'Landmark':
                objek = TempatWisata(nama, lat, lon, tipe, deskripsi)
            elif tipe == 'Kuliner':
                objek = Kuliner(nama, lat, lon, deskripsi)
            elif 'Ibadah' in str(tipe):
                agama_info = "Umum"
                if "Masjid" in str(nama):
                    agama_info = "Islam"
                elif "Klenteng" in str(nama):
                    agama_info = "Tridharma"
                objek = TempatIbadah(nama, lat, lon, agama_info, deskripsi)

            if objek:
                list_objek_lokasi.append(objek)
        except Exception as e:
            print(f"  -> GAGAL membuat objek untuk '{nama}' di baris {index}: {e}")

    return list_objek_lokasi

def buat_peta_lokasi_folium(list_objek: list, file_output: str = "peta_lokasi.html"):
    if not list_objek:
        print("Tidak ada objek lokasi untuk dipetakan.")
        return

    print(f"\nMemulai pembuatan peta Folium dari {len(list_objek)} lokasi...")

    try:
        lat_tengah = list_objek[0].latitude
        lon_tengah = list_objek[0].longitude
    except IndexError:
        lat_tengah, lon_tengah = -6.9929, 110.4200  # Default Semarang

    peta = folium.Map(location=[lat_tengah, lon_tengah], zoom_start=13,
                      tiles="OpenStreetMap")
    print(f"  -> Objek peta dibuat, berpusat di ({lat_tengah:.4f}, {lon_tengah:.4f})")

    jumlah_marker_valid = 0
    for lok in list_objek:
        koordinat = lok.get_koordinat()

        if koordinat != (0.0, 0.0):
            info_popup_html = lok.get_info_popup()

            folium.Marker(
                location=koordinat,                              # Koordinat marker
                popup=folium.Popup(info_popup_html, max_width=300),  # Konten popup saat diklik
                tooltip=lok.nama                                 # Teks saat hover
            ).add_to(peta)
            jumlah_marker_valid += 1
        else:
            print(f"  -> Melewati marker untuk '{lok.nama}' karena koordinat tidak valid.")

    try:
        peta.save(file_output)
        print(f"\n-> Peta berhasil dibuat dan disimpan sebagai '{file_output}'.")
        print(f"   Total marker ditambahkan: {jumlah_marker_valid}")
    except Exception as e:
        print(f"\nERROR saat menyimpan peta Folium: {type(e).__name__} - {e}")

if __name__ == "__main__":
    NAMA_FILE_CSV = "lokasi_semarang.csv"
    NAMA_FILE_PETA = "peta_interaktif_semarang.html"

    print("--- Memulai Praktikum 5: Visualisasi Peta dengan Folium ---")

    df_lokasi = baca_data_lokasi(NAMA_FILE_CSV)

    list_semua_lokasi = buat_objek_lokasi_dari_df(df_lokasi)

    buat_peta_lokasi_folium(list_semua_lokasi, NAMA_FILE_PETA)

    print(f"\nSilakan buka file '{NAMA_FILE_PETA}' di browser Anda untuk melihat hasilnya.")
    print("\n--- Praktikum 5 Selesai ---")
