from tkinter import *
import random

window = Tk()
canvas = Canvas(window, width=400, height=400)
canvas.pack()
canvas.create_rectangle(10, 10, 50, 50)

canvas.create_arc(10, 10, 200, 100, extent=180, style=ARC)

canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", outline="black")
canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="", outline="black")

canvas.create_text(150, 100, text='Был один человек из Тулузы,')

def random_rectangle(width, height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    canvas.create_rectangle(x1, y1, x2, y2)

random_rectangle(400, 400)

window.mainloop()

