import random

# lists - ekleme çıkarma yapılır.değişik olur.
group_one = ['Ahmet', 'Kenan', 'Hasan']
# h getirir. Ahmetin 2. elemanı
print(group_one[0][1])

# 10 - forma no, 1.75 - boyu, 72 - kilo, true - evli
Ahmet = ['Milli Takım', 10, 1.75, 72, 'Kara', True]
Kenan = ['Milli Takım', 19, 1.69, 85, 'Kaya', False]
print(f'takım  =  {Ahmet[0]} ')
#
print(group_one)
#
for i in group_one:
    print(i)
print('-------------')
# liste içinde farklı listeler barınabilir. O. elemanının 1: elemanı olarak nohut döndü.
gıdalar = [['fasülye', 'nohut', 'mercimek'],
           ['şeker', 'yağ', 'un'],
           ['domates', 'salatalık', 'patlıcan']]
print(gıdalar[0][1])

# liste eleman değiştirme
sebzeler = ['domates', 'salatalık', 'patlıcan', 'kabak', 'fasülye', 'soğan', 'karpuz']
sebzeler[-1] = 'Patates'
print(sebzeler)
print(len(sebzeler))
print(len(group_one))

# listeye eleman ekleme
sebzeler.append('biber')
print(sebzeler)
sebzeler.insert(2, 'bamya')
print(sebzeler)

sebzeler += ['sarımsak', 'üzüm']
print(sebzeler)

# listeden eleman silme
sebzeler.remove('üzüm')
print(sebzeler)

sebzeler.pop(1)
print(sebzeler)

del sebzeler[1]
print(sebzeler)

# listenin içindekilerin hepsini silme
sebzeler.clear()
print(sebzeler)
# del sebzeler dersek herşeyi siler bir daha print edemezsin.
# del sebzeler
# print(sebzeler)

# kopyalama

liste1 = ['Ali', 'Ayşe']
liste2 = ['Ahmet', 'Fatma']

liste3 = liste1
liste1[0] = 'Veli'

print(id(liste3))
print(id(liste1))  # aynı çıktı.
print(liste1)
print(liste3)  # aynı çıktı.

liste4 = liste2.copy()
liste2.append('Ahmet')
print(id(liste2))
print(id(liste4))  # farklı çıktı.

print(liste2)
print(liste4)  # veriler farklı çıktı.

# sıralama, string listeyi de sıralıyo sort methodu.
rakamlar = [0, 7, 9, 8, 2, 3, 2, 1]
rakamlar.sort(reverse=True)
print(rakamlar)

# users = [['yunus@ecodation.com', '123456'],
#          ['ahmet@gmail.com', '112233'],
#          ['mehmet@hotmail.com', '102030']]
# print('### Login ###')
# email = input("e-mail : ")
# password = input("Şifre : ")
# is_mail = False
#
# for user in users:
#     if email in user:
#         is_mail = True
#         i = users.index(user)
#         break
# if is_mail:
#     if users[i][1] == password:
#         print('Giriş Başarılı')
#     else:
#         print('Şifre Yanlış!')
# else:
#     print('Böyle bir kullanıcı bulunamadı.')
#


listex = [1, 2, 3, 4, 5, 6]
cevap = 0 not in listex
print(cevap)

# Belli bir elemanın sayısını bulma
names = ['Ali', "Ayşe", "Veli", "Ahmet", "Ayşe"]
ayse_sayisi = names.count("Ayşe")
print(ayse_sayisi)

# En büyük ve en küçük elemanlar
sayilar = [1, 700, 159, 3698, -25, -987, 15, 100]
sayilar.sort()
enkucuk = sayilar[0]
en_buyuk = sayilar[-1]
print(f"En büyük eleman : {en_buyuk}, En küçük eleman: {enkucuk}")


def minik(sayi):
    sayi.sort()
    kucuk = sayi[0]
    return kucuk


print(minik(sayilar))

print(min(sayilar))
print(max(sayilar))

# liste elemanlarının toplamı
sayilar = [1, 700, 159, 3698, -25, -987, 15, 100]

# Toplamı saklamak için bir değişken oluştur
toplam = 0

# Listenin her elemanını topla
for sayi in sayilar:
    toplam += sayi

print("Liste elemanlarının toplamı:", toplam)

toplam = sum(sayilar)
adet = len(sayilar)
ortalama = toplam / adet
print(ortalama)

# Liste üreticisi
yuzden_kucuk_sayılar = [x for x in range(10, 20, 2)]
print(yuzden_kucuk_sayılar)

# mukemmel_besli = []
# for i in range(6):
#     yeni_sayi = random.randint(1, 5)
#     while yeni_sayi not in mukemmel_besli:
#        mukemmel_besli.append(yeni_sayi)
# print(mukemmel_besli)





# demetler - demetler değişmez ekleme çıkarma yok.


# kümeler - bir eleman aynıysa 2 kez bulunmaz.


# sözcükler - değişkenlerin key i oluyo.
