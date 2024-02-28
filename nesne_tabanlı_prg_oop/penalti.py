import random
import time


class Team:
    def __init__(self, team_name, colors, footballers, score):
        self.team_name = team_name
        self.colors = colors
        self.footballers = footballers
        self.score = score

    @classmethod
    def scoreboard(cls, team1, team2):
        print(f"{team1.team_name} : {team1.score}")
        print(f"{team2.team_name} : {team2.score}")
        print("-------------------------------")


class Footballer:
    def __init__(self, name, uniform_no, hit_rate, team):
        self.name = name
        self.uniform_no = uniform_no
        self.hit_rate = hit_rate
        self.team = team
        team.footballers.append(self)

    def take_penalty(self):
        print(f"{self.name} penaltı kullanıyor", end="")
        for i in range(3):
            time.sleep(1)
            print(".", end="")
        print()
        goal_statu = random.randint(1, 100)
        if goal_statu <= self.hit_rate:
            print("Vurdu ve gol oldu")
            self.team.score += 1
        else:
            print("Vurdu ve kaçırdı")


# Takımlar
gs = Team("Galatasaray", ["Sarı", "Kırmızı"], [], 0)
fb = Team("Fenerbahçe", ["Sarı", "Lacivert"], [], 0)

# Futbolcular
arda = Footballer("Arda Kaya", 10, 60, gs)
emre = Footballer("Emre Kara", 9, 50, fb)

penalty_process = False

for i in range(10):
    if i % 2 == 0:
        arda.take_penalty()
    else:
        emre.take_penalty()
    arda.team.scoreboard(arda.team, emre.team)
    if arda.team.score == emre.team.score:
        penalty_process = True

while penalty_process:
    arda.take_penalty()
    emre.take_penalty()
    if arda.team.score == emre.team.score:
        penalty_process = True
    else:
        penalty_process = False

if arda.team.score > emre.team.score:
    print(f"{arda.team.team_name} WIN")
else:
    print(f"{emre.team.team_name} WIN")
print("Game Over")
