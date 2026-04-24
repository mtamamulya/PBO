class KalkulatorSederhana:
    def __init__(self, nama="Kalkulator"):
        self.nama = nama

    def tambah(self, *args):
        total = 0
        for angka in args:
            if isinstance(angka, (int, float)):
                total += angka
        return total

if __name__ == "__main__":
    calc = KalkulatorSederhana("Calc-01")
    print(calc.tambah(5, 10))
    print(calc.tambah(2, 3, 5, 10))