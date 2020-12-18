from tkinter import *
window = Tk()
canvas = Canvas(window, width=500, height=500)
canvas.pack()
my_image = PhotoImage(file='surge.png')
canvas.create_image(0, 0, anchor=NW, image=my_image)
window.mainloop()


