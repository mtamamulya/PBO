#1. Pendeklarasian Variabel
nama = "Budi"
umur = 20
tinggi = 170.5
is_student = True

print("Nama =", nama)
print("Umur =", umur)
print("Tinggi =", tinggi, "cm")
print("Mahasiswa =", is_student)


#2. Operasi Aritmetika
a = 10
b = 3

penjumlahan = a + b       # Tambah
pengurangan = a - b       # Kurang
perkalian = a * b         # Kali
pembagian = a / b         # Bagi (hasil float)
pembagian_bulat = a // b  # Bagi (bulat)
modulus = a % b           # Sisa bagi
pangkat = a ** b          # Pemangkatan

print("\nOPERASI ARITMETIKA")
print("a =", a, ", b =", b)
print("Penjumlahan =", penjumlahan)
print("Pengurangan =", pengurangan)
print("Perkalian =", perkalian)
print("Pembagian =", pembagian)
print("Pembagian Bulat =", pembagian_bulat)
print("Modulus =", modulus)
print("Pangkat =", pangkat)

#3. Operasi Perbandingan
#Menghasilkan nilai Boolean (True/False)
lebih_besar = a > b
kurang_dari = a < b
sama_dengan = a == b
tidak_sama = a != b
lebih_besar_sama = a >= b
kurang_sama = a <= b

print("\nOPERASI PERBANDINGAN")
print("a > b =", lebih_besar)
print("a < b =", kurang_dari)
print("a == b =", sama_dengan)
print("a != b =", tidak_sama)
print("a >= b =", lebih_besar_sama)
print("a <= b =", kurang_sama)

#4. Operasi Logika
#and, or, not

x = True
y = False

logika_and = x and y
logika_or = x or y
logika_not_x = not x

print("\nOPERASI LOGIKA")
print("x =", x, ", y =", y)
print("x and y =", logika_and)
print("x or y =", logika_or)
print("not x =", logika_not_x)

# 5. Contoh penggunaan di dalam percabangan
if a > b and b > 0:
    print("\nKondisi terpenuhi: a lebih besar dari b, dan b masih positif.")
else:
    print("\nKondisi tidak terpenuhi atau b <= 0.")