#Muhammad Rizki Mujahidin
#2606375
def ke_detik(jam, menit, detik):
    return jam * 3600 + menit * 60 + detik


def selisih_waktu(mulai, selesai):
    """mulai & selesai berupa tuple (jam, menit, detik)."""
    selisih = ke_detik(*selesai) - ke_detik(*mulai)
    jam = selisih // 3600
    menit = (selisih % 3600) // 60
    detik = selisih % 60
    return jam, menit, detik


print("Input mulai:")
mulai = (int(input("Jam: ")), int(input("Menit: ")), int(input("Detik: ")))

print("\nInput selesai:")
selesai = (int(input("Jam: ")), int(input("Menit: ")), int(input("Detik: ")))

j, m, d = selisih_waktu(mulai, selesai)
print(f"\nOutput: {j} jam - {m} menit - {d} detik")