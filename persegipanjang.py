def persegipanjang():
    panjang = int(input('Masukan Panjang nya\t: '))
    lebar = int(input('Masukan Lebar nya\t: '))
    luas = lambda : panjang * lebar
    keliling = lambda : 2 * (panjang + lebar)

    print('luas persegipanjang\t\t:' ,luas(),'cm2')
    print('keliling persegipanjang\t\t:' ,keliling(),'cm')
persegipanjang()