import tkinter as tk

form = tk.Tk()
form.geometry("600x600+500+200")

degisken = tk.IntVar()


def spinner():
    print(degisken.get())


tk.Spinbox(form, from_=0, to=10, textvariable=degisken).pack()

tk.Button(form, text="Yaz", command=spinner).pack()

form.mainloop()
