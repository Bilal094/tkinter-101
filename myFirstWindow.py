import tkinter 

window = tkinter.Tk()
# Start code
def phase1():
    print('5')
    window.configure(bg = 'yellow')
    window.geometry('100x100')
    window.after(2000, phase2)

def phase2():
    print('4')
    window.configure(bg = 'orange')
    window.geometry('150x150')
    window.after(2000, phase3)

def phase3():
    print('3')
    window.configure(bg = 'red')
    window.geometry('200x200')
    window.after(2000, phase4)

def phase4():
    print('2')
    window.configure(bg = 'purple')
    window.geometry('250x250')
    window.after(2000, phase5)

def phase5():
    print('1')
    window.configure(bg = 'black')
    window.geometry('300x300')
    window.after(2000, end)

def end():
    print('BOOM!')
    window.destroy()

window.geometry('50x50')
print('6')
window.after(2000, phase1)
# End code
window.mainloop()