class mahasiswa():
  # atribute / properti
    nama = 'nama'

# method
    def belajar(self, kondisi):
        print(self.nama, 'sedang belajar', kondisi)

    def tidur(self, kondisi):
        print(self.nama, 'tidur dikelas', kondisi)

    def berhitung(self, nilai1, nilai2):
        print(self.nama, 'melakukan perhitungan')
        return nilai1 + nilai2



otong = mahasiswa()
ucup = mahasiswa()

otong.nama = 'otong surotong'
ucup.nama = 'michael ucup'

otong.belajar('dengan giat')
ucup.tidur('dengan pulas')

print(otong.berhitung(10, 5))
