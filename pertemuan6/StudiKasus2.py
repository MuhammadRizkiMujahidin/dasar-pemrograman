#Muhammad Rizki Mujahidin
#2606375
gender = input("Masukan Gender Anda: ")
umur = int(input("Masukan Umur Anda: "))
tinggi = int(input("Masukan Tinggi Badan Anda: "))
iq = int(input("Masukan IQ Anda: "))

if gender == "pria":
    tinggi_minimum = 175
elif gender == "wanita":
    tinggi_minimum = 170
else:
    tinggi_minimum = None

if tinggi_minimum is None:
    print("Jenis Kelamin Tidak Valid")
elif 18 <= umur <= 25 and tinggi >= tinggi_minimum and iq >= 130:
    print("Selamat Kamu Terpilih Menjadi Model Catwalk")
else:
    print("Mohon Maaf Kamu Belum Memenuhi Kriteria")