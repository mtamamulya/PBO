#Penugasan 2
angka = int(input("Masukkan bilangan: "))

if angka % 2 == 0:
    jenis = "Genap"
else:
    jenis =  "Ganjil"

is_prima = True
if angka <= 1 :
    is_prima = False
else:
    for i in range(2, angka):
        if angka % i == 0:
            is_prima = False
            break

if is_prima:
    status = "dan merupakan bilangan prima"
else:
    status = "dan BUKAN merupakan bilangan prima"

print(f"Angka {angka} adalah bilangan {jenis} {status}.")