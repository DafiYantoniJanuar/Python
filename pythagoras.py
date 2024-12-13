print('='*30)
print('pythagoras')
print('='*30)

def pythagoras():
    a = int(input('masukkan panjang sisi segitiga yang saling tegak lurus: '))
    b = int(input('masukkan panjang sisi segitiga yang saling tegak lurus: '))

    c = lambda a, b: a**2 + b**2
    print('panjang sisi miring adalah\t: ', c(a, b))

pythagoras()
print(' -'*20)
pythagoras()
print(' -'*20)