class Kitap:
    def __init__(self, ad, yazar, raf_no, durum, kategori):
        self.ad = ad
        self.yazar = yazar
        self.raf_no = raf_no
        self.durum = durum  # Rafta - Ödünç alındı.
        self.odunc_alma_sureleri = 0
        self.kategori = kategori

    @staticmethod
    def kitap_ara(kitaplar, aranan_ad):
        eslesen_kitaplar = []
        for kitap in kitaplar:
            if aranan_ad.upper() in kitap.ad.upper() or aranan_ad.upper() in kitap.yazar.upper():
                eslesen_kitaplar.append(kitap)
        return eslesen_kitaplar

    @staticmethod
    def kategoriye_gore_ara(kitaplar, kategori):
        eslesen_kitaplar = []
        for kitap in kitaplar:
            if kitap.kategori.upper() == kategori.upper():
                eslesen_kitaplar.append(kitap)
        return eslesen_kitaplar

    def odunc_al(self):
        if self.durum == "Rafta":
            print(f"{self.ad} kitabı ödünç alınabilir durumda.")
            sure = int(input("Kaç gün ödünç almak istiyorsunuz? (10/20/30): "))
            if sure in [10, 20, 30]:
                self.durum = "Ödünç Alındı"
                self.odunc_alma_sureleri = sure
                print(f"{self.ad} kitabı {sure} gün ödünç alındı.")
            else:
                print("Geçersiz süre seçimi. Ödünç alma işlemi iptal edildi.")
        else:
            print("Bu kitap şu anda ödünç alınamaz.")

    def suresini_uzat(self, ek_sure):
        if self.durum == "Ödünç Alındı":
            yeni_sure = self.odunc_alma_sureleri + ek_sure
            print(f"{self.ad} kitabının toplam ödünç alınma süresi {yeni_sure} gün olarak tanımlandı.")
            self.odunc_alma_sureleri = yeni_sure
        else:
            print("Bu kitap ödünç alınmamıştır, kütüphanede bulunuyor.")

    def iade_et(self):
        if self.durum == "Ödünç Alındı":
            print(f"{self.ad} kitabı başarıyla iade edildi.")
            self.durum = "Rafta"
            self.odunc_alma_sureleri = 0
        else:
            print("Bu kitap ödünç alınmamıştır, kütüphanede bulunuyor.")


def kitap_ekleme(ad, yazar, raf_no, durum, kategori):
    kitap = Kitap(ad, yazar, raf_no, durum, kategori)
    kitaplar.append(kitap)


kitaplar = []
kitap_ekleme("Suç ve Ceza", "Dostoyevski", 1, "Rafta", "Roman")
kitap_ekleme("Anna Kareninaa", "Tolstoy", 2, "Rafta", "Roman")
kitap_ekleme("Sefiller", "Victor Hugo", 3, "Rafta", "Roman")
kitap_ekleme("1984", "George Orwell", 4, "Rafta", "Roman")
kitap_ekleme("Yüzyıllık Yalnızlık", "Gabriel Garcia Marquez", 5, "Rafta", "Roman")
kitap_ekleme("Sherlock Holmes Serisi", "Sir Arthur Conan Doyle", 6, "Rafta", "Polisiye")
kitap_ekleme("Gone Girl", "Gillian Flynn", 7, "Rafta", "Polisiye")
kitap_ekleme("The Da Vinci Code", "Dan Brown", 8, "Rafta", "Polisiye")
kitap_ekleme("Hamlet", "William Shakespeare", 9, "Rafta", "Tiyatro")
kitap_ekleme("Romeo ve Juliet", "William Shakespeare", 10, "Rafta", "Tiyatro")
kitap_ekleme("Macbeth", "William Shakespeare", 11, "Rafta", "Tiyatro")
kitap_ekleme("Düşten güzel", "Özdemir Asaf", 12, "Rafta", "Şiir")


def yazara_ve_kitap_ismine_gore_arama(eslesen_kitaplar, isim):
    if eslesen_kitaplar:
        for i in eslesen_kitaplar:
            if i.durum == "Rafta":
                print(f"*Kitap ismi*{' ' * (21 - len("Kitap ismi"))}*Yazar*{' ' * (21 - len("Yazar"))}*Kategori*"
                      f"{' ' * (21 - len("Kategori"))}*Raf No*")
                break
        for kitap in eslesen_kitaplar:
            if kitap.durum == "Rafta":
                print(f"{kitap.ad}{' ' * (23 - len(kitap.ad))}{kitap.yazar}{' ' * (23 - len(kitap.yazar))}"
                      f"{kitap.kategori}{' ' * (23 - len(kitap.kategori))}{kitap.raf_no}")
            else:
                print(f"Bu {isim}de bir kitap bulunamadı.")
    else:
        print(f"Bu {isim}de bir kitap bulunamadı.")


while True:
    print("""
  KÜTÜPHANE OTOMASYONU
  1 -> Almak istediğiniz kitabı arayın.
  2 -> Kategoriye göre kitap arayın.
  3 -> Mevcut kitabı ödünç alabilirsiniz.
  4 -> Aldığınız kitabın süresini uzatın.
  5 -> Kitabı iade edin.
  """)
    choose = int(input("İşlem giriniz: "))

    if choose == 1:
        aranan = input("Aramak istediğiniz kitabın adını veya yazarını girin: ")
        eslesen_kitaplar = Kitap.kitap_ara(kitaplar, aranan)
        yazara_ve_kitap_ismine_gore_arama(eslesen_kitaplar, "isim")
    elif choose == 2:
        kategori = input("Aramak istediğiniz kategoriyi girin: ")
        eslesen_kitaplar = Kitap.kategoriye_gore_ara(kitaplar, kategori)
        yazara_ve_kitap_ismine_gore_arama(eslesen_kitaplar, "kategori")
    elif choose == 3:
        ad = input("Ödünç almak istediğiniz kitabın adını girin: ")
        for kitap in kitaplar:
            if kitap.ad.upper() == ad.upper():
                kitap.odunc_al()
                break
        else:
            print("Girdiğiniz isimde bir kitap bulunamadı.")
    elif choose == 4:
        ad = input("Süresini uzatmak istediğiniz kitabın adını girin: ")
        for kitap in kitaplar:
            if kitap.ad.upper() == ad.upper():
                kitap.suresini_uzat(7)
                if kitap.durum == "Ödünç Alındı":
                    print("İşlem süresi 7 gün uzatıldı.")
                break
    elif choose == 5:
        ad = input("İade etmek istediğiniz kitabın adını girin: ")
        for kitap in kitaplar:
            if kitap.ad.upper() == ad.upper():
                kitap.iade_et()
                break
            else:
                print("Girdiğiniz isimde bir kitap bulunamadı veya ödünç alınmamış.")
                break
