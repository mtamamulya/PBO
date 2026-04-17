#Penugasan 1
berat = float(input("Masukkan berat badan anda (kg): "))
tinggi_cm = float(input("Masukkan tinggi badan anda (cm): "))

tinggi_m = tinggi_cm / 100

bmi = berat / (tinggi_m ** 2)

if bmi < 18.5:
    kategori = "Underweight (Kekurangan berat badan)"
elif bmi < 25:
    kategori = "Normal (Ideal)"
elif bmi < 30:
    kategori = "Overweight (Kelebihan berat badan)"
else:
    kategori = "Obese (Kegemukan)"

print("\n--- HASIL PERHITUNGAN BMI ---")
print(f"Nilai BMI Anda : {bmi:.2f}")
print(f"Kategori       : {kategori}")