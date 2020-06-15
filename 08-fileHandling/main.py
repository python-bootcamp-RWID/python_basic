# f = open('file.txt', 'w')
# f.write('welcome to python full course for beginner')
# f.write('\nkeep spirit and keep focus')
# f.close()


# f = open('file.txt', 'r')
# print(f.read())
# print(f.read(10))
# print(f.readline())
# f.close()

# for x in f:
#     print(x)

f = open("file.txt", "a")
f.write("\nini paragraf tambahan")
f.close()

f = open("file.txt", "r")
print(f.read())

