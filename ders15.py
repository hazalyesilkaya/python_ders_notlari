
text = 'Yazılım sektörü yapay zeka ile yeni bir yolculuğa başladı.'

# ilk 7 karakteri getirdi.
print(text[0:7])

# -1.--10. karakter. -1 dahil değil
print(text[-10:-1])

#-10 dan başla sonuna kadar al.
print(text[-10:])

#text'in kaç karakterli olduğunu bul.
print(len(text))

# yapay zeka kısmını AI ile değiştirdik.
new_text = text.replace('yapay zeka', 'AI')
print(new_text)

# 1. k harfini z ile değiştir.
cumle1 = 'Yakıtları koruyamadık'
cumle2 = cumle1.replace('k','z',1)
print(cumle2)
#text içinde ö nün olduğu indeksi getir.
print(text.index('ö'))

# eksik_cumle = cumle1[cumle1.index('k'):]
# print(cumle1[cumle1.index('k'):])
# print(eksik_cumle.replace('k','z', 1))

# title: ilk harfi büyük, upper ve lower hepsi büyük ya da hepsi küçük harf.
print('ecodation'.upper())
print('Ecodation'.lower())
print('ecodation academy'.title()) # her iki kelimenin ilk harfleri büyük.
print('ecodation academy'.capitalize()) #yalnızca ilk harfi büyük.
print('Yunus Alparslan'.lower().count('a'))

# önde arkada boşluk veya başka bir şey olunca onu siler.
print('----selam-merhaba----'.strip('-'))

#- lerden kelimeleri böl.
print('selam-merhaba-günaydın'.split('-'))

#endswith bir şeyle bitip bitmediğini yakalıyo.

# x i bulmaya çalışıyo. bulamayınca -1 dönüyor.
print('amdfhdfösd'.find('x'))

# soldakileri silmek istersek lstrip kullanılır.
print('----selam-merhaba----'.lstrip('-'))

def ikisayi(a,b):
    return a + b

x = ikisayi(10, 5)

print(x)
