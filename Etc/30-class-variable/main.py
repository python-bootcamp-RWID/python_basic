class mahasiswa():
    jurusan = 'ekonomi'

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim


otong = mahasiswa('otong surotong', 3216607)
ucup = mahasiswa('michael ucup', 32121212)

otong.jurusan = 'ekonomi mikro'
otong.matakuliah = 'pemrograman'
ucup.matakuliah = 'sejarah'

print(mahasiswa.jurusan)
print(otong.jurusan)
print(ucup.jurusan)
print(otong.matakuliah)

print(mahasiswa.__dict__)
print(otong.__dict__)
print(ucup.__dict__)
