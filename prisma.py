def prisma():
    la = int(input('Masukan luas alas nya     : '))
    ls = int(input('Masukan luas selimut nya  : '))

    lp = lambda la,ls: 2 * la * ls

    print('luas permukaan prisma :',lp(lp,ls))

prisma()