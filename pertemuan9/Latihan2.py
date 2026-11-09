#Muhammad Rizki Mujahidin
#2606375
PASSWORD_BENAR = "Latihan"   
MAKS_PERCOBAAN = 3


def login():
    for percobaan in range(1, MAKS_PERCOBAAN + 1):
        username = input("Usename: ")
        password = input("Masukkan password: ")
        if password == PASSWORD_BENAR:
            print("Login berhasil! Selamat datang, Admin.")
            return True
        sisa = MAKS_PERCOBAAN - percobaan
        if sisa > 0:
            print(f"Password salah! Sisa kesempatan: {sisa}")
    print("Kesempatan habis. Anda keluar dari menu login.")
    return False


print("=== MENU LOGIN ===")
login()