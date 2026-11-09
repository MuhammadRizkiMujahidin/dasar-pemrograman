#Muhammad Rizki Mujahidin
#2606375
import math
# 1
def fibonacci(n):
    deret = []
    a, b = 0, 1
    for _ in range(n):
        deret.append(a)
        a, b = b, a + b
    return deret

# 2
def volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari ** 2 * tinggi

# 3
def total_rata(*angka):
    total = sum(angka)
    rata = total / len(angka)
    return total, rata
    
print("=== 1. Deret Fibonacci ===")
n = int(input("Banyak suku: "))
print("Deret:", fibonacci(n))

print("\n=== 2. Volume Tabung ===")
r = float(input("Jari-jari: "))
t = float(input("Tinggi: "))
print(f"Volume tabung = {volume_tabung(r, t):.2f}")

print("\n=== 3. Total dan Rata-rata ===")
data = [float(x) for x in input("Masukkan angka (pisahkan dengan spasi): ").split()]
total, rata = total_rata(*data)
print(f"Total     = {total}")
print(f"Rata-rata = {rata}")