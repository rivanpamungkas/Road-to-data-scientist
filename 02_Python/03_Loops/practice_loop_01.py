angka = int(input('Masukkan Angka Anda : '))
angka1 = 1

for i in range (angka1, angka) :
    if i % 2 == 0 :
        print(f'{i} Adalah Angka Genap')
    else:
        print(f'{i} Adalah Angka Ganjil')
