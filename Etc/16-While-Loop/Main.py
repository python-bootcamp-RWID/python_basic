
angka = 0
while angka < 10:
    print("nilai angka adalah : ", angka)
    angka += 1

print(100*"=")

start = True
angka = 0

while start:  # syarat menggunakan variable boolean
    print("ini didalam while")
    if angka is 100:
        start = False
        print("oke angka 100 ditemukan")
    angka += 1
