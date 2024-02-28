# manav
# ürün ekle
# ürün listele

urunler = {"portakal": 19.00, "cilek": 20.00}


def add():
    print(""" # ÜRÜN EKLE # """)
    urun_adi = input("Ürün Adı: ")
    urun_fiyati = input("Ürün Fiyatı: ")
    urun_adi = urun_adi.title()
    urunler[urun_adi] = urun_fiyati
    print("-------------")
    print("Ürün Kaydı Başarılı!")


def list():
    print(urunler)


while True:
    print(""""**************
    # ÜRÜN KAYDI #
    1 -> Ürün ekle
    2 -> Ürünleri listele
    -----------------------
    """)
    secim = int(input("İşlem giriniz: "))
    print("*****************")

    if secim == 1:
        add()
    elif secim == 2:
        list()
    else:
        print("Seçenekler arasında bulunamadı.")
