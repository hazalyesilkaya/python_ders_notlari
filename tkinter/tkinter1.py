import tkinter as tk

window = tk.Tk()
window.geometry("500x500+800+200")

window.title("Login Ekranı")
window.resizable(False, False)  # sağa sola ve yukarı aşağı büyebilmesi
window.config(bg="red")
# Label
l1 = tk.Label(window, text="COMPANY PANEL", font="Arial 24 bold", fg="white", bg="red")
l1.pack(pady=100)

# Username
l2 = tk.Label(window, text="Username", font="Arial 12 bold", bg="red", fg="white")
l2.place(x=90, y=160)

e1 = tk.Entry(window, font="Arial 12 italic")  # kullanıcı veri girişi input
e1.place(x=200, y=160)

# Password
l3 = tk.Label(window, text="Password", font="Arial 12 bold", bg="red", fg="white")
l3.place(x=90, y=190)

e2 = tk.Entry(window, font="Arial 12 italic")  # kullanıcı veri girişi input
e2.place(x=200, y=190)

# Alert
l4 = tk.Label(window, text="_________________________________", font="Arial 12 bold", bg="red", fg="white")
l4.place(x=90, y=390)


# Button
def login():
    username = e1.get()
    password = e2.get()
    if username == "admin" and password == "112233":
        l4["text"] = "Username and Passwprd is True"
        l4["bg"] = "Green"
    else:
        l4["text"] = "Username or Password is False"
        l4["bg"] = "Orange"


b1 = tk.Button(window, text="Giriş", bg="gray", width="10", command=login)
b1.place(x=300, y=240)
window.mainloop()  # bu pencerenin açık kalmasını sağlıyor.
