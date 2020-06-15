def hello(nama):
    print(f'hello world {nama}')

hello("danil")
hello("haykal")
hello("fika")

def tambah(a,b):
    print(a + b)

tambah(10,12)

def print_name(name="danil"):
    print("hello ", name)

print_name('udin')

def add(a,b):
    return a+b

s = add(2,5)
print(s)

print(100*"-")

def pro(programming):
    for p in range(0,len(programming)):
        print(p, 'pemrograman : ', programming[p])


prog = ['python','java','php','c++','javascript']
pro(prog)