# copyright Coders_in_The_Ocean 2023

import turtle

t = turtle.Turtle()
t.speed(10)
t.color('black', 'yellow')


def spider(size):
    t.begin_fill()
    for i in range(100):
        t.forward(size)
        t.left(360//7)
        size = size+1
    t.end_fill()


spider(10)
turtle.done()
