#Muhammad Rizki Mujahidin
#2606375
student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

nama = input("Inputkan nama siswa: ")

if nama in student_info:
    umur = student_info[nama]["age"]
    prodi = student_info[nama]["major"]
    print(f"Umur {nama} adalah {umur} dan Prodi nya adalah {prodi}")
else:
    print("Data siswa tidak ditemukan")