programming = {"python","java","C++"}

print(type(programming))
print(programming)

programming.add("PHP")
print(programming)

programming.remove("C++")
print(programming)

print(100*"+")

programming2 = {2,3,4,5}

# menggabungkan 2 set
s3 = programming.union(programming2)
print(s3)

programming.update(programming2)
print(programming)