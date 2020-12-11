import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

def move(event):
    if event.keysym == 'Up':
        canvas.move(1,0,-5) # ID = 1, x = 0, y = -5
    elif event.keysym == 'Down':
        canvas.move(1,0,5)
    elif event.keysym == 'Left':
        canvas.move(1,-5,0)
    else:
        canvas.move(1,5,0)

canvas.bind_all('<KeyPress-Up>', move)
canvas.bind_all('<KeyPress-Down>', move)
canvas.bind_all('<KeyPress-Left>', move)
canvas.bind_all('<KeyPress-Right>', move)

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.05)
