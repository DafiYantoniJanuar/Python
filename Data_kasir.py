print('='*50)
print('\t\tMESIN KASIR')
print('='*50)

produk = {
    'biskuit': 5000,
    'keripik': 10000,
    'cokelat': 15000,
    'susu': 17000, 
    'apel': 5000, 
    'jeruk': 7000, 
    'mangga': 10000, 
    'anggur': 15000
}

keranjang = []
total = 0

while True:
    barang = input('Masukkan nama produk (atau ketik "selesai" untuk berhenti): ')
    if barang.lower() == 'selesai':
        break
    if barang in produk:
        keranjang.append(barang)
        total += produk[barang]
    else:
        print('Produk tidak ditemukan!')

print('='*50)
print('\n\t\tStruk Pembelian\n')
print('='*50)
for barang in keranjang:
    print(f'{barang.title()}\t\t: Rp {produk[barang]}')
print('='*50)
print(f'Total Harga\t: Rp {total}')
print('='*50)
print('\tTerima kasih telah berbelanja!')