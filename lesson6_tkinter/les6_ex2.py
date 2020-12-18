import time
from tkinter import *
window = Tk()
canvas = Canvas(window, width=700, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)

for x in range(0, 60):
    canvas.move(1, 10, 1) #дія для переміщення полотна, # ID = 1, x = 0, y = -5
    window.update()
    time.sleep(0.05)

window.mainloop()