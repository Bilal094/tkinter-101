import tkinter as tk
root = tk.Tk()
windowSize = 50
root.geometry(f'{str(windowSize)}x{str(windowSize)}') 
colors = ['yellow', 'orange', 'red', 'purple', 'black']
colorIndex = 0
count = 6

def colorBg():
    global windowSize, colorIndex, count
    if windowSize == 350:
        root.destroy()
        print('BOOM!')
    elif windowSize == 50:
        print(count)
        windowSize += 50
        root.after(2000, colorBg)
    else:
        count -= 1
        print(count)
        windowSize += 50
        root.config(bg = colors[colorIndex])
        colorIndex += 1
        root.geometry(f'{str(windowSize)}x{str(windowSize)}') 
        root.after(2000, colorBg)

colorBg()
root.mainloop()