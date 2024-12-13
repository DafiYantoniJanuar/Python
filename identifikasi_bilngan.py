print("="*45)
print("\tBILANGAN POSITIF DAN NEGATIF")
print("="*45)

angka_list = []
jumlah = int(input('masukkan jumlah yang ingin di identifikasi: '))

for i in range(jumlah):
    angka = float(input(f"Masukkan angka ke-{i+1}\t: "))
    angka_list.append(angka)

positif = [x for x in angka_list if x > 0]
negatif = [x for x in angka_list if x < 0]

print('Bilangan Positif\t:', positif)
print('Bilangan Negatif\t:', negatif)