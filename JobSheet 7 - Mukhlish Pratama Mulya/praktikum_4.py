class KalkulatorAngka:
    def __init__(self):
        print("Kalkulator Angka siap.")

    def bagi(self, angka1, angka2):
        """
        Membagi angka1 dengan angka2.
        Menangkap objek exception untuk menampilkan detail error.
        """
        print(f"\nMencoba membagi '{angka1}' dengan '{angka2}'...")
        try:
            num1 = float(angka1)
            num2 = float(angka2)

            if num2 == 0:
                # Bisa juga raise ZeroDivisionError di sini jika mau
                raise ZeroDivisionError("Pembagi tidak boleh nol secara eksplisit.")

            hasil = num1 / num2
            print(f" -> Hasil pembagian: {hasil}")
            return hasil

        # Menangkap ValueError dan menyimpannya di variabel 'e_val'
        except ValueError as e_val:
            print(" -> ERROR Konversi: Input tidak valid.")
            # Menampilkan representasi string dari objek exception e_val
            print(f"     Detail Error (ValueError): {e_val}")
            return None

        # Menangkap ZeroDivisionError dan menyimpannya di variabel 'e_zero'
        except ZeroDivisionError as e_zero:
            print(" -> ERROR Pembagian: Tidak dapat membagi dengan nol.")
            # Menampilkan representasi string dari objek exception e_zero
            print(f"     Detail Error (ZeroDivisionError): {e_zero}")
            return None

        # Menangkap exception lain dan menyimpannya di variabel 'e'
        except Exception as e:
            print(" -> ERROR Lainnya: Terjadi kesalahan tak terduga.")
            # Menampilkan representasi string dari objek exception e
            print(f"     Detail Error (Lainnya): {type(e).__name__} - {e}")
            return None

# --- Kode Utama ---
if __name__ == "__main__":
    calc = KalkulatorAngka()

    print("--- Tes Kalkulator ---")
    hasil1 = calc.bagi(100, 5)             # Sukses
    hasil2 = calc.bagi(20, 0)              # Memicu ZeroDivisionError
    hasil3 = calc.bagi("limapuluh", 10)    # Memicu ValueError
    hasil4 = calc.bagi(10, [])             # Memicu TypeError (ditangkap except Exception)

    print("\n--- Ringkasan Hasil ---")
    print(f"Hasil 1 (100/5): {hasil1}")
    print(f"Hasil 2 (20/0): {hasil2}")
    print(f"Hasil 3 ('limapuluh'/10): {hasil3}")
    print(f"Hasil 4 (10/[]): {hasil4}")