# membuat gabungan area rentang dari angka

inputUser = float(
    input("Masukan Angka yang bernilai kurang dari 3 atau lebih besar dari 10 : "))
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("kurang dari 3 : ", isKurangDari)

# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 10 : ", isLebihDari)

# ++++++++3----------10++++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan : ", isCorrect)

# -------3++++++++++10--------
# kasus irisan
print("\n", 10*"=", "\n")
inputUser = float(
    input("Masukan Angka yang bernilai lebih dari 3 atau kurang dari 10 : "))

# -------3++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("Lebih dari 3 = ", isLebihDari)

# +++++++++++++10---------
isKurangDari = inputUser < 10
print("Kurang dari 10  = ", isKurangDari)

#  -----------3++++++++10----------
isCorrect = isKurangDari and isLebihDari
print("anda yang masukan: ", isCorrect)
