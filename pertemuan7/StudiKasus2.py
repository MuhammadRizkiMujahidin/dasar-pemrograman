#Nama: Muhammad Rizki Mujahidin
#NIM: 2606375
n = int(input("Masukan Jumlah Hewan Yang Akan Dimasukan: "))
hewan = []
for i in range(n):
    nama = input(f"Hewan ke-{i+1}: ")
    hewan.append(nama)

for i in range(len(hewan)):
    print(f"hewan ke-{i+1} adalah {hewan[i]}")