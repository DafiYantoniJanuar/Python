totalBelanja = float(input( 'Masukkan harga total belanja : '))
diskon = 0

if totalBelanja > 1000000:
 diskon = 6 / 100 * totalBelanja
elif totalBelanja > 500000:
 diskon = 4 / 100 * totalBelanja
elif totalBelanja > 100000:
 diskon = 2 / 100 * totalBelanja

totalBayar = totalBelanja - diskon

print(f'''
Harga Beli: {totalBelanja}
Diskon    : {diskon}
Dibayar   : {totalBayar}
''')
