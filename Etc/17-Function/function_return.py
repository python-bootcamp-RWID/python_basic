# fungsi dengan return value
def kuadrat(argument):
    total = argument ** 2
    return total


a = kuadrat(4)
print("kuadrat = ", a)

print(100*"=")

# fungsi dengan return value dan multiple argumen


def tambah(argument1, argument2):
    total = argument1 + argument2
    print(argument1, " + ", argument2, " = ", total)
    # return [total, 2, 54, 5]
    return total


def kali(argument1, argument2):
    total = argument1 * argument2
    print(argument1, "x", argument2, " = ", total)
    return total


# a = tambah(4, 2)
# print("tambah = ", a)
# print(type(a))
# print(a[2])

a = tambah(3, 2)
b = kali(2, a)
print(b)
