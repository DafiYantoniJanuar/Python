print('=' * 55)
print('\tProgram Menghitung Energi Mekanik')
print('=' * 55)

energi_kinetik = float(input("Masukkan energi kinetik (Joule)\t\t: "))
energi_potensial = float(input("Masukkan energi potensial (Joule)\t: "))

energi_mekanik = energi_kinetik + energi_potensial

if energi_mekanik >= 100:
    energi_mekanik_kj = energi_mekanik / 1000
    print('Energi mekanik adalah\t\t\t: ',energi_mekanik_kj,' kiloJoule')
else:
    print('Energi mekanik adalah\t\t\t: ',energi_mekanik,' Joule')