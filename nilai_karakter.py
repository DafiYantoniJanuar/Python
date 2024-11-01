'''Menentukan kelulusan dari 4 kritea berikut: 
Lulus apabila :
Nilai karakter A atau B
Nilai Matematika minimal 60
Nilai B. Indonesia minimal 70
Nilai B. Inggris minimal 55
'''
Nilai_karakter =input("Masukan Nilai A atau B: ").lower()
Nilai_matematika =int(input("Masukan Nilai Matematika minimal 60 : "))
Nilai_B_Indonesia = int(input("Masukan Nilai B Indonesia minimal 70 : "))
Nilai_B_Inggris = int(input("Masukan Nilai B Inggris minimal 55 : "))

if Nilai_karakter == 'A' or Nilai_karakter == 'B' and Nilai_matematika >= 60 and Nilai_B_Indonesia >= 70 and Nilai_B_Inggris >= 55:
    print('Lulus')
else:
    print('Tidak Lulus')


