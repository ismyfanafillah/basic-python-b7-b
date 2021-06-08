a = 70 #minimal ujian teori dan ujian praktek
b = float(input("masukkan nilai b : ")) #nilai ujian teori yang diperoleh
c = float(input("masukkan nilai c : ")) #nilai ujian praktek yang diperoleh
if b >= a <= c:
    print("Selamat, anda lulus!")
if b >= a > c:
    print("Anda harus mengulang ujian praktek.")
elif c >= a > b :
    print("Anda harus mengulang ujian teori.")
elif b < a > c:
    print("Anda harus mengulang ujian teori dan praktek.")