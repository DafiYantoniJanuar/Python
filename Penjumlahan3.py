matriks1 = [
    [1, 2],
    [3, 4]
]

matriks2 = [
    [5, 6],
    [7, 8]
]

hasil = [
    [matriks1[i][j] + matriks2[i][j] for j in range(2)]
    for i in range(2)
]

print("Hasil penjumlahan matriks:")
for baris in hasil:
    print(baris)
