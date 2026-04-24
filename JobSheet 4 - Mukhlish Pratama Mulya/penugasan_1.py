class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim = nim
        self.ipk = ipk

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"IPK: {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            print("Predikat: Dengan Pujian")
        elif self.ipk >= 3.0:
            print("Predikat: Sangat Memuaskan")
        elif self.ipk >= 2.5:
            print("Predikat: Memuaskan")
        else:
            print("Predikat: Cukup")

class MahasiswaSarjana(Mahasiswa):
    def __init__(self, nama, nim, ipk, semester, sks_lulus):
        super().__init__(nama, nim, ipk)
        self.semester = semester
        self.sks_lulus = sks_lulus

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Semester: {self.semester}")
        print(f"SKS Lulus: {self.sks_lulus}")

class MahasiswaMagister(Mahasiswa):
    def __init__(self, nama, nim, ipk, judul_tesis, nama_pembimbing):
        super().__init__(nama, nim, ipk)
        self.judul_tesis = judul_tesis
        self.nama_pembimbing = nama_pembimbing

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Judul Tesis: {self.judul_tesis}")
        print(f"Pembimbing: {self.nama_pembimbing}")

if __name__ == "__main__":
    mhs_s1 = MahasiswaSarjana("Budi", "12345678", 3.85, 6, 120)
    print("--- Informasi Mahasiswa Sarjana ---")
    mhs_s1.tampilkan_info()
    mhs_s1.hitung_predikat()
    
    print("\n" + "="*30 + "\n")
    
    mhs_s2 = MahasiswaMagister("Ani", "87654321", 3.90, "Analisis Algoritma Berbasis AI", "Dr. Budi Santoso")
    print("--- Informasi Mahasiswa Magister ---")
    mhs_s2.tampilkan_info()
    mhs_s2.hitung_predikat()







