# input nilai lebih kecil dari 0 atau lebih besar dari 5
inputUser1 = float(
    input("Masukan nilai lebih kecil dari 0 atau lebih besar dari 5 = "))
lebihKecilDari0 = inputUser1 < 0
print("Lebih Kecil Dari 0 : ", lebihKecilDari0)

lebihBesarDari5 = inputUser1 > 5
print("Lebih Besar Dari 5 : ", lebihBesarDari5)

isCorrect = lebihKecilDari0 or lebihBesarDari5
print("Hasil Dari Perbandingan Logika : ", isCorrect)

print("\n", 10*"=", "\n")

# masukan nilai lebih kecil dari 8 atau lebih besar dari 11

inputUser2 = float(
    input("Masukan nilai lebih kecil dari 8 atau lebih besar dari 11 : "))
lebihKecilDari8 = inputUser2 < 8
print("Lebih Kecil Dari 8 : ", lebihKecilDari8)
lebihBesarDari11 = inputUser2 > 11
print("Lebih Besar Dari 11 : ", lebihBesarDari11)
isCorrect2 = lebihKecilDari8 or lebihBesarDari11
print("Hasil perbandingan logika : ", isCorrect2)

hasilPerbandingan = isCorrect and isCorrect2
print("hasil perbadingan : ", hasilPerbandingan)
