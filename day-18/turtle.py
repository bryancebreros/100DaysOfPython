from turtle import Turtle, Screen, forward
import random
import turtle
tom = Turtle()
tom.speed("fastest")
turtle.colormode(255)


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tom.forward(100)
        tom.right(angle)


def pick_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_circle():
    tom.circle(100)


screen = Screen()

for i in range(16):
    tom.color(pick_color())
    draw_circle()
    tom.left(20)
# tom.down(100)
# tom.left(100)
# tom.up(100)
# tom.right(100)

screen.exitonclick()
