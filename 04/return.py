def function(p,l): #untuk mengembalikan nilai ke dalam text atau fungsi
    luas = p*l
    text = "Luas persegi panjang adalah {}".format(luas)
    return text
print(function(20,10))

def function(p,l): 
    luas = p*l
    text = "Luas persegi panjang adalah {}".format(luas)
    return text
#input nilai sendiri
p = int(input("panjang: "))
l = int(input("lebar: "))
print(function(p,l))

def function(p,l): #untuk mengeluarkan nilai dari text atau fungsi, hasilnya tidak ada
    return
    luas = p*l
    text = "Luas persegi panjang adalah {}".format(luas)
    return text
print(function(20,10))

#return ga bisa digunakan diluar/selain fungsi