import tkinter as tk

form = tk.Tk()
form.geometry("900x900+500+200")

# Scroll
# Listbox

scroll = tk.Scrollbar(form)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(form, yscroll=scroll.get())
listbox.pack(side=tk.LEFT)

for i in range(1, 101):
    listbox.insert("end", str(i))

scroll.config(command=listbox.yview)

t = tk.Text(form, width= 10, height=15).pack()


form.mainloop()
