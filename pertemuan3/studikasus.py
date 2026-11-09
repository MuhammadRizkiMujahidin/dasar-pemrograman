#Muhammad Rizki Mujahidin
#2606375
buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

# 1
index_ceri = buah.index("ceri")
buah[index_ceri] = "cherry"
print("Setelah mengganti ceri:", buah)

# 2     

nama_buah = input("\nMasukkan nama buah yang ingin ditambahkan: ")
index_baru = int(input("Masukkan index tempat buah tersebut: "))

buah.insert(index_baru, nama_buah.strip().lower())
print("Setelah menambah item        :", buah)

# 3
buah.sort()
print("Setelah diurutkan sesuai abjad:", buah)
