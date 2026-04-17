class SimpleExample:
    def __init__(self, name):
        """
        Konstruktor: Dipanggil otomatis saat objek dibuat.
        """
        self.name = name
        print(f"Konstruktor: Objek '{self.name}' telah dibuat.")

    def __del__(self):
        """
        Destruktor: Dipanggil otomatis saat objek dihapus dari memori.
        """
        print(f"Destruktor: Objek '{self.name}' sedang dihapus.")

def main():
    print("Program dimulai.\n")

    # 1. Membuat objek (Memanggil __init__)
    obj = SimpleExample("Demo")
    
    print("Program sedang berjalan...\n")

    # 2. Menghapus objek secara eksplisit (Memanggil __del__)
    del obj
    
    print("Objek telah dihapus secara eksplisit.\n")
    print("Program selesai.")

if __name__ == "__main__":
    main()