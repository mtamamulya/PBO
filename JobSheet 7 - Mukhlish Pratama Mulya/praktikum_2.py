class KalkulatorAngka:
    def __init__(self):
        print("Kalkulator Angka siap.")

    def bagi(self, angka1, angka2):
        """
        Membagi angka1 dengan angka2.
        Menangani potensi ValueError (jika input bukan angka)
        dan ZeroDivisionError (jika pembagi nol) secara terpisah.
        """
        print(f"\nMencoba membagi '{angka1}' dengan '{angka2}'...")
        try:
            # Konversi input ke float, bisa memicu ValueError
            num1 = float(angka1)
            num2 = float(angka2)

            # Operasi pembagian, bisa memicu ZeroDivisionError
            hasil = num1 / num2

            print(f" -> Hasil pembagian: {hasil}")
            return hasil

        # Menangkap ValueError secara spesifik
        except ValueError:
            print(" -> ERROR: Input tidak valid! Pastikan kedua input adalah angka.")
            return None

        # Menangkap ZeroDivisionError secara spesifik
        except ZeroDivisionError:
            print(" -> ERROR: Tidak bisa melakukan pembagian dengan nol.")
            return None

        # Menangkap exception lain yang mungkin tidak terduga (opsional)
        except Exception as e:
            print(f" -> ERROR Lainnya: Terjadi kesalahan - {e}")
            return None

# --- Kode Utama ---
if __name__ == "__main__":
    calc = KalkulatorAngka()

    print("--- Tes Kalkulator ---")
    hasil1 = calc.bagi(100, 5)        # Operasi sukses
    hasil2 = calc.bagi(20, 0)         # Memicu ZeroDivisionError
    hasil3 = calc.bagi("limapuluh", 10) # Memicu ValueError saat konversi num1
    hasil4 = calc.bagi(50, "sepuluh") # Memicu ValueError saat konversi num2

    print("\n--- Ringkasan Hasil ---")
    print(f"Hasil 1 (100/5): {hasil1}")
    print(f"Hasil 2 (20/0): {hasil2}")
    print(f"Hasil 3 ('limapuluh'/10): {hasil3}")
    print(f"Hasil 4 (50/'sepuluh'): {hasil4}")