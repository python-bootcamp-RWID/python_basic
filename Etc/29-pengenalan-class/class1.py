class Mahasiswa():
    __nilai = 0  # menggunakan __ artinya variabel private

    def __init__(self, input_nama, input_nim, input_jurusan):
        self.nama = input_nama  # public
        self.nim = input_nim  # public
        self.jurusan = input_jurusan  # public

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, 'dengan jurusan ', self.jurusan, 'tidak lulus')
        else:
            print(self.nama, 'dengan jurusan ', self.jurusan, 'lulus')


# main program
otong = Mahasiswa("otong suproto", 3216607, 'sistem informasi')
ucup = Mahasiswa('michael ucup', 3212121, 'teknik informatika')

otong.uts(33)
otong.uas(50)
otong.check_status()

ucup.uts(10)
ucup.uas(20)
ucup.check_status()

print(ucup.nama)
