import pandas as pd
import folium
import datetime
from abc import ABC, abstractmethod

class Lokasi(ABC):
    def __init__(self, nama: str, latitude: float, longitude: float):
        self.nama = str(nama) if nama else "Tanpa Nama"
        try:
            self.latitude = float(latitude)
            self.longitude = float(longitude)
        except (ValueError, TypeError):
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
    """Tempat wisata alam, sejarah, atau budaya."""

    def __init__(self, nama, latitude, longitude, jenis, deskripsi):
        super().__init__(nama, latitude, longitude)
        self.jenis_wisata = str(jenis) if jenis else "Umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Tidak ada deskripsi."

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>{self.jenis_wisata}</i><br><br>"
                f"{self.deskripsi}<br><br>"
                f"<small>Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})</small>")

class Kuliner(Lokasi):

    def __init__(self, nama, latitude, longitude, menu_andalan):
        super().__init__(nama, latitude, longitude)
        self.menu_andalan = str(menu_andalan) if menu_andalan else "Tidak diketahui"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>🍽️ Kuliner</i><br><br>"
                f"Menu Andalan: {self.menu_andalan}<br><br>"
                f"<small>Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})</small>")

class TempatIbadah(Lokasi):

    def __init__(self, nama, latitude, longitude, agama="Umum", deskripsi=""):
        super().__init__(nama, latitude, longitude)
        self.agama = str(agama) if agama else "Umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Tempat Ibadah"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>🕌 Tempat Ibadah ({self.agama})</i><br><br>"
                f"{self.deskripsi}<br><br>"
                f"<small>Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})</small>")

class Museum(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float,
                 koleksi_utama: str = "", deskripsi: str = ""):
        super().__init__(nama, latitude, longitude)
        self.koleksi_utama = str(koleksi_utama) if koleksi_utama else "Beragam koleksi"
        self.deskripsi = str(deskripsi) if deskripsi else "Museum"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>🏛️ Museum</i><br><br>"
                f"{self.deskripsi}<br><br>"
                f"Koleksi Utama: {self.koleksi_utama}<br>"
                f"<small>Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})</small>")


class TamanKota(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float,
                 fasilitas: str = "", deskripsi: str = ""):
        super().__init__(nama, latitude, longitude)
        self.fasilitas = str(fasilitas) if fasilitas else "Taman umum"
        self.deskripsi = str(deskripsi) if deskripsi else "Taman Kota"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>🌳 Taman Kota</i><br><br>"
                f"{self.deskripsi}<br><br>"
                f"Fasilitas: {self.fasilitas}<br>"
                f"<small>Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})</small>")


class KantorPemerintahan(Lokasi):
    def __init__(self, nama: str, latitude: float, longitude: float,
                 instansi: str = "", deskripsi: str = ""):
        super().__init__(nama, latitude, longitude)
        self.instansi = str(instansi) if instansi else "Pemerintahan"
        self.deskripsi = str(deskripsi) if deskripsi else "Kantor Pemerintahan"

    def get_info_popup(self) -> str:
        return (f"<h4><b>{self.nama}</b></h4>"
                f"<i>🏢 Kantor Pemerintahan</i><br><br>"
                f"Instansi: {self.instansi}<br><br>"
                f"{self.deskripsi}<br>"
                f"<small>Koordinat: ({self.latitude:.4f}, {self.longitude:.4f})</small>")

def tulis_log(pesan: str, file_log: str = "proses_peta.log"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(file_log, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] {pesan}\n")
    except IOError as e:
        print(f"ERROR: Gagal menulis ke file log '{file_log}': {e}")


def baca_data_lokasi(nama_file: str):
    try:
        dataframe = pd.read_csv(nama_file)
        print(f"  -> File '{nama_file}' berhasil dibaca ({len(dataframe)} baris).")
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
        print("DataFrame kosong atau None, tidak ada objek dibuat.")
        return list_objek_lokasi

    print("\nMembuat objek dari DataFrame...")
    for index, row in dataframe.iterrows():
        nama = row.get('Nama', None)
        lat = row.get('Latitude', None)
        lon = row.get('Longitude', None)
        tipe = str(row.get('Tipe', 'Lainnya'))
        deskripsi = row.get('Deskripsi', '')
        objek = None

        if nama is None or lat is None or lon is None:
            print(f"  -> Melewati baris {index}: Data tidak lengkap.")
            continue

        try:
            if 'Wisata' in tipe or tipe == 'Landmark':
                objek = TempatWisata(nama, lat, lon, tipe, deskripsi)

            # Kuliner
            elif tipe == 'Kuliner':
                objek = Kuliner(nama, lat, lon, deskripsi)

            # TempatIbadah
            elif 'Ibadah' in tipe:
                agama_info = "Umum"
                if "Masjid" in str(nama):
                    agama_info = "Islam"
                elif "Gereja" in str(nama):
                    agama_info = "Kristen"
                elif "Klenteng" in str(nama):
                    agama_info = "Tridharma"
                objek = TempatIbadah(nama, lat, lon, agama_info, deskripsi)

            # Museum (KELAS BARU)
            elif tipe == 'Museum':
                objek = Museum(nama, lat, lon,
                               koleksi_utama="Sejarah & Budaya Jawa Tengah",
                               deskripsi=deskripsi)

            # TamanKota (KELAS BARU)
            elif tipe == 'Taman Kota':
                objek = TamanKota(nama, lat, lon,
                                  fasilitas="Area bermain, jogging track, tempat duduk",
                                  deskripsi=deskripsi)

            # KantorPemerintahan (KELAS BARU)
            elif tipe == 'Kantor Pemerintahan':
                objek = KantorPemerintahan(nama, lat, lon,
                                           instansi=nama,
                                           deskripsi=deskripsi)

            else:
                print(f"  -> Peringatan: Tipe '{tipe}' untuk '{nama}' tidak dikenali.")

            if objek:
                list_objek_lokasi.append(objek)

        except Exception as e:
            print(f"  -> GAGAL membuat objek untuk '{nama}' di baris {index}: {e}")

    print(f"Total {len(list_objek_lokasi)} objek lokasi berhasil dibuat.")
    return list_objek_lokasi

def baca_konfigurasi_peta(file_config: str = "config_peta.txt") -> tuple:

    lat_default, lon_default, zoom_default = -6.9929, 110.4200, 13

    try:
        with open(file_config, 'r', encoding='utf-8') as f:
            baris = f.readlines()

        lat = float(baris[0].strip())
        lon = float(baris[1].strip())
        zoom = int(baris[2].strip())

        print(f"  -> Konfigurasi peta dibaca dari '{file_config}': "
              f"lat={lat}, lon={lon}, zoom={zoom}")
        return lat, lon, zoom

    except FileNotFoundError:
        print(f"  -> Peringatan: '{file_config}' tidak ditemukan. Menggunakan default.")
        return lat_default, lon_default, zoom_default
    except (ValueError, IndexError) as e:
        print(f"  -> Peringatan: Error membaca konfigurasi ({e}). Menggunakan default.")
        return lat_default, lon_default, zoom_default

def dapatkan_style_marker(lok: Lokasi) -> dict:

    if isinstance(lok, Museum):
        return {'color': 'purple', 'icon': 'university', 'prefix': 'fa'}
    elif isinstance(lok, TamanKota):
        return {'color': 'green', 'icon': 'tree', 'prefix': 'fa'}
    elif isinstance(lok, KantorPemerintahan):
        return {'color': 'gray', 'icon': 'building', 'prefix': 'fa'}
    elif isinstance(lok, TempatWisata):
        return {'color': 'blue', 'icon': 'camera', 'prefix': 'fa'}
    elif isinstance(lok, Kuliner):
        return {'color': 'red', 'icon': 'cutlery', 'prefix': 'fa'}
    elif isinstance(lok, TempatIbadah):
        return {'color': 'orange', 'icon': 'star', 'prefix': 'fa'}
    else:
        return {'color': 'black', 'icon': 'info-sign', 'prefix': 'glyphicon'}


def buat_peta_lokasi_folium(list_objek: list,
                             file_output: str = "peta_mini_project.html",
                             file_config: str = "config_peta.txt",
                             file_log: str = "proses_peta.log"):
    nama_fungsi = "buat_peta_lokasi_folium"

    if not list_objek:
        pesan = f"[{nama_fungsi}] Gagal: Tidak ada data lokasi untuk dipetakan."
        print(pesan)
        tulis_log(pesan, file_log)
        return

    print(f"\n[{nama_fungsi}] Memulai pembuatan peta dari {len(list_objek)} lokasi...")
    tulis_log(f"[{nama_fungsi}] Memulai pembuatan peta '{file_output}' "
              f"dengan {len(list_objek)} lokasi.", file_log)

    # Baca konfigurasi dari file (Penugasan c)
    lat_tengah, lon_tengah, zoom_level = baca_konfigurasi_peta(file_config)

    # Buat objek peta Folium
    peta = folium.Map(location=[lat_tengah, lon_tengah],
                      zoom_start=zoom_level,
                      tiles="OpenStreetMap")

    # Tambahkan legenda warna sebagai HTML sederhana
    legenda_html = """
    <div style="position: fixed; bottom: 30px; left: 30px; z-index: 1000;
                background-color: white; padding: 15px; border-radius: 8px;
                border: 2px solid #ccc; font-size: 13px; line-height: 1.8;">
        <b>Legenda Peta</b><br>
        <span style="color:#3388ff;">&#9679;</span> Tempat Wisata<br>
        <span style="color:#d9534f;">&#9679;</span> Kuliner<br>
        <span style="color:#f0ad4e;">&#9679;</span> Tempat Ibadah<br>
        <span style="color:#8e44ad;">&#9679;</span> Museum<br>
        <span style="color:#5cb85c;">&#9679;</span> Taman Kota<br>
        <span style="color:#777;">&#9679;</span> Kantor Pemerintahan<br>
    </div>
    """
    peta.get_root().html.add_child(folium.Element(legenda_html))

    # Tambahkan marker dengan ikon berbeda per tipe (Penugasan b)
    jumlah_marker = 0
    lokasi_dilewati = []

    for lok in list_objek:
        koordinat = lok.get_koordinat()

        if koordinat != (0.0, 0.0):
            info_popup = lok.get_info_popup()
            style = dapatkan_style_marker(lok)  # Gunakan isinstance()

            folium.Marker(
                location=koordinat,
                popup=folium.Popup(info_popup, max_width=320),
                tooltip=f"{lok.nama} ({type(lok).__name__})",
                icon=folium.Icon(
                    color=style['color'],
                    icon=style['icon'],
                    prefix=style['prefix']
                )
            ).add_to(peta)
            jumlah_marker += 1
        else:
            lokasi_dilewati.append(lok.nama)

    if lokasi_dilewati:
        pesan_lewat = (f"[{nama_fungsi}] Melewati marker untuk: "
                       f"{', '.join(lokasi_dilewati)} (koordinat tidak valid).")
        print(f"  -> Peringatan: {pesan_lewat}")
        tulis_log(pesan_lewat, file_log)

    # Simpan peta dan log
    try:
        peta.save(file_output)
        pesan_sukses = (f"[{nama_fungsi}] Peta '{file_output}' berhasil dibuat "
                        f"dengan {jumlah_marker} marker.")
        print(f"-> {pesan_sukses}")
        tulis_log(pesan_sukses, file_log)
    except Exception as e:
        pesan_error = (f"[{nama_fungsi}] ERROR saat menyimpan peta: "
                       f"{type(e).__name__} - {e}")
        print(f"-> {pesan_error}")
        tulis_log(pesan_error, file_log)

if __name__ == "__main__":
    NAMA_FILE_CSV = "lokasi_semarang_extended.csv"
    NAMA_FILE_PETA = "peta_mini_project_semarang.html"
    FILE_CONFIG = "config_peta.txt"
    FILE_LOG = "proses_peta.log"

    print("=" * 60)
    print("  MINI PROJECT SIG - SISTEM INFORMASI GEOGRAFIS SEMARANG")
    print("  Jobsheet 12 - Mukhlish Pratama Mulya")
    print("=" * 60)

    # 1. Baca data CSV (termasuk lokasi baru)
    print("\n[LANGKAH 1] Membaca data CSV...")
    df_lokasi = baca_data_lokasi(NAMA_FILE_CSV)

    # 2. Buat list objek dari DataFrame (semua tipe termasuk kelas baru)
    print("\n[LANGKAH 2] Membuat objek dari data...")
    list_semua_lokasi = buat_objek_lokasi_dari_df(df_lokasi)

    # 3. Tampilkan ringkasan objek
    print("\n[LANGKAH 3] Ringkasan objek yang dibuat:")
    tipe_count = {}
    for lok in list_semua_lokasi:
        tipe = type(lok).__name__
        tipe_count[tipe] = tipe_count.get(tipe, 0) + 1
    for tipe, count in tipe_count.items():
        print(f"  - {tipe}: {count} lokasi")

    # 4. Buat peta dengan konfigurasi dari file, marker berbeda, dan logging
    print("\n[LANGKAH 4] Membuat peta interaktif...")
    buat_peta_lokasi_folium(
        list_semua_lokasi,
        file_output=NAMA_FILE_PETA,
        file_config=FILE_CONFIG,
        file_log=FILE_LOG
    )

    print(f"\n{'=' * 60}")
    print(f"  Peta disimpan: {NAMA_FILE_PETA}")
    print(f"  Log disimpan : {FILE_LOG}")
    print(f"  Buka file HTML di browser untuk melihat hasil peta.")
    print(f"{'=' * 60}")
    print("\nMini Project SIG Selesai!")
