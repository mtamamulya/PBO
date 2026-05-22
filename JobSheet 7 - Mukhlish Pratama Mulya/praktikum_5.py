# Ganti fungsi locale dengan fungsi manual agar stabil di Google Colab
def format_rupiah(angka):
    # Menggunakan f-string untuk ribuan dan mengganti koma menjadi titik
    return f"Rp {angka:,.0f}".replace(",", ".")

class PengelolaAkun:
    def __init__(self, nomor_akun, saldo_awal=0):
        print(f"\nMencoba membuat akun {nomor_akun}...")
        if not isinstance(saldo_awal, (int, float)) or saldo_awal < 0:
            # 1. Raise ValueError di init jika saldo awal tidak valid
            raise ValueError(f"Saldo awal ({saldo_awal}) tidak valid. Harus angka non-negatif.")

        self.nomor_akun = nomor_akun
        self._saldo = float(saldo_awal)
        print(f" -> Akun {self.nomor_akun} berhasil dibuat dengan saldo: {format_rupiah(self._saldo)}")

    def get_saldo(self):
        """Mengembalikan saldo saat ini."""
        return self._saldo

    def tarik_tunai(self, jumlah):
        """Menarik tunai dengan validasi. Me-raise exception jika gagal."""
        print(f"\n[{self.nomor_akun}] Mencoba tarik tunai: {format_rupiah(jumlah)}")

        # 2. Validasi jumlah penarikan
        if not isinstance(jumlah, (int, float)) or jumlah <= 0:
            raise ValueError(f"Jumlah penarikan ({jumlah}) tidak valid. Harus angka positif.")

        # 3. Validasi saldo cukup
        if jumlah > self._saldo:
            raise RuntimeError(f"Saldo tidak mencukupi! Saldo: {format_rupiah(self._saldo)}, Diminta: {format_rupiah(jumlah)}")

        # Jika semua validasi lolos, lakukan penarikan
        self._saldo -= jumlah
        print(f" -> Penarikan {format_rupiah(jumlah)} berhasil.")
        print(f" -> Saldo sekarang: {format_rupiah(self._saldo)}")
        return True

# --- Kode Utama ---
if __name__ == "__main__":
    # Skenario 1: Gagal membuat akun karena saldo awal tidak valid
    print("--- Skenario 1: Saldo Awal Tidak Valid ---")
    try:
        akun_gagal = PengelolaAkun("ACC001", -50000)
    except ValueError as e:
        print(f"  ERROR DITANGKAP: {e}")

    # Skenario 2: Membuat akun valid, lalu coba transaksi
    print("\n--- Skenario 2: Akun Valid dan Transaksi ---")
    try:
        akun_sukses = PengelolaAkun("ACC002", 100000)
        akun_sukses.tarik_tunai(30000)

        print("\n  Mencoba tarik jumlah negatif...")
        akun_sukses.tarik_tunai(-10000)
    except ValueError as e:
        print(f"  ERROR DITANGKAP (ValueError): {e}")

    # Skenario 3: Gagal karena saldo tidak cukup
    print("\n--- Skenario 3: Saldo Tidak Cukup ---")
    try:
        print(f"    Saldo saat ini: {format_rupiah(akun_sukses.get_saldo())}")
        akun_sukses.tarik_tunai(80000)
    except RuntimeError as e:
        print(f"  ERROR DITANGKAP (RuntimeError): {e}")

    print(f"\nSaldo akhir {akun_sukses.nomor_akun}: {format_rupiah(akun_sukses.get_saldo())}")