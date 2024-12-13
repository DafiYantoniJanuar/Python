print("="*50)
print('\tKONVERSI DURASI WAKTU DALAM DETIK')
print("="*50)

durasi_detik = int(input('Masukkan durasi waktu dalam detik: '))

hari = durasi_detik // (24 * 3600)
durasi_detik %= (24 * 3600)
jam = durasi_detik // 3600
durasi_detik %= 3600
menit = durasi_detik // 60
detik = durasi_detik % 60

print(f"Durasi tersebut adalah '{hari}' hari, '{jam}' jam, '{menit}' menit, dan '{detik}' detik.")