# input user
# data yang dimasukan pasti string
data = input("masukan nama :")
print("data = ", data, " type = ", type(data))

# jika kita ingin mengubah ke integer, float
angka1 = int(input("Masukan Nilai Pertama : "))
angka2 = int(input("Masukan Nilai Kedua : "))
jml = angka1 + angka2
print("penjumlahan dari ", angka1 , type(angka1), " + ", angka2, type(angka2), " = ", jml)

# float
n1 = float(input("masukan nilai : "))
n2 = float(input("masukan nilai : "))
jmlh = n1 + n2
print(n1, type(n1), " + ", n2, type(n2), " = ", jmlh)

# boolean , False jika nilai bernilai 0
biner = bool(int(input("masukan nilai boolean : ")))
print("data = ", biner, " , type = ", type(biner))
