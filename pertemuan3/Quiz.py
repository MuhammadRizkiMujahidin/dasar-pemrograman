#Muhammad Rizki Mujahidin
#2606375

# NOMOR 1 
nilai = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]

# a. Nilai maksimum, minimum, dan rata-rata
nilai_maksimum = max(nilai)
nilai_minimum = min(nilai)
nilai_rata_rata = sum(nilai) / len(nilai)

print("===== NOMOR 1 =====")
print(f"a. Nilai maksimum : {nilai_maksimum}")
print(f"   Nilai minimum  : {nilai_minimum}")
print(f"   Nilai rata-rata: {nilai_rata_rata}")

# b. Angka terbesar kedua
nilai_urut = nilai.copy()
nilai_urut.sort()    
nilai_urut.reverse()  
print(f"b. Angka terbesar kedua: {nilai_urut[1]}")

# NOMOR 2 
jakarta = (-6.2088, 106.8456)
bandung = (-6.9175, 107.6191)
surabaya = (-7.2575, 112.7521)

lokasi = (jakarta, bandung, surabaya)

print("\n===== NOMOR 2 =====")

# a. Koordinat kota Bandung 
latitude, longitude = bandung
print(f"a. Koordinat Bandung: {bandung}")
print(f"   Latitude : {latitude}")
print(f"   Longitude: {longitude}")

# b. Jumlah lokasi yang tersimpan
print(f"b. Jumlah lokasi yang tersimpan: {len(lokasi)}")

# NOMOR 3 - 10 nama teman dalam satu baris

print("\n===== NOMOR 3 =====")
teman_input = input("Input nama teman (pisahkan dengan koma): ")

# strip() buang spasi di awal/akhir, replace() merapikan spasi setelah koma,
# lalu split() memecah teks menjadi list berdasarkan tanda koma
daftar_teman = teman_input.strip().replace(", ", ",").split(",")

print("Output:", daftar_teman)
print("Jumlah teman:", len(daftar_teman))