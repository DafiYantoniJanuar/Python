def tabung():
    KA = int(input('Masukan keliling alas : '))
    LA = int(input('Masukan luas alas     : '))
    T = int(input('Masukan tinggi nya     : '))
    R = int(input('Masukan jari jari      : '))

    phi = 22/7
    luas = lambda KA,LA,T,R: 2 * phi * R * (R * T)
    volume = lambda KA,LA,T,R: phi * R * R * T

    print('Luas tabung   :',luas(KA,LA,T,R))
    print('Volume tabung :',volume(KA,LA,T,R))
tabung()