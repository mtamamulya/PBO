class Kucing:
    def bersuara(self): print("Kucing: Meow!")

class Anjing:
    def bersuara(self): print("Anjing: Guk guk!")

class Bebek:
    def bersuara(self): print("Bebek: Kwek kwek!")

class Mobil:
    def jalankan(self): print("Mobil: Brummm!")

def buat_suara(objek):
    try:
        objek.bersuara()
    except AttributeError:
        print(f"Objek {type(objek).__name__} tidak bisa bersuara.")

if __name__ == "__main__":
    daftar_objek = [Kucing(), Anjing(), Bebek(), Mobil()]
    for item in daftar_objek:
        buat_suara(item)