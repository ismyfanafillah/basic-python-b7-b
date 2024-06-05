class hewan: #penggunaan class
    def __init__(self, kaki, gigi, makanan): #harus ada self
        self.kaki = kaki #untuk atribut yang ada co:kaki,gigi,dsb
        self.gigi = gigi
        self.makanan = makanan

tiger = hewan(4, "punya taring", "daging") #variable object, dan diurutkan sesuai penulisan atribut
kancil = hewan(4, "tidak punya taring", "tumbuhan")
print(tiger.gigi) #pemanggilan satu satu tiap atribut
print(tiger.kaki)