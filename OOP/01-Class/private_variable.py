class Hero:

    # class variable
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

        # variable instance private
        self.__color = 'red'

        # variable instance protected
        self._hair = 'kribo'

    # untuk mengakses atribut variabel private dan protected
    def getColor(self):
        return self.__color

    def getHair(self):
        return self._hair


lina = Hero('lina',100)
print(lina.__dict__)
print(Hero.__dict__)
print(lina.name)
print(lina.health)
print(lina.getColor())
print(lina.getHair())
print(Hero.__privateJumlah) #error