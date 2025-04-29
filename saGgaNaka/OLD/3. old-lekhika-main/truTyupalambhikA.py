from tkinter import Tk, Label
from tkinter import font
from tkinter.font import Font
import tkinter.ttk as ttk

root = Tk()

style = ttk.Style()
style.configure("h.TLabel", font=("Nirala UI", 14, "bold"), foreground="red")
l1 = ttk.Label(root, text="This part is under development.", style="h.TLabel")
l1.grid(row=0,column=0,sticky="nw")
root.mainloop()