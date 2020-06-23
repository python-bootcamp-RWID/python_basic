# Stack / tumpukan = masuk di awal, keluar di akhir , contoh tumpukan buku
# Queues / antrian = masuk di awal ,  keluar di awal, contoh antrian di supermarket

# stack
tumpukan = [1, 2, 3, 4, 5, 6]
print('data sekarang', tumpukan)

# memasukan data baru
tumpukan.append(7)
print('data masuk :', 7)
print('data sekarang :', tumpukan)
tumpukan.append(8)
print('data masuk :', 8)
print('data sekarang :', tumpukan)

# keluar
out = tumpukan.pop()
print('data keluar :', out)
print('data sekarang :', tumpukan)
