class Hero:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("sniper",100, 10, 4)
hero2 = Hero("mirana",100, 15, 1)
hero3 = Hero("ucup",1000, 100, 0)

print("atribut dari hero1 : ", hero1.__dict__)
print("atribut dari hero2  : ", hero2.__dict__)
print("atribut dari hero3 : ", hero3.__dict__)
