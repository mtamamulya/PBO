# Kelas Induk
class Person:
    def __init__(self, nama, usia):
        print(f"(Memanggil __init__ Person untuk '{nama}')")
        self.nama = nama
        self.usia = usia

    def perkenalkan_diri(self):
        print(f"Halo, nama saya {self.nama}, usia saya {self.usia} tahun.")

# Kelas Anak (mewarisi dari Person)
class Student(Person):
    def __init__(self, nama, usia, student_id, jurusan):
        print(f"(Memanggil __init__ Student untuk '{nama}')")
        # Memanggil __init__ dari kelas Person
        super().__init__(nama, usia)
        self.student_id = student_id
        self.jurusan = jurusan
        print(f"(Inisialisasi atribut Student selesai untuk '{nama}')")

    def info_akademik(self):
        print(f"ID Mahasiswa: {self.student_id}")
        print(f"Jurusan: {self.jurusan}")

    # Override perkenalkan_diri
    def perkenalkan_diri(self):
        super().perkenalkan_diri()
        print(f"Saya adalah mahasiswa dengan ID {self.student_id}, jurusan {self.jurusan}.")

# --- Kode Utama ---
if __name__ == "__main__":
    dosen = Person("Pak Anton", 45)
    dosen.perkenalkan_diri()
    print("\n" + "=" * 30 + "\n")
    mahasiswa = Student("Dewi", 20, "MHS001", "Teknik Komputer")
    mahasiswa.perkenalkan_diri()
    mahasiswa.info_akademik()
    print(f"\nUsia mahasiswa {mahasiswa.nama}: {mahasiswa.usia}")