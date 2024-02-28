telefon = [["ahmet", 555], ["mehmet", 222], ["ayşe", 333]]
kisi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

for value in telefon:
    if (value[0] == kisi):
        print(f"Telefon numarası: {value[1]}")
        value[1] = input("Yeni isim girin: ")
        value[1] = value[1].upper()
        print(f"Aradığınız {kisi} isimli kitap raf numarası {value[1]} olarak güncellendi.")
        varmi = True
        break
else:
    print("Aradığınız kişi bulunamadı.")