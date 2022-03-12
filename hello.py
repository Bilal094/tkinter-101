import tkinter as tk

root = tk.Tk()
root.title('Hello')
root.configure(bg = 'red')


box1 = tk.Label(text= 'Hello\ntkinter!', fg = 'blue', bg = 'green', font = ('Arial', 75))
box1.pack(ipadx = 100, ipady = 100, expand = True)

root.mainloop()

# You'll need to maximize the root's window for the correct view