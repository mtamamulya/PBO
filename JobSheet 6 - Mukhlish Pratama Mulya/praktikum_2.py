from abc import ABC, abstractmethod

class MediaAbstrak(ABC):
    def __init__(self, judul):
        self.judul = judul
        print(f"Inisialisasi MediaAbstrak dengan judul: {self.judul}")

    @abstractmethod
    def play(self):
        """Metode abstrak untuk memulai pemutaran."""
        pass

    @abstractmethod
    def stop(self):
        """Metode abstrak untuk menghentikan pemutaran."""
        pass

if __name__ == "__main__":
    print("Mencoba membuat objek dari kelas abstrak MediaAbstrak...")
    try:
        # Baris ini akan menyebabkan TypeError
        media = MediaAbstrak("Konten Abstrak")
    except TypeError as e:
        print(f"\nGAGAL membuat objek!")
        print(f"Error yang muncul (sesuai harapan): {e}")