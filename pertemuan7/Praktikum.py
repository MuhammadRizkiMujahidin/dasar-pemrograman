#Muhammad Rizki Mujahidin
#2606375
#1
harga = 25000
total = 0

for i in range(5):
    total += harga
    print(f"Total Biaya Pembelian: {total}")

#2
total = 0

for i in range(5):
    nilai = float(input("Masukkan nilai mahasiswa: "))
    total += nilai

rata_rata = total / 5

print("Rata-rata nilai:", rata_rata)

#3
total = 0

for i in range(0, 21, 2):
    total += i

print("Jumlah bilangan genap:", total)

#4
jumlah_lulus = 0

for i in range(5):
    nilai = float(input("Masukkan nilai mahasiswa: "))

    if nilai >= 65:
        jumlah_lulus =+ 1

print("Jumlah mahasiswa yang lulus:", jumlah_lulus)