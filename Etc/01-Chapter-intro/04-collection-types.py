# ========== List =============
int_list = [1, 2, 3]
string_list = ['danil', 'syah']
empty_list = []
mixed_list = [1, 'abc', True, 2.34, None]
nested_list = [['a','b','c'], [1, 2, 3]]
print(int_list)
print(string_list)
print(empty_list)
print(mixed_list)
print(nested_list)

names = ['Danil','Khalinda','Fika','Haykal']
print(names[2])
print(names[1])
print(names[-1])
print(names[-3])
print(names)
names[0] = 'rizal'
print(names)

names.append("icih") # menambahkan data ke list ke akhir list
print(names)

names.insert(2, "udin") #menambahkan data ke list seusai index yang di inginkan
print(names)

names.remove("udin") # menghapus data list sesuai dengan object yang di input
print(names)
print("fika berada pada index ke ", names.index("Fika")) # get index dalam list sesuai object yang di input

# menghitung jumlah item yang sama dalam list
a = [1, 1, 1, 1, 3, 4, 2]
print(a)
print("jumlah 1 dalam list : ", a.count(1))
print(a[::-1]) #menampilkan list dari kanan

# menghapus data pada index trakhir dan mengembalikan index yang terhapus 
print(names)
print(names.pop())
print(names)

# menampilkan data list menggunakan for loop
for name in names:
    print(name)
print("================================")

# ============== Tuple =============
# value dari tuple ini tidak bisa di ubah
# biasanya di gunakan untuk ip address dan port nya
mhs = ('danil', 'fika','haykal')

for m in mhs:
    print(m.capitalize())
print("==================================")

# ============ Dictionaries / kamus ===========
# Kamus dalam Python adalah kumpulan pasangan nilai kunci. Kamus ini dikelilingi oleh kurung kurawal. 
# Setiap pasangan adalah dipisahkan oleh koma dan kunci dan nilai dipisahkan oleh titik dua. 

mahasiswa = {
    'nik' : '3216607',
    'nama' : 'danil syah',
    'jurusan' : 'sistem informasi',
    'email' : 'danilsyaharihardjo@gmail.com'
}
# get data nama
print(mahasiswa['nama'])

for k in mahasiswa.keys():
    print('{} mahasiswa : {}'.format(k, mahasiswa[k]))

print("=====================================")

# ====== Set ========
#  set hanya akan menampilkan data unik 
#  jadi ketika ada data yang sama , maka hanya 1 data yang ditampilkan

first_names = {'Fika','Haykal','Danil','Danil', 'Haykal'}
print(first_names)




