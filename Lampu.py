statuslampu = input("Status Lampu : ")
warnalampu = input("Masukan warna lampu lalu lintas : ")

if statuslampu == 'menyala':
  if warnalampu == 'merah':
    print('Berhenti!')
  elif warnalampu == 'kuning':
    print("Bersiap!")
  elif warnalampu == 'hijau':
    print("Maju!")
  else:
    print("Warna salah!")
else:
   print('Jalan!')

