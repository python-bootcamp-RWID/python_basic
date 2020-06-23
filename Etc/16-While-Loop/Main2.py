# else, break, continue, pass

angka = 0

while angka < 10:

    if angka is 5:
        print("checkpoint")
        angka += 1
        continue
        # break
        # pass

    print("nilai angka adalah ", angka)
    angka += 1
else:
    print('nilai angka terakhir adalah ', angka)

print("di luar while")
