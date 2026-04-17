class Person:
    def __init__(self, name, age):
        """
        Konstruktor untuk menginisialisasi objek Person.
        Memanggil setter secara otomatis untuk validasi awal.
        """
        self.name = name
        self.age = age

    @property
    def name(self):
        """Getter untuk atribut name."""
        return self.__name

    @name.setter
    def name(self, value):
        """Setter untuk atribut name dengan validasi."""
        if not value:
            print("Nama tidak boleh kosong.")
        else:
            self.__name = value

    @property
    def age(self):
        """Getter untuk atribut age."""
        return self.__age

    @age.setter
    def age(self, value):
        """Setter untuk atribut age dengan validasi."""
        if value < 0:
            print("Umur tidak boleh negatif!")
        else:
            self.__age = value

def main():
    # 1. Membuat objek Person
    person = Person("Alice", 30)
    print(f"Nama: {person.name}, Umur: {person.age}")

    # 2. Mengubah nama dan umur melalui setter (seperti mengakses variabel biasa)
    person.name = "Bob"
    person.age = 35
    print(f"Nama baru: {person.name}, Umur baru: {person.age}")

    # 3. Mencoba memasukkan nilai yang tidak valid
    print("\nMencoba input tidak valid:")
    person.age = -5
    person.name = ""

if __name__ == "__main__":
    main()