print("Selamat datang!")

print("--- Menu ---")
print("1. Daftar Kontak")
print("2. Tambah Kontak")
print("3. Keluar")

kontak = ["Nama : Blake","No. Telepon : 081522633231","Nama : Reece","No. Telepon : 082356913402","Nama : George","No. Telepon : 081364579231",] 

menu = int(input("Pilih menu : "))

if menu==1:
    print('Daftar kontak :')
    for x in kontak:
        print(x)
if menu==2:
    a = input("Nama : ")
    b = int(input("No. Telepon : "))
    c = "Nama : {}".format(a)
    d = "No. Telepon : {}".format(b)
    kontak.append(c)
    kontak.append(d)
    for x in kontak:
        print(x)
    print("Kontak berhasil ditambahkan")
elif menu==3:
    print("Program selesai, Sampai jumpa!")
elif menu!=1 and menu!=2 and menu!=3:
    print("Menu tidak tersedia")