programming = ('java','python','c++','php','ruby','golang')
print(programming)
print(programming[1])
print(programming[-1])
print(type(programming))
print(programming[1:3])

p = list(programming)
p[2] = 'javascript'
p.append('kotlin')
pt = tuple(p)
print(pt)

print(100*'+')

t1 = (1,2,3,4,5)
t2 = ("a","b","c")

t3 = t1 + t2
print(t3)
print(t3[4])