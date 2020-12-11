import time
from tkinter import *

class Ball:
    def __init__(self,canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id, 245,100)
    def draw(self):
        pass

tk = Tk()
tk.title("Ball game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width = 500, height = 400)
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')

while 1:
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
