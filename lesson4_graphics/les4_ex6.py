import turtle
t = turtle.Pen()

def mycircle(red, green, blue):  #def = define, визначити
    t.color(red, green, blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

mycircle(1, 1, 0)
t.up()
t.forward(100)
t.down()
mycircle(0,1,1)
turtle.exitonclick()

