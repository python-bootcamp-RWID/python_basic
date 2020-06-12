# for loop list
programming = ['Python','java','C#','C++']

for p in programming:
    print(f'programming: {p}')

print(100*'-')

mystring = 'python'
for i in mystring:
    print(i)

print(100*'-')

mylist2 = [1,2,3,4,5]
jml = 0
for j in mylist2:
    jml = jml + j

print(jml)

print(100*'-')

for p in programming:
    print(p)
    if p == 'java':
        break

print(100*'-')

for i in range(10):
    print(i)