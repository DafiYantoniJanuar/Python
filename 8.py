jumlah= 0
for b in range(2,11,2):
    if b < 10:
        print(b,end=' + ')
    else:
        print(b,end=' = ')
    jumlah= jumlah + b
print(jumlah)