# dosya oluşturma
# open("C://Users//...//demoq.txt",  mode="w", encoding="utf-8")
open("index.html", mode="w", encoding="utf-8")

# dosyaya yazma(WRİTE w)
# Append a
dosyam = open("demo2.txt", mode="a", encoding="utf-8")
dosyam.write("Hazal Y.")
dosyam.close()

# dosya okuma(Read r)
dosyam2 = open("demo2.txt", mode="r", encoding="utf-8")
print(dosyam2.read())

# readline =satırı oku, readlines = listenin tüm satırlarını getiriyo.