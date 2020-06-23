# ==== belajar variable dan tipe data primitif ====

angka = 10 #int
pecahan = 3.14 #float
nama = 'danil syah' #string
logic = True #bool

print(angka, " type = ", type(angka))
print(pecahan, " type = ", type(pecahan))
print(nama, " type = ", type(nama))
print(logic, " type = ", type(logic))

# assign multiple value
a,b,c = 1,2,3
print(a,c,b)

a,b,_ = 2,1,6
print(a,_,b)

a = b = c = 1
print(a,b,c)
b = 2
print(a,b,c)

x = y = [7, 8, 9]
x = [13, 8, 9]
print(y)

x = y = [7, 8, 9]
x[0] = 13
print(y)

x = [1, 2, [3, 4, 5], 6, 7] #this is nested list
print(x[2])
print(x[2][1])