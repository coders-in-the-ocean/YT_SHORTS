# @Coders_in_The_Ocean 2023

import turtle
import random

turtle.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.speed(15)
t.color("white")


def draw_star():
    for i in range(5):
        t.fd(15)
        t.right(144)


for j in range(100):
    x = random.randint(-640, 640)
    y = random.randint(-330, 330)
    draw_star()
    t.up()
    t.goto(x, y)
    t.down()


t.up()
t.goto(0, 200)
t.down()
t.begin_fill()
t.circle(100)
t.end_fill()


turtle.done()
