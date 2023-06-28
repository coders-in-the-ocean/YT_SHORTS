"""
@Coders_in_the_Ocean
--------2023--------

"""
import turtle  
turtle.title("Coders in the Ocean")
turtle.bgcolor('black')
t = turtle.Turtle()
t.color('yellow')
# t.color("blue")
t.speed(10)
t.goto(-125, 0)

def sqrfunc(size):
    for i in range(50):
        t.fd(size)
        t.left(90)
        size = size-5

sqrfunc(300)

t.hideturtle()
turtle.done()
