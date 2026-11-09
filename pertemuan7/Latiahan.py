#Contoh pengulangan for sederhana
angka = [1,2,3,4,5]
for x in angka:
  print(x)

#Contoh pengulangan for
buah = ["nanas", "apel", "jeruk"]
for makanan in buah:
  print ("Saya suka makan", makanan)

  jumlah_perulangan = 5

  for index in range(jumlah_perulangan):
    print(f"Print ke- {index}")

buah  = ["apel", "belimbing", "ceri", "durian"]
for i in buah:
  print(f"Buah: {i}")

for i in range(len(buah)):
  print(f"Buah: {buah[i]}")

for i in range(0,11,2):
  print(f"Nilai ke-{i}")