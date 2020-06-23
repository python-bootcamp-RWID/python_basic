# parent class
class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ndaerah:',self.daerah)


# class turunan dari Ojek
class Gojek(Ojek):
    def cek_id_abang(self):
        print(self.nama, 'cek aplikasi gojek')


ojek1 = Ojek('mario','manual','bandung')
ojek2 = Gojek('danil','automatic','rancaekek')

ojek1.cek_id_abang()
ojek2.cek_id_abang()
