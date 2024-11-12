def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Tidak bisa membagi dengan nol"
    return x / y

def calculator():
    print("Selamat datang di Kalkulator Sederhana!")
    print("Pilih operasi yang ingin Anda lakukan:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")

    # Memilih operasi
    choice = input("Masukkan pilihan (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            # Memasukkan angka
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            # Melakukan operasi berdasarkan pilihan
            if choice == '1':
                print(f"Hasil: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Hasil: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Hasil: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"Hasil: {num1} / {num2} = {divide(num1, num2)}")

        except ValueError:
            print("Error: Input harus berupa angka.")
    else:
        print("Pilihan tidak valid.")

# Menjalankan kalkulator
calculator()

   
