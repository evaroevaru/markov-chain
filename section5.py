#section 5
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()
root.geometry("500x300")
root.resizable(True, True)
root.minsize(400, 200)
calc_btn = ttk.Button(root, text="Calculate", bootstyle=SUCCESS)
calc_btn.place(relx=0.4, rely=0.6, anchor=CENTER)


quit_btn = ttk.Button(root, text="Quit", bootstyle=(DANGER), command=root.destroy)
quit_btn.place(relx=0.6, rely=0.6, anchor=CENTER)

dropdown_lbl = ttk.Label(text="Select initial router: ")
dropdown_lbl.place(relx=0.33, rely=0.4, anchor=CENTER)

n = tk.IntVar()
dropdown = ttk.Combobox(root, textvariable=n, state='readonly', bootstyle=(INFO))
dropdown['values'] = ('A', 'B', 'C', 'D', 'E')
dropdown.place(relx=0.67, rely=0.4, anchor=CENTER)
dropdown.set("A")

entry_lbl = ttk.Label(text="Enter number of days: ")
entry_lbl.place(relx=0.33, rely=0.2, anchor=CENTER)

nodays = tk.IntVar()
input_entry = ttk.Entry(root, textvariable=nodays)
input_entry.place(relx=0.67, rely=0.2, anchor=CENTER)

# main program
e = 0
f = 0
g = 0
h = 0
i = 0
with open('network_traffic.txt','r') as file:
    for line in file:
        d = line.split('->')
        if d[0]=='A':
            e = e+1
        if d[0]=='B':
             f = f+1
        if d[0]=='C':
            g = g+1
        if d[0]=='D':
            h = h+1
        if d[0]=='E':
            i = i +1
e = round(e/10000,5)
f = round(f/10000,5)
g = round(g/10000,5)
h = round(h/10000,5)
i = round(i/10000,5)

print(str(e))
print(str(f))
print(str(g))
print(str(h))
print(str(i))

root.mainloop()
