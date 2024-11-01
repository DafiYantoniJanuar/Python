masukan_nomor = 20
masukan_nomor = int(input("masukan nomor sepatumu:\t"))

if masukan_nomor > 40 and masukan_nomor < 46:
    print('besar')
elif masukan_nomor > 35 and masukan_nomor <= 40:
    print("sedang")
elif masukan_nomor >= 30 and masukan_nomor <= 35:
    print('keci')
else:
    print('nomor salah')