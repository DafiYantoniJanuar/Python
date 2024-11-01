jumlah = 0
for g in range(1,6):
    if g < 5:
        print(g, end=' + ')
    else:
        print(g, end=' = ')
    jumlah = jumlah + (g)
print(jumlah)