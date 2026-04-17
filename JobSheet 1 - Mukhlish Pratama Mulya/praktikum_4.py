# -*- coding: utf-8 -*-

# 1. FOR Loop dengan range()
print("1) FOR loop dengan range()")
for i in range(5):
    print("Perulangan ke-", i)
# range(5) menghasilkan nilai 0, 1, 2, 3, dan 4
# Sehingga perulangan akan berjalan sebanyak 5 kali

print() # pemisah output

# 2. FOR Loop untuk mengiterasi List
print("2) FOR loop mengiterasi list")
buah = ["apel", "mangga", "jeruk", "pisang"]
for item in buah:
    print("Buah:", item)
# Loop akan mengeksekusi setiap elemen dalam list "buah"

print()

# 3. WHILE Loop
print("3) WHILE loop sederhana")
count = 0
while count < 5:
    print("count =", count)
    count += 1 # increment
# Perulangan while terus dijalankan selama kondisi (count < 5) bernilai True

print()

# 4. BREAK pada Loop
print("4) BREAK di dalam loop")
for i in range(10):
    if i == 3:
        print("Loop dihentikan pada i =", i)
        break # mengakhiri loop saat i = 3
    print("i =", i)
# Keyword break langsung menghentikan keseluruhan perulangan

print()

# 5. CONTINUE pada Loop
print("5) CONTINUE di dalam loop")
for i in range(5):
    if i == 2:
        print("Lewati i =", i, "dengan continue")
        continue # melewati iterasi saat ini dan lanjut ke iterasi berikutnya
    print("i =", i)
# Saat i = 2, baris print("i =", i) tidak akan dieksekusi

print()

# 6. NESTED Loop (Loop Bersarang)
print("6) NESTED loop")
for i in range(3):    # Loop luar (outer loop)
    for j in range(2):    # Loop dalam (inner loop)
        print(f"i={i}, j={j}")
# Pada setiap iterasi i, loop j akan berjalan dari 0 sampai 1

print()

# 7. Memanfaatkan ELSE pada Loop
print("7) ELSE pada loop for/while")
# Python memiliki fitur unik: blok else pada loop
# Blok else akan dieksekusi jika loop selesai tanpa di-break.

for x in range(3):
    print("x =", x)
else:
    print("Loop for telah selesai tanpa break.\n")

y = 0
while y < 3:
    print("y =", y)
    y += 1
else:
    print("Loop while telah selesai tanpa break.\n")

# 8. PASS sebagai placeholder
print("8) PASS (placeholder)")
for i in range(3):
    if i == 1:
        pass # pass tidak melakukan apa-apa, digunakan sebagai placeholder
    print("i =", i)