r = int(input("berapa panjang jari-jari ?: "))
p = 22/7 #nilai (phi)
luas = (p*r*r) #luas lingkaran
txt = "Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2".format(r,luas)
print(txt)