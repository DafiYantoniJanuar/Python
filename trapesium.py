def trapesium():
    sisiA = int(input('Masukan sisi A\t\t: '))
    sisiB = int(input('Masukan sisi B\t\t: '))
    tinggi = int(input('Masukan tinggi nya\t\t: '))
    luas = lambda : 0.5 * (sisiA + sisiB) * tinggi
    
    print('luas trapesium\t\t:' ,luas(), 'cm2')
trapesium()