class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"{self.name} dengan health : {self.health}")


class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name,100)
        super().showInfo()


class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().showInfo()

lina = Hero_intelligent('lina')
axe = Hero_strength('Axe')