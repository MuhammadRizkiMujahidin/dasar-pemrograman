#Muhammad Rizki Mujahidin
#2606375
nama = input("Masukan Nama Anda: ")
tugas = float(input("Masukan Nilai Tugas Anda: "))
uts = float(input("Masukan Nilai UTS: "))
uas = float(input("Masukan Nilai UAS: "))\

rata_rata = (tugas + uts + uas) / 3

if rata_rata >= 70:
    if tugas >= 60 and uts >= 60 and uas >= 60:
        print(f"{nama} kamu LULUS tanpa remedial")
    else:
        print(f"{nama} kamu LULUS dengan remedial")
elif rata_rata >= 50:
    print(f"{nama} kamu TIDAK LULUS, boleh remedial")
else:
    print(f"{nama} kamu TIDAK LULUS dan tidak boleh remedial")