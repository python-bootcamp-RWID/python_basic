inputUser = float(
    input("Masukan Angka lebih besar dari 0 dan lebih kecil dari 5 : "))

lebihBesarDari0 = inputUser > 0
lebihKecilDari5 = inputUser < 5
isCorrect1 = lebihBesarDari0 and lebihKecilDari5

print("Lebih Besar Dari 0 : ", lebihBesarDari0)
print("Lebih Kecil dari 5 : ", lebihKecilDari5)
print("angka yang anda masukan : ", isCorrect1)

inputUser2 = float(
    input("Masukan Angka Lebih besar dari 8 dan lebih kecil dari 11 : "))

lebihBesarDari8 = inputUser2 > 8
lebihKecilDari11 = inputUser2 < 11
isCorrect2 = lebihBesarDari8 and lebihKecilDari11
print("Lebih Besar dari 8 : ", lebihBesarDari8)
print("lebih kecil dari 11 : ", lebihKecilDari11)
print("angka yang anda masukan : ", isCorrect2)

hasilPerbandinganLogika = isCorrect1 or isCorrect2
print("hasil penggabungan logika : ", hasilPerbandinganLogika)
