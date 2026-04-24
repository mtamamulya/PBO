class Burung:
    def terbang(self): print("Terbang umum")
class Elang(Burung):
    def berburu(self): print("Berburu!")
class Pipit(Burung):
    def membangun_sarang(self): print("Sarang dibangun!")

def interaksi(burung):
    if isinstance(burung, Burung):
        burung.terbang()
        if isinstance(burung, Elang): burung.berburu()
        elif isinstance(burung, Pipit): burung.membangun_sarang()

if __name__ == "__main__":
    interaksi(Elang())
    interaksi(Pipit())