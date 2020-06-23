nilai1 = 75
nilai2 = 80

# nesting if
if nilai1 == 75:
    print("nilai anda", nilai1)
    print("step 1")
    if nilai2 == 80:
        print("nilai anda", nilai2)
        print("step 2")

nilai = 50
if nilai == 75:  # equal eksplisit
    print("nilai anda :", nilai)

if nilai is 60:  # equal
    print("nilai anda :", nilai)

if nilai is not 60:  # not equal
    print("nilai anda bukan 60, tapi :", nilai)

print(40*"=")

nilai = 60
if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai <= 80:
    print("nilai anda adalah B")
elif 60 <= nilai <= 70:
    print("nilai anda adalah C")
elif 50 <= nilai <= 60:
    print("nilai anda adalah T, lakukan perbaikan")
else:
    print("maaf anda tidak lulus mata kuliah ini")

print(100*"+")
print("Operator Logika untuk List dan string")
print(" ")

gorengan = ["bakwan", "cireng", "gehu", "bala-bala", "tahu"]
beli = "bandros"

if beli in gorengan:
    print('Mamang bilang : " ya, saya jual, ', beli, ' "')

if not beli in gorengan:
    print('Mamang bilang, " waduh euy saya lagi ga jual ', beli, ' " ')

karakter = "z"
if karakter in beli:
    print("ada", karakter, "di ", beli)
else:
    print("tidak ada", karakter, "di ", beli)
