print('='*30)
print('volume dan luas permukaan bola')
print('='*30)

def bola():
    PHI = 3.14
    r = float(input('masukkan jari jari bola\t\t: '))

    v = lambda r, PHI: (4/3) * PHI * r**3
    l = lambda r, PHI: 4 * PHI * r**2
    print(f'nilai volume bola adalah\t: ', v(r, PHI))
    print(f'niali luas permukaan adalah\t: ', l(r, PHI))
bola()
print('- '*20)
bola()