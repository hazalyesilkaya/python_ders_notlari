import time
person_file = open("../kisiler.txt", mode="w", encoding="utf-8")
person_file.write("KİŞİ                                   # ODA NUMARASI | TARİH #\n")
person_file.close()
def add_person():
    username = input("Kişi adı:")
    number = input("Oda Numarası: ")
    start_time = time.strftime("%d.%B.%Y")
    len_username = len(username)
    last_username = f"{username}{" " * (40 - len_username)}"
    person_f = open("../kisiler.txt", mode="a", encoding="utf-8")
    person_f.write(f"{last_username} | {number}  |  {start_time}\n")
def get_persons():
    persons_file = open("../kisiler.txt", mode="r", encoding="utf-8")
    persons = persons_file.readline()
    for person in persons:
        print(person[:-1])
while True:
    print("RESEPSİYON")
    print("----------")
    print("1.Kayıtlı Kişiler")
    print("2.Oda Bilgilerinizi Giriniz")
    print("-----------")
    choose = int(input("İşlem Seçin: "))
    if choose == 1:
        get_persons()
    elif choose == 2:
        add_person()
    else:
        print("Geçersiz Seçim!")
        print("###############")
