print('='*45)
print('\tHITUNGAN SELISIH WAKTU')
print('='*45)

jam_mulai = int(input("Masukkan jam mulai\t: "))
menit_mulai = int(input("Masukkan menit mulai\t: "))
jam_selesai = int(input("Masukkan jam selesai\t: "))
menit_selesai = int(input("Masukkan menit selesai\t: "))

if 0 <= jam_mulai < 24 and 0 <= menit_mulai < 60 and 0 <= jam_selesai < 24 and 0 <= menit_selesai < 60:
    total_menit_mulai = jam_mulai * 60 + menit_mulai
    total_menit_selesai = jam_selesai * 60 + menit_selesai
    selisih_menit = total_menit_selesai - total_menit_mulai
    jam_selisih = selisih_menit // 60
    menit_selisih = selisih_menit % 60
    jam_selisih_12 = jam_selisih % 12

    print(f"Selisih waktu\t\t: {jam_selisih_12} jam {menit_selisih} menit")
else:
    print("Input waktu tidak valid.")