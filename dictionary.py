d = {
    "nama" : "Ismy",
    "umur" : "17",
    "tinggi" : "153.0",
    #key       #value
}
print(d["nama"]) 
print(d["umur"])
print(d)
d["nama"]="Fana" #change value
print(d)

#for x in d:
    #print(d)

d = []

for i in range(1):
    nama = input("masukkan nama anda : ")
    umur = int(input("masukkan umur anda : "))
    tinggi = float(input("masukan tinggi anda : "))
    data = {
        "nama" : nama,
        "umur" : umur,
        "tinggi" : tinggi,  
    }
    d.append(data)
for i in d:
    print("nama pelanggan : ",i["nama"])
    print("umur pelanggan : ",i["umur"])
    print("tinggi pelanggan : ",i["tinggi"])