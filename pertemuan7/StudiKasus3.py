#Nama: Muhammad Rizki Mujahidin
#NIM: 2606375
n = int(input("Masukan Jumlah Bilangan: "))
bilangan = []
for i in range(n):
    angka = int(input(f"Bilangan ke-{i+1}: "))
    bilangan.append(angka)

for angka in bilangan:
    if angka % 2 == 0:
        print(f"Bilangan {angka} adalah genap")
    else:
        print(f"Bilangan {angka} adalah ganjil")

