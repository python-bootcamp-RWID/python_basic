class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim
        mahasiswa.jumlah_mahasiswa += 1


otong = mahasiswa('otong surotong', 321212121)
ucup = mahasiswa('michael ucup', 32323223)
danil = mahasiswa('danil', 32323223)

print(mahasiswa.jumlah_mahasiswa)
