# File utama untuk simulasi Penjualan HP
import perangkat

def main():
    # 1. Membuat objek (instance) dari kelas Handphone
    hp1 = perangkat.Handphone("Samsung", "Galaxy S24", 15000000, 10)
    hp2 = perangkat.Handphone("Apple", "iPhone 15", 16500000, 5)

    print("=== DAFTAR PRODUK TERSEDIA ===")
    hp1.tampilkan_info()
    hp2.tampilkan_info()

    # 2. Simulasi Transaksi
    print("\n--- Proses Pembelian ---")
    jumlah_beli = 2
    
    if hp1.kurangi_stok(jumlah_beli):
        total = perangkat.hitung_total_bayar(hp1.harga, jumlah_beli)
        print(f"Berhasil membeli {jumlah_beli} unit {hp1.model}")
        print(f"Total yang harus dibayar: Rp {total:,}")
    
    print("\n=== STATUS STOK TERBARU ===")
    hp1.tampilkan_info()

if __name__ == "__main__":
    main()