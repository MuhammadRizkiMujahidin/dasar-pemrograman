#Muhammad Rizki Mujahidin
#2606375
nilai = int(input("Masukan Nilai: "))

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Nilai anda: {grade}")