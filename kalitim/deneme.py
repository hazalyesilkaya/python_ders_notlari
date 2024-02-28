import random


class Asker:
    def __init__(self, enerji):
        self.enerji = enerji


class Ordu:
    def __init__(self, ad, asker_sayisi):
        self.ad = ad
        self.askerler = self.ordu_kur(asker_sayisi)
        self.enerji = self.toplam_enerji(self.askerler)

    def ordu_kur(self, asker_sayisi):
        askerler = []
        for i in range(asker_sayisi):
            asker = Asker(100)
            askerler.append(asker)
        return askerler

    def toplam_enerji(self, askerler):
        enerji = 0
        for asker in askerler:
            enerji += asker.enerji
        return enerji

    def saldir(self, saldirilan):
        print(f"{self.ad} ordu {saldirilan.ad} orduya hücum ediyor.")
        for i in range(random.randint(10, 100)):
            saldiriya_ugrayan_asker = saldirilan.askerler[random.randint(0, len(saldirilan.askerler) - 1)]
            saldiriya_ugrayan_asker.enerji -= random.randint(50, 100)
            if saldiriya_ugrayan_asker.enerji <= 0:
                saldirilan.askerler.remove(saldiriya_ugrayan_asker)
        saldirilan.askerler.pop(0)


mavi = Ordu("Mavi", 10)
sari = Ordu("Sari", 5)
print("Mavi ordunun askerlerinin enerjileri:")
for asker in mavi.askerler:
    print(asker.enerji)

print("Sari ordunun askerlerinin enerjileri:")
for asker in sari.askerler:
    print(asker.enerji)

