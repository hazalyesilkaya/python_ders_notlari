# # NESNE TABANLI PROGRAMLAMA
#
#
# class Araba:
#     def __init__(self,brand,type,year):
#         self.marka=brand
#         self.model=type
#         self.yil=year
#         self.hiz=0
#
#
#     def hizlan(self,artis):
#         self.hiz+=artis
#         print(f"{self.marka}-{self.model} marka aracın hızı {artis} artarak {self.hiz} a cıktı.")
#
#
#     def yavasla(self,dusus):
#         self.hiz-=dusus
#         print(f"{self.marka}-{self.model} marka aracın hızı {dusus} azalarak {self.hiz} a düştü.")
#
#
# car1=Araba("Toyota","Yaris",2005)
# print(car1.hiz)
# print(car1.model)
# print(car1.marka)
# print(car1.yil)
# car1.hizlan(100)
# car1.yavasla(40)
#
# print("---------------")
#
# car2=Araba("Ford","Focus",2015)
# print(car2.hiz)
# print(car2.model)
# print(car2.marka)
# print(car2.yil)
# car2.hizlan(200)
# car2.yavasla(130)