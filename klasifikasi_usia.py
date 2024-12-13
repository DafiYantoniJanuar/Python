print('='*45)
print('\tKLASIFIKASI USIA')
print('='*45)

usia = int(input('masukkan usia: '))

if usia > 60 and usia <= 74:
    print('Lansia')
elif usia > 45 and usia <= 59:
    print('Usia Pertengahan')
elif usia > 25 and usia <= 44:
    print('Dewasa')
elif usia > 15 and usia <= 24:
    print('Remaja')
elif usia > 0 and usia <= 14:
    print('Anak-Anak')
else:
    print('Usia Lanjut')