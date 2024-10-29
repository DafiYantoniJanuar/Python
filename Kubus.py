def persegi():
    sisi = int(input('Masukan nilai sisi\t :'))
    luas = lambda S : S * (S * S)
    keliling = lambda : sisi + sisi + sisi + sisi

    print('luas persegi\t\t:' ,luas(sisi),'cm2')
    print('keliling persegi\t\t:' ,keliling(),'cm' )
persegi()