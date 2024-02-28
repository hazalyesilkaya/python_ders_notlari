import time

try:
    dogum_yili = int(input("Doğum Yılınız: "))
    mevcut_yil = int(time.strftime("%Y"))
    yas = mevcut_yil - dogum_yili
    print(f"Yaş: {yas}")
except Exception as e:
    print(f"Bir hata oluştu: {e}")


try:
    sayi1 = float(input("Bölünen sayıyı giriniz: "))
    sayi2 = float(input("Bölen girin: "))
    bolum = sayi1/sayi2
    print(bolum)
except ZeroDivisionError:
    print("Bölen sıfır olamaz.")
    sayi2 = float(input("Bölen girin: "))
    bolum = sayi1 / sayi2
    print(bolum)
# tür hataası
except ValueError as e:
    print(f"{e}")
except Exception as e:
    print("Beklenmeyen bir hata oluştu! Sayıları düzgün yazın.")

try:
    sayilar = [0,1,2,3,4,5,6,7,8,9]
    a = int(input("Bir sayı girin: "))
    b = int(input("Bir sayı daha giriniz: "))
    sonuc = a/b
    print(sonuc)
    print(sayilar[b]/sayilar[b])
except ZeroDivisionError:
    print("Sıfıra bölme hatası oluştu")
except ValueError:
    print("Geçersiz değer girilmiştir.")
except:
    print("Beklenmeyen bir hta oluştu.")
finally:
    print("Program burda sonlandı!")

print("......")
