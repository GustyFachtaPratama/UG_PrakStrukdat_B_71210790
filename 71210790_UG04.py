import json


karyawan = open('karyawan.json','a+') 
karyawan.seek(0) 
data = json.loads(karyawan.read())
karyawan_list = karyawan.readlines()
nama = dict()
l = []
n = int(input("Masukkan jumlah Karyawan baru: "))
for i in range(0,n):
    k = input('Masukkan nama anda: ')
    alamat = input("Masukkan alamat anda: ")
    h = int(input("Masukkan jumlah kolega : "))
    for j in range(1,h+1):
        kolega = (input(f"Masukkan kolega ke-{j}: "))
    print("=== Data berhasil ditambahkan ===")
karyawan.close()

# with open('karyawan.json', 'r') as datafile:
#         data = json.load(datafile)
#         data[nama] = l
# with open('karyawan.json', 'w') as datafile:
#         json.dump(data, datafile)
# print('=== Data berhasil ditambahkan ===\n')