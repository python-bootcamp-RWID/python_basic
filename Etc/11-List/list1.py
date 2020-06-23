Barang = ['kunci', 'ember', 'jaket', 'ban', 'mobil']
print(Barang)

# beberapa method yang bisa digunakan untuk memanipulasi list
# method untuk menambah data ke dalam list
Barang.append('sepeda')
print(Barang)

Barang.extend('dompet')
print(Barang)

Barang.insert(3, 'sepeda')
print(Barang)

# method untuk menghitung anggota
jumlahSepeda = Barang.count('sepeda')
print('Jumlah sepeda adalah : ', jumlahSepeda)

# remove data
Barang.remove('sepeda')
print(Barang)

# membalikan urutan elemen data
Barang.reverse()
print(Barang)

print(100*"=")

Stuff = Barang.copy()
Stuff.append('gelas')
print(Stuff)
print(Barang)
