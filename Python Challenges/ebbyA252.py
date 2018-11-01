class character:

    def __init__(self,name,health,strength,defence):
        self.name = name
        self.health = health
        self.strength = strength
        self.defence = defence

    def attack(self,other):
        damage = int(10*(self.strength/other.defence))
        other.health -= damage
        print(self.name+" attacked "+other.name+"!")
        print("It did "+str(damage)+" damage!")

class mage(character):

    def __init__(self,name,health,mana,magic_atk,magic_def):
        self.name = name
        self.health = health
        self.strength = 5
        self.defence = 20
        self.mana = mana
        self.magic_atk = magic_atk
        self.magic_def = magic_def

    def attack(self,other):
        if type(other) == type(self):
            damage = int(10*(self.magic_atk/other.magic_def))
        else:
            damage = int(10*(self.magic_atk/other.defence/2))
        other.health -= damage
        print(self.name+" attacked "+other.name+"!")
        print("It did "+str(damage)+" damage!")



        
