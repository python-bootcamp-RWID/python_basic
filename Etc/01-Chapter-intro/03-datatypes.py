# belajar tipe data

# beberapa jenis tipe data
#  1. numbers : 
#  int
angka = 10
print(angka ,"type = ", type(angka))

# float
pecahan = 3.14
print(pecahan, "type = ", type(pecahan))

# complex
a = 2 + 1j
print(a, " type = ", type(a))

# string
nama_depan = "danil"
nama_belakang = "syah arihardjo"
full_name = nama_depan + " "+ nama_belakang
print(full_name, "type = ", type(full_name))

i = "3"
print(isinstance(i, int))
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    print("type :", type(i))
    i = int(i)
    i += 1
print(i)

#  konversi type data
# int
a = '123'
b = int(a)
print(a, "type = ", type(a), "konversi ke ", type(b))

# float
a = '123.1234'
b = float(a)
print(a, "type = ", type(a), "konversi ke ", type(b))

#  konversi ke list, set, tuple
a = 'hello'
print(list(a))
print(set(a))
print(tuple(a))

# mutable : tipe data variabel yang bisa di ubah : 
    # int, long, float, complex, str, bytes, tuple, frozenset

# immutable : tipe data variable yang tidak bisa di ubah:
    # bytearray, list, set, dict

def test(m):
    m.append(3) #menambahkan number ke list
    m.append(5)
    return m
x = [1, 2]
print(test(x))

