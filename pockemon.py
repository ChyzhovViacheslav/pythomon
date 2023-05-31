class Pockemon:
    name = None
    hp = None
    attack = None
    defense = None

    def __init__(self, name, hp, attack, defense):
        self.set_pockemon(name, hp, attack, defense)

    def set_pockemon(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nAttack: {self.attack}\nDefence: {self.defense}\n"
