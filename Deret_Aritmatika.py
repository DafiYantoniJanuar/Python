print('='*45)
print('\tMenghitung Deret Aritmatika')
print('='*45)

a = int(input('Masukkan suku pertama (a)\t: '))
b = int(input('Masukkan suku beda (b)\t\t: '))
n = int(input('Masukkan jumlah suku (n)\t: '))

S_n = int(n / 2) * (2 * a + (n - 1) * b)

print('Jumlah deret aritmatika\t\t: ',S_n)