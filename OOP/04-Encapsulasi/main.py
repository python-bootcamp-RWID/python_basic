class Hero:
    def __init__(self, name, health, attackPower):
        # private variabel instansiasi
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getAttPower(self):
        return  self.__attackPower

    # setter
    def diserang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaibaru):
        self.__attackPower = nilaibaru


#     awal dari game
axe = Hero('Axe',100, 20)

# game berjalan
print(axe.getName())
print(axe.getHealth())
axe.diserang(30)
print('diserang')
print('sisa HP : ', axe.getHealth())
axe.setAttPower(120)
print('darah menjadi', axe.getAttPower())