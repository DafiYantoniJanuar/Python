print("="*50)
print('\tMEMBACA NOMOR BULAN DAN TAHUN')
print("="*50)

bulan = int(input('Masukkan nomor bulan (1-12)\t: '))
tahun = int(input('Masukkan tahun \t\t\t: '))

hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    hari_per_bulan[1] = 29

jumlah_hari_dalam_bulan = hari_per_bulan[bulan - 1]
print(f'Jumlah hari dalam bulan {bulan} Tahun {tahun} Adalah {jumlah_hari_dalam_bulan}')