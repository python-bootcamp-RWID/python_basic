#  program konversi kelvin ke satuan lain

#  kelvin
print("\n==== PROGRAM KONVERSI KELVIN TO SATUAN LAIN ====\n")
kelvin = float(input("masukan nilai kelvin : "))
print("Kelvin adalah : ", kelvin, " Kelvin")

#  konversi ke fahrenheit
fahrenheit = 1.8 * (kelvin - 273) + 32
print("suhu dalam satuan fahrenheit adalah ", fahrenheit, "Fahrenheit")

