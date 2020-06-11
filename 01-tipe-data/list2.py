mylist = ['danil', 'haykal', 12, 212, 3.14, True]
print(mylist)

mylist[1] = 'fika' #mengubah data pada index ke 1
print(mylist)

print(100*"+")

a = [1,2,3,4,6,2]
b = [5,6,7,8]
print(a+b)

print(a * 3)

print(a[2])

print(a[1:3])

print(4 in a)
print(len(a))
print(max(a))
print(min(a))

# menambahkan data list
languages = ['Java','Python','C++']
languages.append('PHP')
languages.insert(1,'C#')
print(languages)

languages.remove('C++')
print(languages)

languages.reverse()
print(languages)

languages.sort()
print(languages)