print('='*40)
print('\tDaftar Buah')
print('='*40)

daftar_buah = []
print('masukkan nama buah satu persatu. dan ketik "selesai" untuk berhenti: ')

while True:
    buah = (input('masukkan nama buah\t: '))
    if buah.lower() == "selesai":
        break
    daftar_buah.append(buah)

print('Daftar buah yang di masukkan: ')
for x, buah in enumerate(daftar_buah, start=1):
     print(f'{x}. {buah}')