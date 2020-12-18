from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)

        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()  #Встановлення поточної висоти холста
        self.canvas_width = self.canvas.winfo_width()   #Встановлення поточної ширини холста

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)  #додали self.x, self.y замість 0 та -1
        pos = self.canvas.coords(self.id)  #створюємо список pos у який додаємо значення координат фігури з id
        #pos буде мати 4 координати - 2 для верхнього лівого кута прямокутрика та 2 для нижнього правогою
        #245 100 270 125
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.y = -1

tk = Tk()
tk.title("Игра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()
ball = Ball(canvas, 'red')
while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)