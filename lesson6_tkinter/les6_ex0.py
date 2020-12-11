from tkinter import *

def hello():
    print('привіт!')

window = Tk()  #як Pen() у черепашки, створює порожнє вікно
btn = Button(window, text="натисни на мене", command=hello)
btn.pack()

def person(width, height):
    print('Моя ширина - %s, а висота - %s' % (width, height))

person(4, 3)
window.mainloop()

