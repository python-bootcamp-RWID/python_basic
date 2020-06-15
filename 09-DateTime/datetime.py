import time

ticks = time.time()
print("berjalan sejak ", ticks)

waktuSekarang = time.localtime(time.time())
tahun = waktuSekarang.tm_year
bulan = waktuSekarang.tm_mon
tanggal = waktuSekarang.tm_mday
jam = waktuSekarang.tm_hour
menit = waktuSekarang.tm_min
detik = waktuSekarang.tm_sec

print(f"Waktu local saat ini : tahun {tahun}, bulan {bulan}, tanggal {tanggal}")
print(f"Waktu Sekarang : {jam}:{menit}:{detik} ")

# mendapatkan waktu dengan berformat
localtime = time.asctime(time.localtime(time.time()))
print("waktu local saat ini ", localtime)