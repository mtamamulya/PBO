import math

class Bentuk:
    def hitung_luas(self): raise NotImplementedError("Subclass wajib implementasi")

class Lingkaran(Bentuk):
    def __init__(self, radius): self.radius = radius
    def hitung_luas(self): return math.pi * (self.radius ** 2)

class Persegi(Bentuk):
    def __init__(self, sisi): self.sisi = sisi
    def hitung_luas(self): return self.sisi * self.sisi

class TaplakMeja: # Duck Typing
    def __init__(self, p, l): self.p, self.l = p, l
    def hitung_luas(self): return self.p * self.l

def tampilkan_info_luas(obj):
    print(f"Luas: {obj.hitung_luas():.2f}")

if __name__ == "__main__":
    item = [Lingkaran(7), Persegi(5), TaplakMeja(1.5, 0.8)]
    for i in item: tampilkan_info_luas(i)