def penjumlahan_rekursif(angka_list):
    if not angka_list:
        return 0
    return angka_list[0] + penjumlahan_rekursif(angka_list[1:])

angka_list = [1, 2, 3, 4, 5]

jumlah = penjumlahan_rekursif(angka_list)

# Menampilkan hasil
print("Jumlah dari elemen dalam daftar (rekursif):", jumlah)
