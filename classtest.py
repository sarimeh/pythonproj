class Classtest:

    def __init__(self, person):
        self.person = person

    def namesetzen(self, name):
        self.person = name
        print("name " + name + " gesetzt")

    def nameausgeben(self):
        print("gebe aus: " + self.person)

memo = Classtest("Mehmet")
memo.nameausgeben()
