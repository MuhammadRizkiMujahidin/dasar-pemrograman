#Muhammad Rizki Mujahidin
#2606375
students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

jumlah_jurusan = {}

for nama, jurusan in students.items():
    jumlah_jurusan[jurusan] = jumlah_jurusan.get(jurusan, 0) + 1

cari = input("Inputkan nama prodi: ")

ditemukan = False
for jurusan, jumlah in jumlah_jurusan.items():
    if jurusan.lower() == cari.lower():
        print("prodi", jurusan.lower(), "sebanyak", jumlah)
        ditemukan = True

if not ditemukan:
    print("prodi", cari, "tidak ditemukan")