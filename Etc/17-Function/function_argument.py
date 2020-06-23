# fungsi dengan menggunakan argument sederhana
def siswa(nama):
    print('siswa ini bernama', nama)


siswa('danil')


# fungsi dengan menggunakan keyword arguments
def guru(nama, pelajaran):
    print('guru ini bernama', nama)
    print('mengajar', pelajaran)


guru(nama='rizki romdoni', pelajaran='pemrograman')
guru(pelajaran='struktur data', nama='heti')


# fungsi dengan menggunakan nilai default argument
def penjagaSekolah(nama, shift='siang', galak='tidak'):
    print('penjaga sekolah ini bernama :', nama)
    print('shiftnya ', shift)
    print('galak ?', galak)


penjagaSekolah('udin')
penjagaSekolah('emen', 'malam', 'sangat')
penjagaSekolah(shift='pagi', nama='mudhar', galak='baik')
