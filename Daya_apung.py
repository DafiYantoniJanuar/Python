print('=' * 65)
print('\tProgram Menghitung Gaya Apung (Hukum Archimedes)')
print('=' * 65)

massa_jenis_fluida = float(input('Masukkan massa jenis fluida (kg/m³)\t\t: '))
volume_benda = float(input('Masukkan volume benda yang tercelup (m³)\t: '))
gravitasi = 10

gaya_apung = massa_jenis_fluida * volume_benda * gravitasi

print('Gaya apung yang dialami benda adalah\t\t:',gaya_apung, 'Newton')