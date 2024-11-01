def cek_kelulusan(nilai):
    if nilai < 0:
        return "Nilai tidak valid! Nilai harus 0 atau lebih."
    elif nilai > 100:
        return "Salah! Nilai harus 100 atau kurang."
    elif nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"

try:
    nilai = float(input("Masukkan nilai: "))
    hasil = cek_kelulusan(nilai)
    print(hasil)
except ValueError:
    print("Input tidak valid! Masukkan angka.")