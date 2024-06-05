def function(): #tulisannya tidak harus function, function py untuk mempermudah dalam perintah
    print("saya makan")
    print("saya minum")
    print("saya tidur")
function()

def nama(name): #function parameter
    print("nama saya",name)
nama("fillah")
nama("ismy")

def method(name="None"): #function default parameter, "none" untuk biar jadi default biar ga error
    print("nama saya "+name)
method()

def fungsi(nama, umur, tinggi):
    print("nama saya",nama)
    print("umur saya",umur)
    print("tinggi saya",tinggi)
fungsi(umur=17, nama="ismy", tinggi=153.0) #buat dipemanggilan fungsinya juga ga harus urut

def fungsi(nama, umur, tinggi):
    print("nama saya",nama,"umur saya",umur,"tinggi saya",tinggi) #penulisan print ke samping
fungsi(umur=17, nama="ismy", tinggi=153.0)