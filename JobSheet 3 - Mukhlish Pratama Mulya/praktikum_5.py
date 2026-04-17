class Calculator:
    def __init__(self, initial_value=0):
        """
        Konstruktor kelas Calculator.
        - self: Mengacu pada instance (objek) yang sedang dibuat.
        - initial_value: Nilai awal dari kalkulator.
        """
        self.value = initial_value
        print(f"Kalkulator diinisialisasi dengan nilai: {self.value}")

    def add(self, number):
        """Menambahkan 'number' ke nilai yang tersimpan di objek."""
        self.value += number
        print(f"Setelah penambahan {number}, nilai sekarang adalah: {self.value}")

    def subtract(self, number):
        """Mengurangi 'number' dari nilai yang tersimpan."""
        self.value -= number
        print(f"Setelah pengurangan {number}, nilai sekarang adalah: {self.value}")

    def reset(self):
        """Mengatur ulang nilai kalkulator ke 0."""
        self.value = 0
        print("Nilai telah direset ke 0.")

    def show_value(self):
        """Menampilkan nilai saat ini dari kalkulator."""
        print(f"Nilai saat ini adalah: {self.value}")

def main():
    # 1. Membuat objek calc1 dengan nilai awal 10
    calc1 = Calculator(initial_value=10)
    calc1.add(5)
    calc1.subtract(3)
    calc1.show_value()

    print("-" * 20)

    # 2. Membuat objek calc2 dengan nilai default (0)
    # Perhatikan bahwa calc2 tidak terpengaruh oleh operasi pada calc1
    calc2 = Calculator()
    calc2.add(20)
    calc2.show_value()

if __name__ == "__main__":
    main()