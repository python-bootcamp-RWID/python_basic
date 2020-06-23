# continue : fungsinya untuk melanjutkan ke step berikutnya
# break : fungsinya untuk mengakhiri for (terminasi)
# pass : hanya untuk konstruksi , dummy if, function

for i in range(1, 10):
    if i is 6:
        print("nilai i adalah", 6)
        # pass
        # break
        continue

    print("nilai saat ini adalah ", i)
else:
    print("akhir dari loop")

print("print diluar loop")
