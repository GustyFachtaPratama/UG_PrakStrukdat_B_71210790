
def kalkulator():
    a = True
    while a:
        iUser = input("Masukkan Pilihan Anda: ")
        
        if iUser == "1":
            bilangan1 = int(input("Masukkan bilangan: "))
            bilangan2 = int(input("Masukkan bilangan: "))
            hasil = bilangan1 + bilangan2
            print("Hasil nya adalah: %d"%hasil)
        elif iUser == "2":
            bilangan1 = int(input("Masukkan bilangan: "))
            bilangan2 = int(input("Masukkan bilangan: "))
            hasil = bilangan1 - bilangan2
            print("Hasil nya adalah: %d"%hasil)
        elif iUser == "3":
            bilangan1 = int(input("Masukkan bilangan: "))
            bilangan2 = int(input("Masukkan bilangan: "))
            hasil = bilangan1 * bilangan2
            print("Hasil nya adalah: %d"%hasil)
        elif iUser == "4":
            bilangan1 = int(input("Masukkan bilangan: "))
            bilangan2 = int(input("Masukkan bilangan: "))
            hasil = bilangan1 / bilangan2
            print("Hasil nya adalah: %d"%hasil)
        elif iUser == "q":
            print("Jika ingin menghentikan program 'q' harus Huruf kapital")
        elif iUser == "Q":
            break
        else :
            print("Pilihan yang anda masukkan tidak ada di menu!")
        
   
   
    

print("Kalkulator Sederhana Python\n")
print("1. Penjumlahan\n")
print("2. Pengurangan\n")
print("3. Perkalian\n")
print("4. Pembagian\n")
print("Ketik 'Q' jika ingin menghentikan program\n")


kalkulator()
