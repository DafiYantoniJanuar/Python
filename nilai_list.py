nilai = []
jml = int(input('Jumlah data yang akan di input: '))

for i in range(jml):
    nilai.append(float(input(f'Nilai ke-{i+1} : ')))

total = max = 0
min = nilai[0]
for data in nilai:
    total += data
    if data > max:
        max = data

    if data < min:
        min = data

print(f'tampilkan total {total}')
print(f'tampilkan nilai {max}')
print(f'tampilkan nilai {min}')

