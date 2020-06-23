# belajar List / array

ngaran = "danil"

daftar_nama = ["saya", "aku", "I", "myself"]
print(daftar_nama)

daftar_nama.append("abdi")
daftar_nama.append("aing")

print(daftar_nama)

#nama merupakan variabel iterasi pengulangan
for nama in daftar_nama:
    print("Nama lain anda adalah %s, padahal nama aslimu itu %s lho !" % (nama, ngaran) )