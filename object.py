class person:
    def __init__(self, input_nama, input_umur, input_tinggi, input_hobi): #memasukkan atribut apa aja
        self.nama = input_nama #bisa ada tulisan input bisa engga juga
        self.umur = input_umur
        self.tinggi = input_tinggi
        self.hobi = input_hobi
    def greet(self):
        print("Nama saya adalah",self.nama,"saya saat ini berumur",self.umur,"saya saat ini memiliki tinggi",self.tinggi,"cm")

user = person("ismy", 17, 153.0, "membaca buku") #harus urut dan ada semua
user.greet() #menggunakan data tyang sudah ada di user