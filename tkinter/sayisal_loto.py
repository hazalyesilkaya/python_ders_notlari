# sayısal loto
import random
from tkinter import *

pencere = Tk()
pencere.title("Sayısal Loto")
pencere.geometry("900x400+500+200")
pencere.configure(bg="#ab0030")
pencere.resizable(False, False)

l1 = Label(pencere, text="_", font="Calibri 50 bold", fg="white", bg="#eb0030")
l1.place(x=150, y=120)

l2 = Label(pencere, text="_", font="Calibri 50 bold", fg="white", bg="#eb0030")
l2.place(x=250, y=120)

l3 = Label(pencere, text="_", font="Calibri 50 bold", fg="white", bg="#eb0030")
l3.place(x=350, y=120)

l4 = Label(pencere, text="_", font="Calibri 50 bold", fg="white", bg="#eb0030")
l4.place(x=450, y=120)

l5 = Label(pencere, text="_", font="Calibri 50 bold", fg="white", bg="#eb0030")
l5.place(x=550, y=120)

l6 = Label(pencere, text="_", font="Calibri 50 bold", fg="white", bg="#eb0030")
l6.place(x=650, y=120)

 # pgm/ppm formatı olmalı
# resim = PhotoImage(file="photo.pgm")
# l0 = Label(image=resim)
# l0.pack()


def cekilis_yap():
    sayilar = []
    for i in range(1, 91):
        sayilar.append(i)
    super_numaralar = random.sample(sayilar, 6)
    super_numaralar.sort()
    l1.config(text=f"{super_numaralar[0]}")
    l2.config(text=f"{super_numaralar[1]}")
    l3.config(text=f"{super_numaralar[2]}")
    l4.config(text=f"{super_numaralar[3]}")
    l5.config(text=f"{super_numaralar[4]}")
    l6.config(text=f"{super_numaralar[5]}")


btn = Button(pencere, text="Çekiliş yap", font="calibri 12 bold", bg="gray", width="50", command=cekilis_yap)
btn.place(x=240, y=240)
pencere.mainloop()
