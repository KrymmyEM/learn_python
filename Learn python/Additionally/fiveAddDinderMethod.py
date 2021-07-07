lst = [1,2,3]

repr(lst) #Возращает строку в детальном виде

print(lst)

print( eval(repr(lst)) == lst )

class Charapter:
    def __init__(self, race, damage = 10):
        self.race = race
        self.damage = damage
        self.heath = 100



    def is_dead(self):
        return self.heath <= 0

    def __repr__(self):
        return f"Charapter('{self.race}', {self.damage}, {self.heath})"

    def __str__(self):
        return f"{self.race}: heath = {self.heath}, damage = {self.damage}"

c = Charapter('Elf')
print(c)
