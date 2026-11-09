#Nama: Muhammad Rizki Mujahidin
#NIM: 2606375
usn = "dasproRPL"
pswd = "RPLfire!123"

while True:
    username = input("Username: ")
    password = input("Password: ")

    if username == usn and password == pswd:
        print("Login Berhasil")
        break
    else:
        print("Usernam atau password salah. Coba lagi.\n")