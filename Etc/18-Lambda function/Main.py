# membuat anonymous function dengan lambda
def kali(n):
    return lambda a: a * n


mydoubler = kali(2)
mytripler = kali(3)

print(mydoubler(11))
print(mytripler(11))
