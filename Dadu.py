import random

def dadu():
    list_barang=["Gayung", "Kursi", "Piring", "Mangkuk", "Karpet", "Casing HP","Handphone"]
    
    lemparan_dadu=random.randint(1, 6)
    print(f"Dadu Nya Adalah \t: {lemparan_dadu}")
    
    hadiah=random.randint(5000, 10000)
    barang_random=random.choice(list_barang)

    if lemparan_dadu == 3:
        print(f"Anda Mendapat Hadiah \t: ${hadiah}")
    else:
        print(f"Anda Mendapatkan \t: {barang_random}")

dadu()
