import tkinter as tk

# CheckBox - birden çok seçenek işaretlenebilir.
form = tk.Tk()
form.geometry("800x800+500+200")

degisken1 = tk.IntVar()
degisken1.set(0)
degisken2 = tk.IntVar()
degisken2.set(0)


def frs_control():
    if degisken1.get() == 1:
        label1.config(text="FRANSIZCA SEÇİLDİ", fg="green", font="bold")
    else:
        label1.config(text="FRANSIZCADAN SEÇİM KALDIRILDI", fg="red", font="bold")


def ing_control():
    if degisken2.get() == 1:
        label2.config(text="İNGİLİZCE SEÇİLDİ", fg="green", font="bold")
    else:
        label2.config(text="İNGİLİZCEDEN SEÇİM KALDIRILDI", fg="red", font="bold")


checkbox1 = tk.Checkbutton(form, text="İngilizce", variable=degisken1, command=ing_control)
checkbox1.pack()

checkbox2 = tk.Checkbutton(form, text="Fransızca", variable=degisken2, command=frs_control)
checkbox2.pack()
# Radio Button - yalnızca tek button seçilebilir.


radio1 = tk.Radiobutton(form, text="Erkek", value="E", variable=degisken1)
radio1.pack()
radio2 = tk.Radiobutton(form, text="Kadın", value="K", variable=degisken1)
radio2.pack()


label1 = tk.Label(form, text="___________")
label1.pack()
label2 = tk.Label(form, text="___________")
label2.pack()
form.mainloop()
