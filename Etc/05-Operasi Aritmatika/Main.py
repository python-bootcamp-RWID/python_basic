#  operasi aritmatika

a = 5
b = 2

# operasi tambah +
hasil = a + b
print(a, " + ", b, " = ", hasil)

# operasi kurang -
hasil = a - b
print(a, " - ", b, " = ", hasil)

#operasi kali *
hasil = a * b
print(a, " * ", b, " = ", hasil)

#operasi bagi
hasil = a / b
print(a, " / ", b, " = ", hasil)

# operasi modulus / sisa bagi
hasil = a % b
print(a, " % ", b, " = ", hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, '**', b, " = ", hasil)

# operasi floor division //
hasil = a // b
print(a, ' // ', b, ' = ', hasil)

#  prioritas operasi , operasional precendence
'''
    KuKaBaTaKu = Kurung, Kali, Bagi, Tambah, Kurang
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, '**',y,'*','(',z,'+',x,')','/',y,'-',y,'%',z,'//',x, ' = ', hasil)

hasil = x + y * z
print(x,'+',y,'*',z,' = ',hasil)

hasil = (x + y) * z
print('(',x,'+',y,')','*',z,' = ', hasil)


