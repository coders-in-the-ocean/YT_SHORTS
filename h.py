import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set the background color
screen = turtle.Screen()
screen.bgcolor("black")

# Set the pen color and size
pen.color("pink")
pen.pensize(3)

# Draw the flower
for i in range(10):
    pen.circle(10*i)
    pen.circle(-10*i)
    pen.left(20)

# Hide the turtle
pen.hideturtle()

# Keep the window open until closed manually
turtle.done()
