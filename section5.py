#section 5
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()
root.geometry("500x300")
root.resizable(True, True)
b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS)
b1.place(relx=0.4, rely=0.6, anchor=CENTER)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE))
b2.place(relx=0.6, rely=0.6, anchor=CENTER)

b3 = ttk.Button(root, text="Quit", bootstyle=(DANGER), command=root.destroy)
b3.place(relx=0.5, rely=0.8, anchor=CENTER)

n = tk.IntVar()
dropdown = ttk.Combobox(root, textvariable=n)
dropdown['values'] = ('A', 'B', 'C', 'D', 'E')
dropdown.place(relx=0.5, rely=0.4, anchor=CENTER)
dropdown.set("A")


nodays = tk.IntVar()
input_entry = ttk.Entry(root, textvariable=nodays)
input_entry.place(relx=0.5, rely=0.2, anchor=CENTER)

root.mainloop()
