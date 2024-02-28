import tkinter as tk

window = tk.Tk()
window.geometry("500x500+800+200")

window.title("Login Ekranı")
window.resizable(False, False)
window.config(bg="black")

l1 = tk.Label(window, text="BMI HESAPLA", font="Arial 22 bold", fg="white", bg="red")
l1.pack(pady=100)

l2 = tk.Label(window, text="Boy", font="Arial 12 bold", bg="red", fg="white")
l2.place(x=90, y=160)

e1 = tk.Entry(window, font="Arial 12 italic")
e1.place(x=200, y=160)

l3 = tk.Label(window, text="Kilo", font="Arial 12 bold", bg="red", fg="white")
l3.place(x=90, y=190)

e2 = tk.Entry(window, font="Arial 12")
e2.place(x=200, y=190)

l4 = tk.Label(window, text="_________________________________", font="Arial 12 bold", bg="gray", fg="white")
l4.place(x=90, y=390)


def calculate_bmi():
    boy = float(e1.get())
    kilo = float(e2.get())
    boy = boy/100  # metreye çevirme
    bmi = kilo / (boy * boy)

    l4.config(text=f"BMI: {bmi}")


btn = tk.Button(window, text="Hesapla", bg="gray", width="10", command=calculate_bmi)
btn.place(x=300, y=240)


window.mainloop()
