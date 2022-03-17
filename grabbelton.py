from random import random
import tkinter as tk
from tkinter import *

def grabbelen():
    randomItem = items.pop()
    itemMessage.set(f'Gefeliciteerd, je hebt een {randomItem} gegrabbeld!')
    print(f'Gefeliciteerd, je hebt een {randomItem} gegrabbeld!')
    itemQuantity.set(len(items))

items = ["horloge", "munt", "speld", "computermuis", "wol", "gouden tand", "telefoon", "oordopjes", "zakdoek", "lader"]

root = tk.Tk()

itemMessage = StringVar()

# Item quantity set up and display
textQuantity = tk.Label(text= 'Aantal items: ').pack()
itemQuantity = IntVar()
itemQuantity.set(len(items))
displayQuantity= tk.Label(textvariable=itemQuantity, font= ("Helvetica", 20)).pack()

message = tk.Label(textvariable=itemMessage, font= ('Helvetica', 15)).place(x=25,y=100)
button1 = tk.Button(text= 'grabbelen', font= ("Helvetica", 20), height= 5, width= 10, command= grabbelen).pack(expand = True)

root.mainloop()