# atıcı, robinhood, akıncı, tarcan, .....
# performans parametresi de olsun.
import os
import random
import time


class Archer:
    def __init__(self, archer_name, accuracy_arrow_hit):
        self.archer_name = archer_name
        self.accuracy_arrow_hit = accuracy_arrow_hit
        self.arrow_targeted_number = 0
        self.total_hit_count = 0

    def arrow_target(self):
        # Performansa göre isabet olasılığını kontrol etme???
        if random.random() < self.accuracy_arrow_hit:
            self.arrow_targeted_number = round((random.randint(0, 20) * 10 / 100) * self.accuracy_arrow_hit / 10)
        else:
            self.arrow_targeted_number = 0

    def sum_targets(self):
        # self.total_hit_count += self.arrow_targeted_number
        return self.total_hit_count


class ArrowGame:
    def __init__(self, archers):
        self.archers = archers

    def arrow_game(self):
        for archer in self.archers:
            archer.arrow_target()
            archer.total_hit_count += archer.arrow_targeted_number
            if archer.arrow_targeted_number != 0:
                print(f"{archer.archer_name} {archer.arrow_targeted_number} sayısına isabet ettirdi.")
                print(f"Toplam Puan: {archer.sum_targets()}")
            else:
                print(f"{archer.archer_name} isabet ettiremedi.")
                print(f"Toplam Puan: {archer.sum_targets()}")
            time.sleep(1)


legolas = Archer("Legolas", 50)
katniss = Archer("Katniss", 70)
robinhood = Archer("Robinhood", 90)
susan_pevensie = Archer("Susan Pevensie", 80)
tauriel = Archer("Tauriel", 75)
oliver_queen = Archer("Oliver Queen", 85)

players = [legolas, katniss, robinhood, susan_pevensie, tauriel, oliver_queen]


player1 = random.choice(players)
players.remove(player1)
player2 = random.choice(players)
players.remove(player2)
player3 = random.choice(players)
players.remove(player3)
player4 = random.choice(players)
players.remove(player4)
player5 = random.choice(players)

there_selected_players = [player1, player2, player3]
four_selected_players = [player1, player2, player3, player4]
five_selected_players = [player1, player2, player3, player4, player5]


def run_game(select_players_list):
    player_number = len(select_players_list)
    default_number = 0
    seperator_line = "====================================="
    print(seperator_line)
    # examples = ArrowGame(select_players_list)
    while default_number < player_number:
        # examples.arrow_game()
        ArrowGame(select_players_list).arrow_game()
        print(seperator_line)
        default_number += 1
    # scores = []
    for player in select_players_list:
        # scores.append(player.sum_targets())
        max_score = max(player.sum_targets())
        if player.sum_targets() == max_score:
            winner = player
            if winner:
                print(f"{winner.archer_name} kazandı!")
                print(f"Toplam puan: {winner.sum_targets()}")
            else:
                print("Berabere bitmiştir.")


def choose_number_of_players():
    print("""
    Oyun 3, 4 ve 5 kişi ile oynanabilir. 
    ---> Lütfen seçim yapınız...
    3 -> 3 kişi
    4 -> 4 kişi
    5 -> 5 kişi
    """)
    try:
        choose_number = int(input("İşlem giriniz: "))
        if choose_number == 3:
            run_game(there_selected_players)
        elif choose_number == 4:
            run_game(four_selected_players)
        elif choose_number == 5:
            run_game(five_selected_players)
        else:
            print(f"{choose_number} kişi ile oyunu oynayamazsınız. Tekrar seçim yapın.")
            choose_number_of_players()
    except ValueError:
        print("Geçersiz bir sayı girişi. Lütfen bir tam sayı giriniz.")
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        print("Tekrar seçim yapınız.")


while True:
    print("""
    ---------------------------------
    HEDEFİ BULMA OYUNUNA HOŞGELDİNİZ
    1 -> Oyun nasıl oynanır?
    2 -> Kuralları biliyorsanız oyuna 
    başlayalım...
    ---------------------------------
    """)
    choose = int(input("İşlem giriniz: "))

    if choose == 1:
        pass
    elif choose == 2:
        choose_number_of_players()
    else:
        print("Seçenekler arasında bulunamadı.")


 # for player in selected_players:
    #     if len(selected_players) == 3:
    #         max_score = max(
    #             player1.sum_targets(),
    #             player2.sum_targets(),
    #             player3.sum_targets())
    #     elif len(selected_players) == 4:
    #         max_score = max(
    #             player1.sum_targets(),
    #             player2.sum_targets(),
    #             player3.sum_targets(),
    #             player4.sum_targets())
    #     else:
    #         max_score = max(
    #             player1.sum_targets(),
    #             player2.sum_targets(),
    #             player3.sum_targets(),
    #             player4.sum_targets(),
    #             player5.sum_targets()
    #         )


#   max_score = max(
#   player1.sum_targets(),
#   player2.sum_targets(),
#   player3.sum_targets())
