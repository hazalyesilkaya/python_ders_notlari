import random


class Fighter:
    energy = 100
    score = 0

    def __init__(self, name, punch_power, kick_power, super_power):
        self.name = name
        self.punch_power = punch_power
        self.kick_power = kick_power
        self.super_power = super_power

    def get_energy(self):
        print(f"{self.name}{' ' * (10-len(self.name))} {'|' * self.energy}")

    def punch(self, defender):
        print(f"{self.name}, {defender.name} isimli oyuncuya yumruk attı")
        defender.energy -= self.punch_power
        self.get_energy()
        defender.get_energy()

    def kick(self, defender):
        print(f"{self.name}, {defender.name} isimli oyuncuya tekme attı")
        defender.energy -= self.kick_power
        self.get_energy()
        defender.get_energy()

    def super(self, defender):
        print(f"{self.name}, {defender.name} isimli oyuncuya tekme attı")
        defender.energy -= self.super_power
        self.get_energy()
        defender.get_energy()

    @staticmethod
    def game(attacker, defender, attack_type):
        if attack_type == 1:
            attacker.punch(defender)
        elif attack_type == 2:
            attacker.kick(defender)
        elif attack_type == 3:
            attacker.super(defender)
        else:
            print("Geçersiz Hamle")


fighters = []
attack_type = ["Punch", "Kick", "Super"]
fighter_names = ["ken", "ryu", "chunli", "dalsim", "blanka", "guila", "honnda", "sagat", "zangief"]
for i in range(len(fighter_names)):
    fighter = Fighter(fighter_names[i], random.randint(2, 5), random.randint(5, 8), random.randint(8, 10))
    fighters.append(fighter)

# ken = Fighter("Competitor1", 6, 8, 10)
# ryu = Fighter("Competitor2", 6, 8, 10)
#
# # # competitor1.energy = competitor1.energy - 10
# # competitor1.get_energy()
# # # competitor2.energy = competitor2.energy + 10
# # competitor2.get_energy()
#
# ken.punch(ryu)
# ken.kick(ryu)
# ken.super(ryu)
# # print(competitor1.energy)
# # print(competitor2.energy)
validation = True
while validation:
    try:
        for i in fighters:
            print(f"{fighters.index(i) + 1}.{i.name}")
        choose_fighter_no = int(input("Choose Fighter: "))
        choose_fighter = fighters[choose_fighter_no - 1]
        validation = False
    except:
        print("Invalid Selection!")

# rastgele rakip atama

player2 = fighters[random.randint(0, len(fighters) - 1)]

while fighter == player2:
    player2 = fighters[random.randint(0, len(fighters) - 1)]

print(f"{fighter.name} * {player2.name}")

while True:
    r = random.randint(1, 2)
    if r == 1:
        attacker = fighter
        defender = player2
        for i in attack_type:
            print(f"{attack_type.index(i) + 1}.{i}")
        attack = int(input("Choose attack type: "))
    elif r == 2:
        attacker = player2
        defender = fighter
        attack = random.randint(1, 3)

    Fighter.game(attacker, defender, attack)

    fighter.get_energy()
    player2.get_energy()
    if defender.energy <= 0:
        print("Game Over!")
        print(f"{attacker.name} Won!")
        break

# @instancemethod -> nesleler üzerinde çağırılırlar.
# @ classmethod _> class adı ile çağırılırlar.
# @staticmethod _> nesne veya class adı ile çağırılırlar.