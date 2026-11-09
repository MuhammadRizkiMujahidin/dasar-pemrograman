
# Muhammad Rizki Mujahidin
# 2606375

def tentukan_grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    else:
        return "E"


def cek_kelulusan(nilai):
    return "Lulus" if nilai >= 60 else "Tidak Lulus"


def main():
    print("=== PROGRAM PENILAIAN ===")

    try:
        nilai = float(input("Masukkan nilai (0-100): "))

        if not 0 <= nilai <= 100:
            print("Error: Nilai harus antara 0 sampai 100.")
            return

        grade = tentukan_grade(nilai)
        status = cek_kelulusan(nilai)

        print("\n=== HASIL PENILAIAN ===")
        print(f"Nilai  : {nilai}")
        print(f"Grade  : {grade}")
        print(f"Status : {status}")

    except ValueError:
        print("Error: Input harus berupa angka.")


if __name__ == "__main__":
    main()
