#  program konversi celcius ke satuan lain

print('\nProgram Konversi Temperatur\n')

celcius = float(input("Masukan Suhu Dalam Celcius : "))
print("Suhu adalah = ", celcius, " Celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, " reamur")

# fahrenheit
fahrenheit = ((9/5)* celcius) + 32
print("suhu dalam fahrenheit adalah ", fahrenheit, " Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ", kelvin, " Kelvin")
