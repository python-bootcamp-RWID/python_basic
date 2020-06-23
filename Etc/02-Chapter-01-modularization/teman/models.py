class Teman:
    # atribute class
    jumlah = 0

    def __init__(self, nama, sex, alamat = "tidak ada"):
        self.nama = nama
        self.sex = sex
        self.alamat = alamat
        Teman.jumlah += 1

    def __str__(self):
        return f'Nama = {self.nama} , sex = {self.sex}, alamat = {self.alamat}'

    def berbicara(self):
        print(f'Hi, nama saya {self.nama}. apa kabar kamu hari ini ?')



daftar_temans = []

daftar_temans.append(Teman('danil','laki-laki'))
daftar_temans.append(Teman('haykal','Laki-laki'))
daftar_temans.append(Teman('fika','Wanita'))

udin = Teman('udin','laki-laki')
udin.alamat = 'jalan perum telaga surya blok f.44'
udin.berbicara()
daftar_temans.append(udin)

print("jumlah teman dengan fungsi len = ", len(daftar_temans))
print("jumlah teman dengan atribut JUMLAH dari class Teman = ", Teman.jumlah)

