# List sebagai iterable
gorengan = ['bahwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']

for g in gorengan:
    print(g)
    print(len(g))

# string sebagai iterable
bakwan = "bakwan"

for i in bakwan:
    print(i)

print(100*"=")

# for di dalam for
gorengan = ['bakwan', 'cireng', 'tahu isi', 'tempe goreng', 'ubi goreng']
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

daftar_belanja = [gorengan, buah, sayur]

for subDaftarBelanja in daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)
