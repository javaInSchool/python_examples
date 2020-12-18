from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)

    def draw(self):
        self.canvas.move(self.id, 0, -1) #команда руху вгору на 1 піксель

window = Tk()
window.title("Гра")
window.resizable(0, 0)
window.wm_attributes("-topmost", 1)
canvas = Canvas(window, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
window.update()

ball = Ball(canvas, 'red')

while 1:
    ball.draw()
    window.update_idletasks()
    window.update()
    time.sleep(0.01)