# operasi komparasi
# setiap hasil dari operasi komparasi adalah boolean (true atau false)
# > : lebih besar
# < : kurang dari
# >= : lebih besar sama dengan
# <= : kurang dari sama dengan
# == : sama dengan
# != : tidak sama dengan
# is : adalah
# is not : bukan  

a = 4
b = 2
c = 4
# lebih besar >
print('===== lebih besar dari ( > ) =====')
hasil = a > 3
print(a, ">", 3, " = ", hasil)
hasil = b > 3
print(b, ">", 3, " = ", hasil)
hasil = b > 2
print(b, ">", 2, " = ", hasil)

# kurang dari <
print('===== kurang dari ( < ) =====')
hasil = a < 3
print(a, "<", 3, " = ", hasil)
hasil = b < 3
print(b, "<", 3, " = ", hasil)
hasil = b < 2
print(b, "<", 2, " = ", hasil)

# lebih besar sama dengan >=
print('===== lebih besar sama dengan ( >= ) =====')
hasil = a >= 3
print(a, ">=", 3, " = ", hasil)
hasil = b >= 3
print(b, ">=", 3, " = ", hasil)
hasil = b >= 2
print(b, ">=", 2, " = ", hasil)

# kurang dari sama dengan <=
print('===== kurang dari sama dengan( <= ) =====')
hasil = a <= 3
print(a, "<=", 3, " = ", hasil)
hasil = b <= 3
print(b, "<=", 3, " = ", hasil)
hasil = b <= 2
print(b, "<=", 2, " = ", hasil)

# sama dengan ==
print('===== sama dengan( == ) =====')
hasil = a == 4
print(a, "==", 4, " = ", hasil)
hasil = b == 3
print(b, "==", 3, " = ", hasil)
hasil = b == 2
print(b, "==", 2, " = ", hasil)

# tidak sama dengan !=
print('===== tidak sama dengan( != ) =====')
hasil = a != 4
print(a, "!=", 4, " = ", hasil)
hasil = b != 3
print(b, "!=", 3, " = ", hasil)
hasil = b != 2
print(b, "!=", 2, " = ", hasil)

# is sebagai komparasi (perbandingan) objek
# komparasi is tidak cocok untuk perbandingan dengan literal angka, harus dengan variable
x = 5 # ini adalah assigment membuat object
y = 5
print("===== object identity (is) ======")
print("nilai x = ", x, " id = ", hex(id(x)))
print("nilai y = ", y, " id = ", hex(id(y)))
hasil = x is y
print("x is y = ", hasil)

x = 5 # ini adalah assigment membuat object
y = 7
print("===== object identity (is) ======")
print("nilai x = ", x, " id = ", hex(id(x)))
print("nilai y = ", y, " id = ", hex(id(y)))
hasil = x is y
print("x is y = ", hasil)

x = 5 # ini adalah assigment membuat object
y = 7
print("===== object identity (is not) ======")
print("nilai x = ", x, " id = ", hex(id(x)))
print("nilai y = ", y, " id = ", hex(id(y)))
hasil = x is not y
print("x is not y = ", hasil)