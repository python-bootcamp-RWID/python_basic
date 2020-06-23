class Buku:
    def __init__(self, nama, pengarang, harga = 5000):
        self.nama = nama
        self.pengarang = pengarang
        self.harga = harga

    def __str__(self):
        return f'nama buku = {self.nama}, pengarang = {self.pengarang}, harga = {self.harga}'


daftar_buku = []
daftar_buku.append(Buku('7 keajaiban rejeki','ippo santoso'))
daftar_buku.append(Buku('Pemrograman dasar python','budi rahardjo'))
daftar_buku.append(Buku('Buku Flutter','uda coding'))





# daftar_buku.append("Naruto shiphuden")
# daftar_buku.append("7 keajaiban rejeki")
# daftar_buku.append("buku pemrograman python")