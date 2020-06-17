class Hero:
    def __init__(self, name, health, armor):
        # variabel public
        self.name = name
        # variable private objek
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name,self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,inputArmor):
        self.__armor = inputArmor

    @armor.deleter
    def armor(self):
        print('armor di delete')
        self.__armor = None

sniper = Hero('sniper',100,30)
print(sniper.info)
# print(sniper.__dict__)
sniper.name = 'dadang'
print(sniper.info)

print('getter dan setter untuk __armor')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)

print('delete armor')
del sniper.armor
print(sniper.__dict__)