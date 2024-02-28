person_file = open("kisiler.txt", mode="w", encoding="utf-8")
person_file.write("KİŞİ                                         # TELEFON #\n")
person_file.close()


# ekleme

def add_person():
    username = input("Kişi adı:")
    phone = input("Telefon: ")
    len_username = len(username)
    last_username = f"{username}{" " * (40 - len_username)}"
    person_f = open("kisiler.txt", mode="a", encoding="utf-8")
    person_f.write(f"{last_username}|{phone}\n")


# listeleme

def get_persons():
    persons_file = open("kisiler.txt", mode="r", encoding="utf-8")
    persons = persons_file.readline()
    for person in persons:
        print(person[:-1])


while True:
    print("MY PHONE")
    print("----------")
    print("1.Kişiler")
    print("2.Kişi Ekle")
    print("-----------")
    choose = int(input("İşlem Seçin: "))
    if choose == 1:
        get_persons()
    elif choose == 2:
        add_person()
    else:
        print("Geçersiz Seçim!")
        print("###############")
