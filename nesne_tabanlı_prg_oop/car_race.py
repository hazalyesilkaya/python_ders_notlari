# 2 tane araba var. ya da arabalar, performansına göre 100 çizgiye ulaşan oyunu kazansın.
# Audi -->
# Bmw ----->
# Toyoto ------->
# döngü her çalıştığında
import os
import random
import time


class Cars:
    def __init__(self, car_brand, performance):
        self.car_brand = car_brand
        self.performance = performance

    def get_performance(self):
        print(f"{self.car_brand}{' ' * (10 - len(self.car_brand))} {'-' * self.performance} >")

    def race(self):
        self.performance += self.performance
        self.get_performance()


toyota = Cars("Toyota", 20)
bmw = Cars("Bmw", 30)
audi = Cars("Audi", 30)
mercedes = Cars("Mercedes", 35)
honda = Cars("Honda", 25)
tofas = Cars("Tofaş", 10)

selected_cars = random.sample([toyota, bmw, audi, mercedes, honda, tofas], 2)
player1 = selected_cars[0]
player2 = selected_cars[1]
print(f"Yarışan araçlar: {player1.car_brand} vs {player2.car_brand}")

while player1.performance < 100 and player2.performance < 100:
    player1.race()
    player2.race()
    time.sleep(0.5)

if player1.performance > player2.performance:
    print(f"\n{player1.car_brand} kazandı!")
elif player1.performance < player2.performance:
    print(f"\n{player2.car_brand} kazandı!")
else:
    print("\nBerabere! İki araç da aynı performansta.")
