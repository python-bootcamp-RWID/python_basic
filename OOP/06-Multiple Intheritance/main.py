class Team:
    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.team)

class Tipe_hero:
    def setTipe(self,tipe):
        self.tipe = tipe

    def showTipe(self):
        print(self.tipe)


class Hero(Team, Tipe_hero):
    def __init__(self,name,health):
        self.name = name
        self.health = health


Axe = Hero('Axe', 100)
Axe.setTeam("merah")
Axe.setTipe("Strength")
Axe.showTeam()
Axe.showTipe()