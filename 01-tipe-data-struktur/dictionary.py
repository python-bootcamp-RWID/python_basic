"""
belajar tipe data dictionary
- tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
- KVP = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'ayah': 'father', 'istri': 'wife', 'ibu': 'mother'}

print(kamus_ind_eng)

# cara memanggil data
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

# menampilkan daftar member
print(kamus_ind_eng.values())

# menampilkan daftar key
print(kamus_ind_eng.keys())

# menampilkan jumlah data
print(len(kamus_ind_eng))

print('+' * 100)

print('-Data Gojek-')
data_dari_server_gojek = {
    'tanggal': '2020-06-11',
    'driver_list': [
        {'nama': 'danil', 'jarak': 10},
        {'nama': 'haykal', 'jarak': 30},
        {'nama': 'fika', 'jarak': 40},
        {'nama': 'razil', 'jarak': 100}
    ]
}
print(data_dari_server_gojek)
print(f"Driver disekitar sini {data_dari_server_gojek['driver_list']}")
print('\n')
print(f"Driver pertama  {data_dari_server_gojek['driver_list'][0]}")
print(f"Jarak Driver pertama  {data_dari_server_gojek['driver_list'][0]['jarak']} meter")

