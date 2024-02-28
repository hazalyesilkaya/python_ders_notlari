import random
import time

class Archer():
    def __init__(self,name,power,point = 0):
        self.name = name
        self.power = power
        self.point = point

    def pointer(self):
        print(f"{self.name}{' ' * (15 - len(self.name))} : {self.point} puan.")

    def game(self):
        #x = random.randint(1,4)
        x = random.randint(1,self.power) + random.randint(1,self.power) + random.randint(1,10)
        if(x >= 20):
            x = 20
        else:
            pass
        self.point += x
        self.pointer()

    def clear_point(self):
        self.point = 0


players = []
last4player = []
final = []
loser = []

players.append(Archer("Ashe",8))
players.append(Archer("Robin Hood",8))
players.append(Archer("Tarzan",8))
players.append(Archer("Mete Gazoz",9))
players.append(Archer("Katniss",6))
players.append(Archer("Okçu6",6))
players.append(Archer("Okçu7",6))
players.append(Archer("Okçu8",6))

i = 1


while(len(players) > 0):

    player1 = random.choice(players)
    players.remove(player1)
    player2 = random.choice(players)
    players.remove(player2)
    print(f"{i}.MAÇ : {player1.name} VS {player2.name} \n")
    i += 1
    for _ in range(3):
        player1.game()
        player2.game()
        time.sleep(1)
    while(player1.point == player2.point):
        player1.game()
        player2.game()
        time.sleep(1)
    print(f"Maç Sonucu : {player1.name} => {player1.point} VS {player2.name} => {player2.point}")
    if (player1.point > player2.point):
        last4player.append(player1)
        print(f"KAZANAN : {player1.name}")
    else:
        last4player.append(player2)
        print(f"KAZANAN : {player2.name}")
    if i < 5:
        print("Diğer maça geçiliyor.\n")
    time.sleep(3)

for i in range(len(last4player)):
    last4player[i].clear_point()

print(f"Yarı finale kalan oyuncular : {last4player[0].name},{last4player[1].name},{last4player[2].name},{last4player[3].name}.")
time.sleep(3)
print("Yarı final başlıyor!")

i = 1
while(len(last4player) > 0):
    player1 = random.choice(last4player)
    last4player.remove(player1)
    player2 = random.choice(last4player)
    last4player.remove(player2)
    print(f"Yarı finalde {i}.MAÇ : {player1.name} VS {player2.name} \n")
    i += 1
    for _ in range(3):
        player1.game()
        player2.game()
        time.sleep(1)
    while(player1.point == player2.point):
        player1.game()
        player2.game()
        time.sleep(1)
    print(f"Maç Sonucu : {player1.name} => {player1.point} VS {player2.name} => {player2.point}")
    if (player1.point > player2.point):
        final.append(player1)
        loser.append(player2)
        print(f"KAZANAN : {player1.name}")
    else:
        final.append(player2)
        loser.append(player1)
        print(f"KAZANAN : {player2.name}")
    if i < 3:
        print("Diğer maça geçiliyor.\n")
    #Total maç sayısını biliyosun, onu kullanarak son maçtan sonra yazmasını engellle.
    time.sleep(3)

for i in range(len(final)):
    final[i].clear_point()

for i in range(len(loser)):
    loser[i].clear_point()

print(f"Finale kalan oyuncular : {final[0].name} ve {final[1].name}")
time.sleep(3)
print("\nÜçüncülük mücadelesi başlamak üzere!\n")

for i in range(3):
    loser[0].game()
    loser[1].game()
    time.sleep(1)
while (loser[0].point == loser[1].point):
    loser[0].game()
    loser[1].game()
    time.sleep(1)
if (loser[0].point > loser[1].point):
    print(f"ÜÇÜNCÜ : {loser[0].name}")
else:
    print(f"ÜÇÜNCÜ : {loser[1].name}")

print(f"\nFİNAL MÜCADELESİ : {final[0].name} VS {final[1].name}")

for i in range(3):
    final[0].game()
    final[1].game()
    time.sleep(1)
while (final[0].point == final[1].point):
    final[0].game()
    final[1].game()
    time.sleep(1)
if (final[0].point > final[1].point):
    print(f"ŞAMPİYON {final[0].name.upper()}!!!!!!!")
else:
    print(f"ŞAMPİYON {final[1].name.upper()}!!!!!!!")



