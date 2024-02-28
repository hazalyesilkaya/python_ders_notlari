# tuples listelere çok benzer tek farkı ekleme çıkarma işlemleri yapılamaz.

osmanli_ilk_bes_padisah = ("1. Osman", "Orhangari", "1. Murat", "1. Beyazıt", "2. Mehmet")
haluk_levent_arkadas_album = ("K", "A")
vizontele_oyunculari = ("Yılmaz Erdoğan", "Cem Yılmaz", "Tolga Çevik")
egitim_serisi = ("Listeler", "Tuples")

print(osmanli_ilk_bes_padisah[2])

for i in osmanli_ilk_bes_padisah:
    print(i)
# parcalama hilesi, bir demetin içinden yeni bir demet oluşturulabilir.
# parçalanmış olanı sonrasında ekleme çıkarma yapılabiliyor mu?
h = haluk_levent_arkadas_album[0:2]
print(h.count("K"))
print(len(h))

liste = [1, 2, 3, 4]
