# scope variabel : global

namaKucing = 'cassandra'
makananKucing = 'royal canin'


def rubahNamaKucing(namaBaru):
    namaKucing = namaBaru  # variabel local
    print('saya rubah nama kucing menjadi ', namaKucing)


def kasihMakanKucing(makanan, nama):
    global makananKucing, namaKucing  # variabel global
    makananKucing = makanan
    namaKucing = nama


rubahNamaKucing('ketie')
kasihMakanKucing('universal', 'alex')
print('nama kucing saya menjadi ', namaKucing, 'dan makanan ', makananKucing)
