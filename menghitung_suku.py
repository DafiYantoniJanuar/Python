print('='*45)
print('\tMenghitung Suku')
print('='*45)

a = int(input('Masukkan suku pertama (a)\t: '))
b = int(input('Masukkan beda (b)\t\t: '))
n = int(input('Masukkan nomor suku (n)\t\t: '))

U_n = a + (n - 1) * b

print(f'Suku ke-{n}\t\t\t: {U_n}')