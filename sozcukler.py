sozluk = {"apple": "elma", "book": "kitap", "school": "okul", "cat": "kedi"}
print(sozluk["book"])
print(sozluk["school"])
print(sozluk["cat"])

hava_durumu = {"sehir": "Adana", "sicaklik": "39", "sicaklik_birimi": "C", "nem": 0.80, "durum": "güneşli",
               "ruzgar_hizi": 15}

# ekleme
hava_durumu["yagis"] = 0.05

# boş bir sözlük
a = {}
print(type(a))
# boş bir küme
b = set()

# güncelleme
hava_durumu["sicaklik"] = 27
print(hava_durumu)

# silme
# hava_durumu.pop("sicaklik")
# print(hava_durumu)

# temizleme
# hava_durumu.clear()
# print(hava_durumu)

# for kullanımı - burda keyler yazılıyor.
for i in hava_durumu:
    print(i)

for k, v in hava_durumu.items():
    print(f"{k} ---> {v}")

for key in hava_durumu.keys():
    print(key)

for value in hava_durumu.values():
    print(value)

# sozluk uzunluğu
print(len(hava_durumu))
# value in 0. indexsini çağırabiliyor muyuz?

telefon_defteri = {"ahmet öz": "0532 532 32 32",
                   "mehmet su": "0543 543 42 42",
                   "seda naz": "0533 533 33 33",
                   "eda ala": "0212 212 12 12"}

kişi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

if kişi in telefon_defteri:
    print(f"{kişi} adlı kişinin telefon numarası: {telefon_defteri[kişi]}")
else:
    print("Aradığınız kişi telefon rehberinde yok!")

telefon = [["1", 555], ["2", 222], ["3", 333]]
kisi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

for value in telefon:
    if (value[0] == kisi):
        print(f"Mevcut Lokasyon: {value[1]}")
        value[1] = input("Yeni lokasyon girin: ")
        value[1] = value[1].upper()
        print(f"Aradığınız {kisi} isimli kitap raf numarası {value[1]} olarak güncellendi.")
        varmi = True
        break
if varmi == False:
    print("Aradığınız kitap bulunamadı.")

# adana, istanbul, izmir vs bir sürü ilde aynı değişkenlerin bulunduğu bir sözlük yapısı var.
# atıyorum adananın sıcaklığını getir, istanbulun nem oranını getir gibi aynı liste içinde yapabilir miyiz?
# kendi oluşturduğumuz bir data var onu uygulama içinde dosyada tutuyorum. Json formatın


# kütüphane uygulaması
# kitap kaydet diye bir şey olsun.
# kitap arama olsun
# kitap sil olsun
# kitapların yerini değiştirdik.

kitaplar = [["Aşk", "C41"], ["1984", "D52"]]


def kitap_kaydet():
    print(""" # KİTAP KAYDI # """)
    kitap_adi = input("Kitap Adı: ")
    kitap_adi = kitap_adi.title()
    lokasyon = input("Kitabın Yeri: ")
    lokasyon = lokasyon.upper()
    kitaplar.append([kitap_adi, lokasyon])
    print("-------------")
    print("Kitap Kaydı Başarılı!")
    print(kitaplar)


def kitap_ara():
    print(""" # KİTAP ARA # """)
    kitap_adi = input("Kitap Adı: ")
    kitap_adi = kitap_adi.title()
    varmi = False
    for kitap in kitaplar:
        if (kitap[0] == kitap_adi):
            print(f"Aradığınız {kitap_adi} isimli kitap {kitap[1]} numaralı raftadır.")
            varmi = True
            break
    if varmi == False:
        print("Aradığınız kitap bulunamadı.")


def kitap_sil():
    print(""" # KİTAP SİL # """)
    kitap_adi = input("Kitap Adı: ")
    kitap_adi = kitap_adi.title()
    varmi = False
    i = 0
    for kitap in kitaplar:
        if (kitap[0] == kitap_adi):
            kitaplar.pop(i)
            print(f"Kitap silindi.")
            varmi = True
            break
    if varmi == False:
        print("Aradığınız kitap bulunamadı.")


def lokasyon_guncelle():
    print(""" # YENİ LOKASYON # """)
    kitap_adi = input("Kitap Adı: ")
    kitap_adi = kitap_adi.title()
    varmi = False
    for kitap in kitaplar:
        if (kitap[0] == kitap_adi):
            print(f"Mevcut Lokasyon: {kitap[1]}")
            kitap[1] = input("Yeni lokasyon girin: ")
            kitap[1] = kitap[1].upper()
            print(f"Aradığınız {kitap_adi} isimli kitap raf numarası {kitap[1]} olarak güncellendi.")
            varmi = True
            break
    if varmi == False:
        print("Aradığınız kitap bulunamadı.")


while True:
    print(""""**************
    # KİTAP KAYDI #
    1 -> Kitap Kaydet
    2 -> Kitap Ara
    3 -> Kitap Sil
    4 -> Lokasyon güncelle
    -----------------------
    """)
    secim = int(input("İşlem giriniz: "))
    print("*****************")

    if secim == 1:
        kitap_kaydet()
    elif secim == 2:
        kitap_ara()
    elif secim == 3:
        kitap_sil()
    elif secim == 4:
        lokasyon_guncelle()
    else:
        print("Seçenekler arasında bulunamadı.")
