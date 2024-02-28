import time

# tick formunda zaman

print(time.time())

# pc deki zaman

now = time.localtime()
print(now)
print(type(now))
print(now.tm_year)
print(now.tm_mon)
print(now.tm_hour)

# zamanı biçimlendirme
print(time.asctime())

zaman1 = time.strftime("%d.%B.%Y")
print(zaman1)

for i in range(1):
    print(".", end="")
    time.sleep(0.5)


# LOG KAYIT
islemler = []
islem = ""

def log(text):
    aciklama = text
    tarih = time.strftime("%d.%m.%Y %H:%M:%S")
    islem = (aciklama, tarih)
    islemler.append(islem)
    listele()
    main()
def listele():
  for islem in islemler:
      print(f"{islem[1]} --- {islem[0]}")
def main():
    print("İŞLEMLER")
    print("1.Ekle")
    print("2.Güncelle")
    print("3.Sil")
    print("4.Listele")
    secim = int(input("Bir işlem Seç: "))
    if secim == 1:
        log("Yeni kayıt eklendi")
    elif secim == 2:
        log("Bir kayıt güncellendi.")
    elif secim == 3:
        log("Bir kayıt silindi")
    elif secim == 4:
        log("Bir kayıt listelendi")
    else:
        print("Geçersiz seçim!")


print(islemler)
# main()

