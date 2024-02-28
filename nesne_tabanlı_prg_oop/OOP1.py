# s = []
# a = [1,1,1,2,0,3,1,5,8,4]
# x = ""
# len_a = len(a)
# # len_a = 10
#
# for i in range(len_a):
#     if( a[i]%2 == a[i-1]%2):
#         s.append(max(a[i],a[i-1]))
#
# for j in s:
#     x +=str(j)
# url = f"www.multisoft.se/{x}"
# print(url)
# # www.multisoft.se/112358
# isminin ilk harfi ile babamın adının arasına kardeşlerininin adını yazan program.
import random


class Car:
    def __init__(self, brand, type_car, year):
        self.marker = brand
        self.model = type_car
        self.yil = year
        self.hiz = 0

    def hizlan(self, artis):
        self.hiz += artis
        print(f"{self.marker}-{self.model} marka aracın hızı {artis} artarak {self.hiz} a çıktı.")

    def yavasla(self, dusus):
        self.hiz -= dusus
        print(f"{self.marker}-{self.model} marka aracın hızı {dusus} azalarak {self.hiz} a düştü.")


car1 = Car("Toyota", "Yaris", 2005)
print(car1.model)
print(car1.marker)
print(car1.hiz)
print(car1.yil)
car1.hizlan(100)
car1.yavasla(40)

print("----------------")
car2 = Car("Ford", "Focus", 2015)
print(car2.model)
print(car2.marker)
print(car2.hiz)
print(car2.yil)
car2.hizlan(200)
car2.yavasla(130)


class Asker:
    rutbe = "Er"
    def __init__(self, enerji, techizat):
        self.enerji = enerji
        self.techizat = techizat

askerler = []
for i in range(10):
    enerji = random.randint(1, 100)
    techizat = random.randint(1, 100)
    yeni_asker = Asker(enerji, techizat)
    askerler.append(yeni_asker)

    for asker in askerler:
        print(asker.enerji)
