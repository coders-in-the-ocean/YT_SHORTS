"""
@Coders_in_the_Ocean
2023
"""
import turtle
t = turtle.Turtle()
t.speed(10)
t.color('grey')

t.up()
t.goto(-200, 0)
t.down()
t.begin_fill()
t.fd(400)
t.left(90)
t.fd(100)
t.left(90)
t.fd(400)
t.left(90)
t.fd(100)
t.end_fill()

t.color('black')
t.pensize(3)
t.up()
t.goto(-150, 100)
t.down()
t.left(180-45)
t.fd(100)
t.right(45)
t.fd(150)
t.right(45)
t.fd(100)


t.up()
t.goto(-130, -20)
t.down()
t.begin_fill()
t.circle(40)
t.end_fill()

t.up()
t.goto(110, -20)
t.down()
t.begin_fill()
t.circle(40)
t.end_fill()

t.hideturtle()
turtle.done()
