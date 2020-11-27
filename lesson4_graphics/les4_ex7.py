import turtle
t = turtle.Pen()

def mysquare(size):
    for x in range(1, 5):
        t.forward(size)
        t.left(90)

t.reset()
t.begin_fill()
mysquare(100)
t.end_fill()

turtle.exitonclick()