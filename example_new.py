import random
import time


class Archer:
    def _init_(self, archer_name, accuracy_arrow_hit):
        self.archer_name = archer_name
        self.accuracy_arrow_hit = accuracy_arrow_hit
        self.arrow_targeted_number = 0
        self.total_hit_count = 0

    def arrow_target(self):
        # Performansa göre isabet olasılığını kontrol etme???
        if random.randint(1, 100) <= (self.accuracy_arrow_hit * 100 / 80):
            self.arrow_targeted_number = random.randint(1, 20)
        else:
            self.arrow_targeted_number = 0

    def sum_targets(self):
        return self.total_hit_count

    def uppercase(self):
        return self.archer_name.upper()


class ArrowGame:
    def _init_(self, archers):
        self.archers = archers

    def arrow_game(self):
        for archer in self.archers:
            archer.arrow_target()
            archer.total_hit_count += archer.arrow_targeted_number
            if archer.arrow_targeted_number != 0:
                print(f"{" " * 4}{archer.uppercase()} {archer.arrow_targeted_number} sayısına isabet ettirdi.")
                print(f"{" " * 4}Toplam Puan: {archer.sum_targets()}")
            else:
                print(f"{" " * 4}{archer.uppercase()} isabet ettiremedi.")
                print(f"{" " * 4}Toplam Puan: {archer.sum_targets()}")
            time.sleep(1)


legolas = Archer("Legolas", 50)
katniss = Archer("Katniss", 70)
robinhood = Archer("Robinhood", 90)
susan_pevensie = Archer("Susan Pevensie", 80)
tauriel = Archer("Tauriel", 75)
oliver_queen = Archer("Oliver Queen", 85)

players = [legolas, katniss, robinhood, susan_pevensie, tauriel, oliver_queen]
there_selected_players = random.sample(players, 3)
four_selected_players = random.sample(players, 4)
five_selected_players = random.sample(players, 5)


# player1 = random.choice(players)
# players.remove(player1)
# player2 = random.choice(players)
# players.remove(player2)
# player3 = random.choice(players)
# players.remove(player3)
# player4 = random.choice(players)
# players.remove(player4)
# player5 = random.choice(players)

# there_selected_players = [player1, player2, player3]
# four_selected_players = [player1, player2, player3, player4]
# five_selected_players = [player1, player2, player3, player4, player5]


def run_game(selected_players):
    tour_number = 3
    default_number = 0
    seperator_line = f"{" " * 4}====================================="
    print(seperator_line)
    # Oyuncuların da oyun bittikten sonra karışması gerekiyo.
    if len(selected_players) == 3:
        selected_players = random.sample(players, 3)
    elif len(selected_players) == 4:
        selected_players = random.sample(players, 4)
    else:
        selected_players = random.sample(players, 5)

    while default_number < tour_number:
        ArrowGame(selected_players).arrow_game()
        print(seperator_line)
        default_number += 1

    for player in selected_players:
        # 3 farklı seçenek mevcut. 3, 4, 5 kişilik oyuncu listesi.
        # Seçilen oyuncu listesi içindeki değerlerden en yüksek değere ulaşmaya çalıştım.
        # Liste içindeki her oyuncunun sum_targets() metodu çağırılarak liste elemanlarını döngüye sokar.
        max_score = max(player.sum_targets() for player in selected_players)
        if player.sum_targets() == max_score:
            winner = player
            if winner:
                print(f"{" " * 4}{winner.uppercase()} KAZANDI!")
                print(f"{" " * 4}Toplam puan: {winner.sum_targets()}")
            else:
                print(f"{" " * 4}Berabere bitmiştir.")
    # Oyun sonunda toplam değerlerinin silinmesi ve tekrar sıfırdan eski değerleriyle oyuna başlaması gerekli.
    for player in selected_players:
        player.total_hit_count = 0


def continue_arrow_game():
    continue_game = input(f"{" " * 4}Oyuna devam etmek istiyor musunuz? -Evet -Hayır: ").upper().strip()
    try:
        if continue_game == "EVET":
            choose_number_of_players()
        elif continue_game == "HAYIR":
            print(f"{" " * 4}Oyun sona erdi. Ana menüye aktarılıyor...")
        else:
            print(f"{" " * 4}Tekrar deneyiniz.")
            input(f"{" " * 4}Oyuna devam etmek istiyor musunuz? -Evet -Hayır: ").upper().strip()
    except ValueError:
        print(f"{" " * 4}Geçersiz giriş! Lütfen evet ve hayır seçeneklerinden birini giriniz.")
    except Exception as e:
        print(f"{" " * 4}Beklenmeyen bir hata oluştu: {e}")
        print(f"{" " * 4}Tekrar seçim yapınız.")


def choose_number_of_players():
    print("""
    Oyun 3, 4 ve 5 kişi ile oynanabilir. 
    ---> Lütfen seçim yapınız...
    3 -> 3 kişi
    4 -> 4 kişi
    5 -> 5 kişi
    """)
    try:
        choose_number = int(input(f"{" " * 4}İşlem giriniz: "))
        if choose_number == 3:
            run_game(there_selected_players)
            continue_arrow_game()
        elif choose_number == 4:
            run_game(four_selected_players)
            continue_arrow_game()
        elif choose_number == 5:
            run_game(five_selected_players)
            continue_arrow_game()
        else:
            print(f"{" " * 4}{choose_number} kişi ile oyunu oynayamazsınız. Tekrar seçim yapın.")
    except ValueError:
        print(f"{" " * 4}Geçersiz bir sayı girişi. Lütfen bir tam sayı giriniz.")
    except Exception as e:
        print(f"{" " * 4}Beklenmeyen bir hata oluştu: {e}")
        print("{" " * 4}Tekrar seçim yapınız.")


def is_valid_input(player_name):
    for i in players:
        if player_name == i.archer_name.upper():
            return True
    return False


def choose_players():
    print(f"""
    {len(players)} kişiden oluşan oyuncu listesi
    bulunmaktadır.
    Bu isimler sırası ile: 
    """)
    for player in players:
        print(f"{" " * 4}->{player.archer_name}")
    print(" ")
    player_name1 = input(f"{" " * 4}İlk ismi giriniz: ").upper().strip()
    player_name2 = input(f"{" " * 4}İkinci ismi giriniz: ").upper().strip()
    player_name3 = input(f"{" " * 4}Üçüncü ismi giriniz: ").upper().strip()

    if is_valid_input(player_name1) and is_valid_input(player_name2) and is_valid_input(player_name3):
        print(f"\n{" " * 4}Giriş doğrulandı.")
        choose_player_list = [player_name1, player_name2, player_name3]
        selected_players = []
        for player in players:
            if player.archer_name.upper() in choose_player_list:
                selected_players.append(player)
        print(f"{" " * 4}Girilen isimler: ")
        for i in selected_players:
            print(f"{" " * 4}->{i.archer_name.upper()}")
        # Bir hata mevcut, random döndürüyor. Bool ifade ile bağlanabilir.
        run_game(selected_players)
        choose_players()
    else:
        print(f"\n{" " * 4}Girilen isimler oyuncu listesinde bulunamadı.")


while True:
    print("""
    ---------------------------------
    HEDEFİ BULMA OYUNUNA HOŞGELDİNİZ
    1 -> İstediğiniz 3 oyuncu ile 
    oyuna başlayın...
    2 -> Rastgele oyuncu seçimi ile
    oyuna başlayın...
    ---------------------------------
    """)
    choose = int(input(f"{" " * 4}İşlem giriniz: "))

    if choose == 1:
        choose_players()
    elif choose == 2:
        choose_number_of_players()
    else:
        print(f"{" " * 4}Seçenekler arasında bulunamadı.")