import random


class Asker:
    def __init__(self, enerji):
        self.enerji = enerji


class Ordu:
    def __init__(self, ad, asker_sayisi):
        self.ad = ad
        self.askerler = []
        for i in range(asker_sayisi):
            asker = Asker(100)
            self.askerler.append(asker)
        self.askerler = self.ordu_kur(asker_sayisi)
        self.enerji = self.toplam_enerji(self.askerler)

    def ordu_kur(self, asker_sayisi):
        for i in range(asker_sayisi):
            asker = Asker(100)
            self.askerler.appened(asker)
        return self.askerler

    def toplam_enerji(self, askerler):
        self.enerji = 0
        for asker in askerler:
            self.enerji += asker.enerji
        return self.enerji

    def saldir(self, saldirilan):
        print(f"{self.ad} ordu {self.ad} orduya hücum ediyor.")
        for i in range(random.randint(10, 100)):
            saldiriya_ugrayan_asker = saldirilan[random.randint(0, len(saldirilan))]
            saldiriya_ugrayan_asker.enerji -= random.randint(50, 100)
            if saldiriya_ugrayan_asker.enerji < 0:
                saldirilan.askerler.remove(saldiriya_ugrayan_asker)
        saldirilan.askerler.pop(0)


mavi = Ordu("Mavi", 10)
for asker in mavi.askerler:
    print(asker.enerji)

