def segitiga():
    alas = int(input('Masukan alasnya\t: '))
    tinggi = int(input('Masukan tinggi nya\t: '))
    sisi = int(input('Masukan sisi nya\t: '))
    luas = lambda : 0.5 * alas * tinggi
    keliling = lambda : sisi + sisi + sisi

    print('Luas segitiga\t\t:' ,luas(),'cm2')
    print('Keliling segitiga\t\t:' ,keliling(),'cm')
segitiga()
segitiga()
segitiga()

