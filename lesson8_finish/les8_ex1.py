from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle,  color):
        #print("begin of init ball")
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        #print(" end of init ball")

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #print('Координати м\'яча', pos)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3

        if self.hit_paddle(pos) == True:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        #print("begin paddle init")
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10,fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        #print('Координати платформи', pos)

        if pos[0] <= 0:
            self.x = 0   #платформа має зупинятися , коли торкається межі полотна
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):       #рух ліворуч
        self.x = -2

    def turn_right(self, evt):  #рух праворуч
        self.x = 2

tk = Tk()
tk.title("Игра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

#print("when this line display ?")

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')    #додаємо платформу до об'єкту м'яча

while 1:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)