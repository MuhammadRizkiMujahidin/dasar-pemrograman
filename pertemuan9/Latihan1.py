
# Muhammad Rizki Mujahidin
# 2606375

import math


def fibonacci(jumlah_suku):
    """Menghasilkan deret Fibonacci sebanyak jumlah suku."""
    if jumlah_suku < 0:
        raise ValueError("Jumlah suku tidak boleh negatif.")

    deret = []
    a, b = 0, 1

    for _ in range(jumlah_suku):
        deret.append(a)
        a, b = b, a + b

    return deret


def volume_tabung(jari_jari, tinggi):
    """Menghitung volume tabung."""
    if jari_jari <= 0 or tinggi <= 0:
        raise ValueError("Jari-jari dan tinggi harus positif.")

    return math.pi * jari_jari ** 2 * tinggi


def hitung_total_rata_rata(*angka):
    """Menghitung total dan rata-rata sekumpulan angka."""
    if not angka:
        raise ValueError("Data tidak boleh kosong.")

    total = sum(angka)
    rata_rata = total / len(angka)

    return total, rata_rata


def main():
    try:
        # 1. Deret Fibonacci
        print("=== 1. Deret Fibonacci ===")
        jumlah = int(input("Banyak suku: "))
        print("Deret:", fibonacci(jumlah))

        # 2. Volume Tabung
        print("\n=== 2. Volume Tabung ===")
        jari_jari = float(input("Jari-jari: "))
        tinggi = float(input("Tinggi: "))

        volume = volume_tabung(jari_jari, tinggi)
        print(f"Volume tabung: {volume:.2f}")

        # 3. Total dan Rata-rata
        print("\n=== 3. Total dan Rata-rata ===")
        data = [
            float(angka)
            for angka in input(
                "Masukkan angka (pisahkan dengan spasi): "
            ).split()
        ]

        total, rata_rata = hitung_total_rata_rata(*data)

        print(f"Total     : {total}")
        print(f"Rata-rata : {rata_rata:.2f}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
