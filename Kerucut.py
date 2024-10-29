def kerucut():
    phi = 22/7
    r = int(input('Masukan jari jari nya:'))
    t = int(input('Masukan tinggi nya   :'))
    s = int(input('Masukan sisi nya     :'))

    volume = lambda  r,t,s: 1/3 * phi * phi * t
    lp = lambda r,t,s: phi * (r + s)
    
    print('Volume kerucut adalah :',volume(r,t,s))
    print('Luas permukaan kerucut:',lp(r,t,s))
kerucut()