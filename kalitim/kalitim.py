class Calisan:
    def __init__(self, isim, soyisim, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas

    def bilgileri_goster(self):
        return f"---------------\nAd: {self.isim}\nSoyad: {self.soyisim}\nMaaş: {self.maas}"


class Yazilimci(Calisan):
    def __init__(self, isim, soyisim, maas, bilgigi_dil):
        super().__init__(isim, soyisim, maas)
        self.bildigi_dil = bilgigi_dil
    def bilgileri_goster(self):
        return f"*************\nAd: {self.isim}\nSoyad: {self.soyisim}\nMaaş: {self.maas}"


class Frontend(Yazilimci):
    def __init__(self, isim, soyisim, maas, bilgigi_dil, seviye):
        super().__init__(isim, soyisim, maas, bilgigi_dil)
        self.seviye = seviye


class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas, calisanlar=None):
        super().__init__(isim, soyisim, maas)
        if calisanlar is None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar


yazilimci1 = Yazilimci("Ayşe", "Şen", 20000, "Phyton")
yazilimci2 = Yazilimci("Ali", "Kaya", 30000, "PHP")

print(yazilimci1.bilgileri_goster())
print(yazilimci2.bilgileri_goster())

yonetici1 = Yonetici("Kaan", "Yılmaz", 40000, [yazilimci1, yazilimci2])
print(yonetici1.bilgileri_goster())
print(yonetici1.calisanlar[0].bilgileri_goster())

frontendci1 = Frontend("Ayşegül", "Şenay", 50000, "Phyton", 9)
print(frontendci1.bilgileri_goster())

