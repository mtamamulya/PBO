class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = None
        self.__grade = None

        self.score = score
    
    #--- Property untuk Name ---
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value:
            self.__name = value
        else:
            print("Nama tidak boleh kosong!")

    #--- Property untuk Score ---
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
            self.__update_grade()
        else:
            print(f"Nilai {value} tidak valid! (Harus 0-100)")

    #--- Property untuk Grade
    @property
    def grade(self):
        return self.__grade
    
    #--- Method untuk update grade ---
    def __update_grade(self):
        if self.__score >= 90:
            self.__grade = "A"
        elif self.__score >= 80:
            self.__grade = "B"
        elif self.__score >= 70:
            self.__grade = "C"
        elif self.__score >= 60:
            self.__grade = "D"
        else:
            self.__grade = "E"

    #--- Method untuk menampilkan info ---
    def show_info(self):
        print(f"Nama Mahasiswa: {self.name}")
        print(f"Nilai: {self.score}")
        print(f"Grade: {self.grade}")
        print()

    #--- Destruktor ---
    def __del__(self):
        print(f"Data mahasiswa {self.name} telah dihapus dari sistem.")

#--- Eksekusi Program ---
if __name__ == "__main__":
    #Membuat objek mhs
    mhs1 = Student("Sony", 85)
    mhs1.show_info()

    #Mengubah nilai(grade akan terupdate otomatis)
    print("Nilai diubah")
    mhs1.score = 91
    mhs1.show_info()

    #menghapus objek
    del mhs1