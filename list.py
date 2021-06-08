mylist = []
mylist.append("a")
mylist.append(12)
mylist.append(20)
print(mylist)
print(len(mylist))

# [a, 12, 20]
# [0  1    2]

mylist[0]=10 #mengedit isi list
print(mylist)

a = int(input("masukkan data ke dalam mylist : "))
mylist.append(a)
print(mylist)