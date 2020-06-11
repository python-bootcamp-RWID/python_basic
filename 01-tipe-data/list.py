# belajar variabel dan tipe data
# tipe data sederhana
anak1 = 'danil'
anak2 = 'udin'
anak3 = 'emen'

# tipe data list/daftar/array
anak = ['Danil','Haykal','Fika']
print(anak)

# menambahkan data ke list
anak.append('icih')
print(anak)

# mengambil data anak ke 2
print(f'Hai {anak[1]}')

# memanggil semua data list dengan index
for a in range(0, len(anak)):
    print(f'hai ke-{a} : {anak[a]}')

# memanggil semua data list tanpa index
for a in anak:
    print(f'hai {a}')