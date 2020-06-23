# teknik looping menggunakan tipe data struktur

nama_band = ['Payung Teduh',
             'Fourtwnty',
             'Dialog Dini Hari',
             'Mr. Sonjaya',
             'Parahyena',
             ]

kumpulan_lagu = ['Akad',
                 'Zona nyaman',
                 'Rumahku',
                 'Sang Filsuf',
                 'Sindoro',
                 ]

# enumerate
for i, band in enumerate(nama_band):
    print(i, " : ", band)

print(100*"=")

# zip
for band, lagu in zip(nama_band, kumpulan_lagu):
    print(band, "menyanyikan lagu yang berjudul :", lagu)

print(100*"=")

# set
playlist = {'yang terdalam', 'ada apa dengan mu',
            'jaran gorang', 'menghapus jejakmu', 'kucing', 'tikut', 'oray'}

for lagu in sorted(playlist):
    print(lagu)

print(100*"=")
# dictionary
playlist2 = {'Payung Teduh': "akad",
             'Fourtwnty': "Zona nyaman",
             'Dialog Dini Hari': 'Rumahku'
             }

for i, v in playlist2.items():
    print(i, "Lagunya :", v)

for i in reversed(range(1, 10, 1)):
    print(i)
