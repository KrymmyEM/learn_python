import pickle

class Charapter:
    def __init__(self, race,armor = 10 , damage = 10):
        self.race = race
        self.armor = armor
        self.damage = damage
        self.heath = 100

    def hit(self,damage):
        self.heath -=damage

    def is_dead(self):
        return self.heath <= 0

    #def __getstate__(self):

    def __setstate__(self, state):
        self.race = state.get('race', 'Orck')
        self.damage = state.get('damage', 20)
        self.armor = state.get('armor', 50)
        self.heath = state.get('heath', 100)

c = Charapter("Elf")
c.hit(10)
print(c.heath)

with open(r'game_state.bin', 'rb') as file:
    c = pickle.load(file)

    print(c.heath)

print(c.__dict__)
