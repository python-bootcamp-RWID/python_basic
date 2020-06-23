# membuat function sederhana
def suaraAyam():
    print("kukuruyukkkk")


def hargaAyam():
    suaraAyam()
    print("harga ayam per 1 kg adalah Rp. 50.000")


# membuat fungsi dengan argument / parameter
def hargaTotalAyam(kg):
    suaraAyam()
    harga = 50000
    hargaTotal = kg * harga
    print("harga ", kg, "Kg ayam adalah ", hargaTotal)
    print(type(hargaTotal))


suaraAyam()
hargaTotalAyam(3)
hargaTotalAyam(1.5)
