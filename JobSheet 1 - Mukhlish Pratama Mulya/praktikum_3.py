#1. IF Sederhana
#Program hanya mengeksekusi blok jika kondisinya True

nilai = 85
print("Contoh IF Sederhana:")
if nilai > 80:
    print("Selamat! Anda lulus dengan nilai tinggi.\n")


#2. IF-ELSE
#Jika kondisi True, eksekusi blok if; jika False, eksekusi blok else

umur = 17
print("Contoh IF-ELSE:")
if umur >= 18:
    print("Anda sudah cukup umur untuk mendapatkan SIM.")
else:
    print("Anda belum cukup umur untuk mendapatkan SIM.\n")


#3. IF-ELIF-ELSE
#Menangani banyak kondisi secara berurutan.
#Jika ada kondisi yang terpenuhi, blok yang bersangkutan dieksekusi,
#lalu program melewati blok kondisi setelahnya.

hari = "Rabu"
print("Contoh IF-ELIF-ELSE:")
if hari == "Senin":
    print("Hari Senin - Saatnya kembali bekerja!")
elif hari == "Selasa":
    print("Hari Selasa - Jadwal rapat mingguan.")
elif hari == "Rabu":
    print("Hari Rabu - Ada diskon di beberapa toko.")
else:
    print("Hari lainnya - Atur jadwalmu dengan baik.\n")


#4. IF Bersarang (Nested IF)
#Kondisi di dalam kondisi, biasa digunakan jika kita perlu
#memeriksa sub-kondisi setelah kondisi pertama terpenuhi.

suhu = 35
print("Contoh IF Bersarang (Nested IF):")
if suhu > 30:
    print("Cuaca cukup panas.")
    if suhu > 40:
        print("Bahkan sangat terik! Disarankan banyak minum air.")
    else:
        print("Masih relatif normal, tapi tetap jaga kesehatan.")
else:
    print("Cuaca sepertinya cukup sejuk.\n")


#5. Menggabungkan Percabangan dengan Operasi Logika
#Memeriksa beberapa kondisi sekaligus dengan and, or, not

nilai_teori = 75
nilai_praktik = 80
print("Contoh IF dengan Operasi Logika AND/OR:")
if nilai_teori >= 70 and nilai_praktik >= 70:
    print("Anda lulus karena nilai teori dan praktik memadai.")
elif nilai_teori < 70 and nilai_praktik < 70:
    print("Anda perlu meningkatkan nilai teori dan praktik.")
elif nilai_teori < 70:
    print("Anda perlu meningkatkan nilai teori.")
else:
    print("Anda perlu meningkatkan nilai praktik.\n")


#6. Penggunaan If Ternary (atau Conditional Expression)
#Bentuk ringkas: <hasil_if_true> if <kondisi> else <hasil_if_false>

angka = -5
print("Contoh If Ternary (Conditional Expression):")
status = "Positif" if angka > 0 else "Negatif atau Nol"
print("Angka =", angka, "=>", status)