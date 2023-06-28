import turtle

t = turtle.Turtle()
t.speed(1)
t.color("black")
t.begin_fill()


for i in range(3):
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.penup()
    t.forward(100)
    t.pendown()
t.end_fill()
t.hideturtle()
turtle.done()