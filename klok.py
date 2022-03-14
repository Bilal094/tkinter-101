import tkinter as tk
from tkinter import StringVar
import time 

root = tk.Tk()

def timeUpdate():
    current_time.set(time.strftime('%H:%M:%S'))
    root.after(1000, timeUpdate)

current_time = StringVar()
timeUpdate()
klok = tk.Label(textvariable=current_time).pack()

root.mainloop()