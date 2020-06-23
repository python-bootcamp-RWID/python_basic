# operasi logika atau boolean
# not, or, and, xor

print("==== NOT ====")
a = True
c = not a
print("data a = ", a)
print("data c = ", c)

print("==== OR ====")
a = True
b = True
c = a or b
print(a," OR ", b, ' = ', c)

a = True
b = False
c = a or b
print(a," OR ", b, ' = ', c)

a = False
b = True
c = a or b
print(a," OR ", b, ' = ', c)

a = False
b = False
c = a or b
print(a," OR ", b, ' = ', c)

print("==== AND ====")
a = True
b = True
c = a and b
print(a," and ", b, ' = ', c)

a = True
b = False
c = a and b
print(a," and ", b, ' = ', c)

a = False
b = True
c = a and b
print(a," and ", b, ' = ', c)

a = False
b = False
c = a and b
print(a," and ", b, ' = ', c)

# XOR (akan true jika salah satu nilai true)
print("==== XOR ====")
a = True
b = True
c = a ^ b
print(a," XOR ", b, ' = ', c)

a = True
b = False
c = a ^ b
print(a," XOR ", b, ' = ', c)

a = False
b = True
c = a ^ b
print(a," XOR ", b, ' = ', c)

a = False
b = False
c = a ^ b
print(a," XOR ", b, ' = ', c)