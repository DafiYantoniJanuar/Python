print('='*50)
print('\t\tANGKA ROMAWI')
print('='*50)

angka = int(input('Masukkan angka 1-15 \t\t: '))

romawi = ['I', 'II', 'III','IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']

if 1 <=  angka <= 15:
    print(f"{angka} dalam angka romawi adalah\t: {romawi[angka-1]}")
else:
    print('Angka salah. Tolong masukkan angka 1-15.')