N = int(input("Masukkan angka N: "))

hasil = N
for i in range(1, N):
    hasil -= i

print(f"Hasil pengurangan dari N hingga 1:", hasil)
