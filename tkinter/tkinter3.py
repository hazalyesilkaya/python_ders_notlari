import tkinter as tk

from tkinter.ttk import Combobox
from tkinter import messagebox

form = tk.Tk()
form.geometry("300x300+500+200")
iller = ["ADANA", "BURSA", "ÇANAKKALE", "DENİZLİ","EDİRNE","GİRESUN", "HATAY", "ISPARTA",
         "İSTANBUL", "KASTAMONU", "MUĞLA", "OSMANİYE","RİZE","SAMSUN"]
combo = Combobox(form, values=iller, height=5)
combo.current(8)
combo.pack()


def il_yaz():
    label1.config(text=f"{combo.get()} seçildi.")


label1 = tk.Label(form, text=".........")
label1.pack()


def bilgi_goster():
    messagebox.showinfo(title="BİLGİ", message="Python öğrenmesi en kolay programlama dilleri arasında yer alır.")


buttonA = tk.Button(form, text="Bilgilendir", command=bilgi_goster)
buttonA.pack()

def uyari_goster():
    messagebox.showwarning(title="UYARI", message="Bu işlem bir veri kaybına sebep olabilir.")


buttonB = tk.Button(form, text="Uyar", command=uyari_goster)
buttonB.pack()


def hata_ver():
    messagebox.showerror(title="HATA", message="Beklenmeyen bir hata oluştu.")


buttonC = tk.Button(form, text="Hata Ver", command=hata_ver)
buttonC.pack()


def yes_no():
    messagebox.askyesno(title="SORU", message="Türkiyenin başkenti Ankara mı?")


buttonD = tk.Button(form, text="Soru", command=yes_no)
buttonD.pack()


il_yaz_button = tk.Button(form, text="İli Yaz", command=il_yaz)
il_yaz_button.pack()

form.mainloop()
